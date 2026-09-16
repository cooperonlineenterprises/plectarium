from __future__ import annotations

import hashlib
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


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


class PinnedGitInputTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="packet-pin-")
        self.root = Path(self.temporary.name) / "upstream"
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

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_newer_head_still_validates_pinned_object(self) -> None:
        self.assertEqual(
            VALIDATOR.check_git_pin(self.root, self.commit, self.remote, "fixture"),
            [],
        )
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
        errors = VALIDATOR.check_pinned_blob(
            self.root, self.commit, "locked.txt", hashlib.sha256(b"wrong").hexdigest(), "fixture"
        )
        self.assertTrue(any("digest mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
