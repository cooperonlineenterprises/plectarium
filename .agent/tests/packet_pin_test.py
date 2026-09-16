from __future__ import annotations

import hashlib
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = next(ROOT.glob("*-build-packet-v1/scripts/validate-packet.py"))
SPEC = importlib.util.spec_from_file_location("packet_pin_validator", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load packet validator: {VALIDATOR_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def snapshot(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


class PinnedGitInputTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="packet-pin-")
        temporary_root = Path(self.temporary.name).resolve()
        self.root = temporary_root / "upstream"
        self.root.mkdir()
        git(self.root, "init", "-q", "-b", "main")
        git(self.root, "config", "user.name", "Packet Pin Test")
        git(self.root, "config", "user.email", "packet-pin@example.invalid")
        git(self.root, "config", "commit.gpgSign", "false")
        self.remote = "https://example.invalid/upstream.git"
        git(self.root, "remote", "add", "origin", self.remote)
        self.pinned_bytes = b"pinned bytes\n"
        (self.root / "locked.txt").write_bytes(self.pinned_bytes)
        git(self.root, "add", "locked.txt")
        git(self.root, "commit", "-q", "-m", "pinned")
        self.commit = git(self.root, "rev-parse", "HEAD")
        (self.root / "locked.txt").write_bytes(b"newer bytes\n")
        git(self.root, "commit", "-q", "-am", "newer")
        self.newer_commit = git(self.root, "rev-parse", "HEAD")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def approve_root(self, remote: str | None = None) -> None:
        self.assertEqual(
            VALIDATOR.check_git_pin(
                self.root, self.commit, remote or self.remote, "fixture"
            ),
            [],
        )

    def test_newer_head_still_validates_pinned_object(self) -> None:
        self.approve_root()
        self.assertEqual(
            VALIDATOR.git_blob(self.root, self.commit, "locked.txt"),
            self.pinned_bytes,
        )

    def test_missing_commit_fails_closed(self) -> None:
        errors = VALIDATOR.check_git_pin(
            self.root, "0" * 40, self.remote, "fixture"
        )
        self.assertTrue(any("commit object is missing" in error for error in errors))

    def test_wrong_digest_fails_closed(self) -> None:
        self.approve_root()
        errors = VALIDATOR.check_pinned_blob(
            self.root,
            self.commit,
            "locked.txt",
            hashlib.sha256(b"wrong").hexdigest(),
            "fixture",
        )
        self.assertTrue(any("digest mismatch" in error for error in errors))

    def test_inherited_git_directory_and_work_tree_are_ignored(self) -> None:
        with mock.patch.dict(
            os.environ,
            {
                "GIT_DIR": "/nonexistent/hostile-git-dir",
                "GIT_WORK_TREE": "/nonexistent/hostile-work-tree",
                "GIT_CONFIG_GLOBAL": "/nonexistent/hostile-config",
                "PATH": "/nonexistent/hostile-path",
            },
            clear=False,
        ):
            self.approve_root()

    def test_raw_origin_rejects_instead_of_substitution(self) -> None:
        git(self.root, "remote", "set-url", "origin", "shortcut:upstream.git")
        git(
            self.root,
            "config",
            f"url.{self.remote.removesuffix('upstream.git')}.insteadOf",
            "shortcut:",
        )
        errors = VALIDATOR.check_git_pin(
            self.root, self.commit, self.remote, "fixture"
        )
        self.assertTrue(any("raw local origin URL" in error for error in errors))

    def test_replacement_refs_do_not_change_pinned_bytes(self) -> None:
        self.approve_root()
        git(self.root, "replace", self.commit, self.newer_commit)
        self.assertEqual(
            VALIDATOR.git_blob(self.root, self.commit, "locked.txt"),
            self.pinned_bytes,
        )

    def test_promisor_missing_blob_does_not_fetch_or_write(self) -> None:
        remote_root = self.root.parent / "remote.git"
        git(self.root.parent, "clone", "-q", "--bare", str(self.root), str(remote_root))
        remote_url = remote_root.resolve().as_uri()
        git(self.root, "remote", "set-url", "origin", remote_url)
        git(self.root, "config", "remote.origin.promisor", "true")
        git(self.root, "config", "remote.origin.partialclonefilter", "blob:none")
        git(self.root, "config", "extensions.partialClone", "origin")
        self.approve_root(remote_url)
        blob_oid = git(self.root, "rev-parse", f"{self.commit}:locked.txt")
        object_path = self.root / ".git" / "objects" / blob_oid[:2] / blob_oid[2:]
        self.assertTrue(object_path.is_file())
        object_path.unlink()
        before = snapshot(self.root / ".git")
        self.assertIsNone(
            VALIDATOR.git_blob(self.root, self.commit, "locked.txt")
        )
        self.assertEqual(snapshot(self.root / ".git"), before)

    def test_symlink_alias_is_rejected_before_resolution(self) -> None:
        alias = self.root.parent / "alias"
        alias.symlink_to(self.root, target_is_directory=True)
        _, errors = VALIDATOR.validate_supplied_root(str(alias), "fixture")
        self.assertTrue(any("symlink component" in error for error in errors))

    def test_redundant_traversal_is_rejected_before_resolution(self) -> None:
        raw = f"{self.root}/../{self.root.name}"
        _, errors = VALIDATOR.validate_supplied_root(raw, "fixture")
        self.assertTrue(any("not lexically normalized" in error for error in errors))

    def test_linked_worktree_common_dir_is_rejected(self) -> None:
        linked = self.root.parent / "linked"
        git(
            self.root,
            "worktree",
            "add",
            "-q",
            "-b",
            "linked-test",
            str(linked),
            self.newer_commit,
        )
        errors = VALIDATOR.check_git_pin(
            linked, self.commit, self.remote, "fixture"
        )
        self.assertTrue(
            any(
                ".git is not a standalone directory" in error
                or "common-dir is not confined" in error
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
