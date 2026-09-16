#!/usr/bin/env python3
"""Read-only validator and explicit derived-integrity writer for the packet."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
PACKET_NAME = "plectarium-product-build-packet-v1"
PACKET_VERSION = "1.0.0"
MANIFEST = "PACKET-MANIFEST.json"
CHECKSUMS = "PACKET-CHECKSUMS.sha256"
INTEGRITY_REPORT = "INTEGRITY-REPORT.md"

REQUIRED_FILES = {
    "README.md", "CHARTER.md", "ARCHITECTURE.md", "SECURITY.md", "ROADMAP.md",
    "RELEASE-CRITERIA.md", "DECISIONS.md", "OPEN-QUESTIONS.md", "suite.yaml",
    "spec/invariants.md", "spec/terminology.md", "spec/product-experience.md",
    "spec/family-contract-profile.md", "spec/catalog-and-discovery.md",
    "spec/identity-tenancy-and-access.md", "spec/request-plan-and-approval.md",
    "spec/job-lifecycle.md", "spec/runner-coordination.md",
    "spec/artifact-result-provenance.md", "spec/api-event-and-queue-contracts.md",
    "spec/failure-recovery-and-idempotency.md", "spec/deployment-modes.md",
    "spec/privacy-retention-and-audit.md", "spec/operations-slos-and-migrations.md",
    "design/decisions.yaml", "design/decision-ledger.md", "design/module-boundaries.md",
    "design/data-ownership.md", "agent/BUILD-DIRECTIVE.md", "agent/authority.md",
    "agent/change-control.md", "agent/task-contract.md", "agent/validation-contract.md",
    "agent/workstreams.yaml", "agent/implementation-dependency-graph.yaml",
    "agent/tasks/index.yaml", "evals/EVALUATION-SPEC.md",
    "evals/claim-proof-matrix.md", "evals/release-gates.yaml",
    "evals/test-catalog.yaml", "evals/conformance-matrix.yaml",
    "fixtures/README.md", "fixtures/index.yaml", "fixtures/lifecycle/job-transitions.yaml",
    "reference/family-source-lock.json", "reference/source-map.md",
    "reference/prompt-coverage.md", "reference/internal-consistency-review.md",
    "research/source-register.md", "research/licensing.md", "scripts/validate-packet.py",
    MANIFEST, CHECKSUMS, INTEGRITY_REPORT,
}

REQUIRED_SCHEMAS = {
    "common-definitions.schema.json", "suite.schema.json",
    "family-source-lock.schema.json", "capability-coordinate.schema.json",
    "catalog-entry.schema.json", "suite-bom.schema.json",
    "policy-decision.schema.json", "request-plan-binding.schema.json",
    "job.schema.json", "execution-profile.schema.json", "runner.schema.json",
    "artifact-record.schema.json", "result-record.schema.json",
    "quota-retention-policy.schema.json", "audit-event.schema.json",
    "air-gap-bundle-manifest.schema.json", "problem.schema.json",
}

FAMILY_SCHEMA_NAMES = {
    "standalone-capability-manifest.v0.schema.json", "result-envelope.v0.schema.json",
    "result-reference.v0.schema.json", "permission-set.v0.schema.json",
    "completion.v0.schema.json", "imported-result.v0.schema.json",
}

FORBIDDEN_REPO_DIRS = {
    "apps", "components", "interfaces", "execution-profiles", "compatibility",
    "distributions", "deploy", "packages", "src", "crates", "containers",
}
FORBIDDEN_REPO_FILES = {
    "package.json", "pnpm-lock.yaml", "yarn.lock", "Cargo.toml", "Cargo.lock",
    "pyproject.toml", "requirements.txt", "go.mod", "go.sum", "Dockerfile",
    "docker-compose.yml", "docker-compose.yaml",
}

JOB_TRANSITIONS = {
    "received": {"planning", "failed", "cancelled"},
    "planning": {"awaiting_approval", "failed", "cancelled"},
    "awaiting_approval": {"queued", "denied", "expired", "cancelled", "failed"},
    "queued": {"leased", "cancel_requested", "failed"},
    "leased": {"running", "cancel_requested", "failed"},
    "running": {"finalizing", "cancel_requested", "failed"},
    "cancel_requested": {"cancelled", "finalizing", "failed"},
    "finalizing": {"completed", "cancelled", "failed"},
    "completed": set(), "denied": set(), "expired": set(), "cancelled": set(), "failed": set(),
}


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    path: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return {"code": self.code, "message": self.message, "path": self.path}


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader: UniqueKeyLoader, node: yaml.Node, deep: bool = False):
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"duplicate YAML key: {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
)


def strict_json(path: Path) -> Any:
    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream, object_pairs_hook=hook)


def strict_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return yaml.load(stream, Loader=UniqueKeyLoader)


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def packet_files(*, include_manifest: bool, include_checksums: bool) -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_symlink() or not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if any(part in {".git", "__pycache__"} for part in path.relative_to(ROOT).parts):
            continue
        if not include_manifest and rel == MANIFEST:
            continue
        if not include_checksums and rel == CHECKSUMS:
            continue
        paths.append(path)
    return sorted(paths, key=lambda item: item.relative_to(ROOT).as_posix())


def classification(rel: str) -> str:
    if rel.startswith("spec/schemas/") or rel.endswith(".yaml"):
        return "machine-readable-normative"
    if rel.startswith("spec/") or rel in {"CHARTER.md", "RELEASE-CRITERIA.md"}:
        return "normative"
    if rel.startswith(("design/", "agent/")) or rel in {"DECISIONS.md", "ROADMAP.md", "OPEN-QUESTIONS.md"}:
        return "governance"
    if rel.startswith(("evals/", "fixtures/")):
        return "verification"
    if rel.startswith("integrations/"):
        return "integration-boundary"
    if rel.startswith(("reference/", "research/")):
        return "provenance-reference"
    if rel.startswith("scripts/"):
        return "validation-tooling"
    if rel in {MANIFEST, CHECKSUMS, INTEGRITY_REPORT}:
        return "packet-integrity"
    if rel == "SECURITY.md":
        return "security-governance"
    return "project-context"


def build_manifest() -> dict[str, Any]:
    decisions = strict_yaml(ROOT / "design/decisions.yaml")["decisions"]
    tasks = strict_yaml(ROOT / "agent/tasks/index.yaml")["tasks"]
    gates = strict_yaml(ROOT / "evals/release-gates.yaml")["gates"]
    lock = strict_json(ROOT / "reference/family-source-lock.json")
    files = []
    for path in packet_files(include_manifest=False, include_checksums=False):
        rel = path.relative_to(ROOT).as_posix()
        files.append({"path": rel, "sha256": digest(path), "bytes": path.stat().st_size, "classification": classification(rel)})
    limitations = ["Packet integrity is not product readiness."]
    if lock["publication_status"] == "pending":
        limitations.append("Family publication equality remains unresolved while family_source.publication_status is pending.")
    else:
        limitations.append("Resolved family bytes still require explicit --family-root verification; the lock alone is not trust or authority.")
    return {
        "schema_version": "plectarium.build-packet-manifest.v1",
        "packet": {"name": PACKET_NAME, "version": PACKET_VERSION, "generated_date": "2026-08-31", "purpose": "Setup-only Product Constitution, Executable Specification, and AI Build Packet for Plectarium."},
        "authority_hierarchy": ["CHARTER.md", "spec/invariants.md", "normative specifications and schemas", "accepted ADRs", "RELEASE-CRITERIA.md and evals/release-gates.yaml", "agent/workstreams.yaml", "agent/tasks/index.yaml and task packets", "later authorized implementation choices"],
        "family_source": {"family_id": lock["family_id"], "packet_version": lock["packet_version"], "publication_status": lock["publication_status"], "git_commit": lock["git_commit"], "packet_manifest_sha256": lock["packet_manifest_sha256"]},
        "counts": {"content_files": len(files), "json_schemas": len(list((ROOT / "spec/schemas").glob("*.schema.json"))), "decisions": len(decisions), "tasks": len(tasks), "release_gates": len(gates), "ready_implementation_tasks": sum(1 for task in tasks if task["status"] == "ready")},
        "integrity": {"manifest_scope": f"All packet files except {MANIFEST} and {CHECKSUMS}.", "checksums_scope": f"All packet files except {CHECKSUMS}, including {MANIFEST}.", "algorithm": "SHA-256", "writer": "scripts/validate-packet.py --refresh-derived"},
        "files": files,
        "limitations": limitations,
    }


def atomic_text(path: Path, content: str) -> None:
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False, prefix=f".{path.name}.", suffix=".tmp") as stream:
        stream.write(content)
        temporary = Path(stream.name)
    os.replace(temporary, path)


def refresh() -> None:
    lock = strict_json(ROOT / "reference/family-source-lock.json")
    if lock["publication_status"] == "resolved":
        family_line = "- The family publication pin is resolved; validate its exact commit and file digests with `--family-root` before relying on it."
    else:
        family_line = "- The family publication pin is pending; publication must not proceed until it is resolved and verified."
    report = f"""# Packet Integrity Report\n\nGenerated only by `scripts/validate-packet.py --refresh-derived`.\n\n- Packet: `plectarium-product-build-packet-v1`\n- Version: `1.0.0`\n- Algorithm: SHA-256\n- Manifest excludes itself and the checksum sidecar.\n- Checksum sidecar includes the manifest and excludes itself.\n- Integrity establishes byte consistency, not product readiness.\n{family_line}\n"""
    atomic_text(ROOT / INTEGRITY_REPORT, report)
    manifest = build_manifest()
    atomic_text(ROOT / MANIFEST, json.dumps(manifest, indent=2, sort_keys=False) + "\n")
    lines = []
    for path in packet_files(include_manifest=True, include_checksums=False):
        lines.append(f"{digest(path)}  {path.relative_to(ROOT).as_posix()}")
    atomic_text(ROOT / CHECKSUMS, "\n".join(lines) + "\n")


def schema_registry() -> tuple[dict[str, Any], Registry, list[Finding]]:
    schemas: dict[str, Any] = {}
    resources: list[tuple[str, Resource[Any]]] = []
    findings: list[Finding] = []
    for path in sorted((ROOT / "spec/schemas").glob("*.schema.json")):
        rel = path.relative_to(ROOT).as_posix()
        try:
            value = strict_json(path)
            Draft202012Validator.check_schema(value)
            schema_id = value.get("$id")
            if not isinstance(schema_id, str) or schema_id in schemas:
                raise ValueError("missing or duplicate $id")
            schemas[schema_id] = value
            resources.append((schema_id, Resource.from_contents(value)))
        except Exception as error:
            findings.append(Finding("schema.invalid", str(error), rel))
    registry = Registry().with_resources(resources)
    return schemas, registry, findings


def validator_for(name: str, schemas: dict[str, Any], registry: Registry) -> Draft202012Validator:
    path = ROOT / "spec/schemas" / name
    value = strict_json(path)
    return Draft202012Validator(value, registry=registry, format_checker=FormatChecker())


def validate_instance(value: Any, name: str, schemas: dict[str, Any], registry: Registry) -> list[str]:
    return [error.message for error in validator_for(name, schemas, registry).iter_errors(value)]


def check_files() -> list[Finding]:
    findings: list[Finding] = []
    for rel in sorted(REQUIRED_FILES):
        path = ROOT / rel
        if not path.is_file():
            findings.append(Finding("file.missing", "required file missing", rel))
    schema_names = {path.name for path in (ROOT / "spec/schemas").glob("*.schema.json")}
    for missing in sorted(REQUIRED_SCHEMAS - schema_names):
        findings.append(Finding("schema.missing", "required schema missing", f"spec/schemas/{missing}"))
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT).as_posix()
        if path.is_symlink():
            findings.append(Finding("path.symlink", "symlinks are prohibited", rel))
        elif path.exists() and not path.is_file() and not path.is_dir():
            findings.append(Finding("path.special", "special files are prohibited", rel))
        if path.name in {".DS_Store", "Thumbs.db"} or path.suffix == ".pyc" or "__pycache__" in path.parts:
            findings.append(Finding("path.transient", "host/cache/bytecode artifact prohibited", rel))
        if path.is_file() and path.stat().st_size == 0:
            findings.append(Finding("file.empty", "empty files are prohibited", rel))
        if path.is_file() and path.name in FAMILY_SCHEMA_NAMES:
            findings.append(Finding("family.fork", "family schemas must be consumed externally, not copied", rel))
    for name in sorted(FORBIDDEN_REPO_DIRS):
        if (REPO / name).exists():
            findings.append(Finding("implementation.present", "implementation-time root prohibited during foundation", name))
    for name in sorted(FORBIDDEN_REPO_FILES):
        if (REPO / name).exists():
            findings.append(Finding("dependency.present", "product dependency/build file prohibited during foundation", name))
    return findings


def check_parsing_and_text() -> list[Finding]:
    findings: list[Finding] = []
    secret_patterns = [r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", r"\bghp_[A-Za-z0-9]{20,}\b", r"\bAKIA[0-9A-Z]{16}\b"]
    placeholder_patterns = [r"\bTODO\b", r"\bFIXME\b", r"replace_with"]
    for path in packet_files(include_manifest=True, include_checksums=True):
        rel = path.relative_to(ROOT).as_posix()
        try:
            if path.suffix == ".json":
                strict_json(path)
            elif path.suffix in {".yaml", ".yml"}:
                strict_yaml(path)
        except Exception as error:
            findings.append(Finding("parse.invalid", str(error), rel))
            continue
        if path.suffix.lower() in {".md", ".json", ".yaml", ".yml", ".py"}:
            text = path.read_text(encoding="utf-8")
            for pattern in secret_patterns:
                if re.search(pattern, text):
                    findings.append(Finding("secret.detected", "secret-like material detected", rel))
            if not rel.startswith("scripts/"):
                for pattern in placeholder_patterns:
                    if re.search(pattern, text, re.I):
                        findings.append(Finding("placeholder.detected", f"unclassified placeholder pattern {pattern}", rel))
            if path.suffix == ".md" and len(text.strip()) < 80:
                findings.append(Finding("content.thin", "Markdown file is not substantive", rel))
    return findings


def check_schemas_and_fixtures(schemas: dict[str, Any], registry: Registry) -> list[Finding]:
    findings: list[Finding] = []
    checks = [
        (strict_yaml(ROOT / "suite.yaml"), "suite.schema.json", "suite.yaml"),
        (strict_json(ROOT / "reference/family-source-lock.json"), "family-source-lock.schema.json", "reference/family-source-lock.json"),
    ]
    for value, schema_name, rel in checks:
        for error in validate_instance(value, schema_name, schemas, registry):
            findings.append(Finding("instance.invalid", error, rel))

    index = strict_yaml(ROOT / "fixtures/index.yaml")
    for item in index.get("fixtures", []):
        rel = f"fixtures/{item['path']}"
        value = strict_json(ROOT / rel)
        errors = validate_instance(value, item["schema"], schemas, registry)
        if "accepted_permissions_subset" in item.get("semantic_checks", []):
            if not set(value.get("accepted_permissions", [])).issubset(value.get("requested_permissions", [])):
                errors.append("accepted permissions are not a subset of requested permissions")
        expected = bool(item["expected_valid"])
        actual = not errors
        if actual != expected:
            findings.append(Finding("fixture.expectation", f"expected valid={expected}, errors={errors}", rel))

    graph = strict_yaml(ROOT / "fixtures/lifecycle/job-transitions.yaml")
    for case in graph.get("cases", []):
        states = case.get("states", [])
        actual = bool(states) and all(right in JOB_TRANSITIONS.get(left, set()) for left, right in zip(states, states[1:]))
        if actual != bool(case.get("expected_valid")):
            findings.append(Finding("lifecycle.fixture", f"case {case.get('id')} expectation mismatch", "fixtures/lifecycle/job-transitions.yaml"))
    return findings


def check_graphs() -> list[Finding]:
    findings: list[Finding] = []
    workstreams = strict_yaml(ROOT / "agent/workstreams.yaml").get("workstreams", [])
    work_ids = [item.get("id") for item in workstreams]
    if len(work_ids) != len(set(work_ids)):
        findings.append(Finding("workstream.duplicate", "duplicate workstream ID", "agent/workstreams.yaml"))

    stage_data = strict_yaml(ROOT / "agent/implementation-dependency-graph.yaml")
    stages = stage_data.get("stages", [])
    stage_ids = {item.get("id") for item in stages}
    for item in stages:
        for dep in item.get("depends_on", []):
            if dep not in stage_ids:
                findings.append(Finding("stage.reference", f"unknown stage dependency {dep}", "agent/implementation-dependency-graph.yaml"))

    tasks = strict_yaml(ROOT / "agent/tasks/index.yaml").get("tasks", [])
    task_ids = [item.get("id") for item in tasks]
    if len(task_ids) != len(set(task_ids)):
        findings.append(Finding("task.duplicate", "duplicate task ID", "agent/tasks/index.yaml"))
    task_map = {item["id"]: item for item in tasks}
    ready = [item["id"] for item in tasks if item.get("status") == "ready"]
    if ready != ["PLEC-FND-001"]:
        findings.append(Finding("task.ready", f"exactly PLEC-FND-001 must be ready, got {ready}", "agent/tasks/index.yaml"))
    for task in tasks:
        if task.get("status") not in {"ready", "blocked"}:
            findings.append(Finding("task.status", "initial task status must be ready or blocked", "agent/tasks/index.yaml"))
        if task.get("workstream") not in set(work_ids):
            findings.append(Finding("task.workstream", f"unknown workstream for {task['id']}", "agent/tasks/index.yaml"))
        if task.get("stage") not in stage_ids:
            findings.append(Finding("task.stage", f"unknown stage for {task['id']}", "agent/tasks/index.yaml"))
        if not (ROOT / "agent/tasks" / f"{task['id']}.md").is_file():
            findings.append(Finding("task.packet", "missing individual task packet", f"agent/tasks/{task['id']}.md"))
        for dep in task.get("dependencies", []):
            if dep not in task_map:
                findings.append(Finding("task.reference", f"unknown dependency {dep}", "agent/tasks/index.yaml"))

    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(task_id: str) -> None:
        if task_id in visiting:
            findings.append(Finding("task.cycle", f"dependency cycle includes {task_id}", "agent/tasks/index.yaml"))
            return
        if task_id in visited:
            return
        visiting.add(task_id)
        for dep in task_map[task_id].get("dependencies", []):
            if dep in task_map:
                visit(dep)
        visiting.remove(task_id)
        visited.add(task_id)
    for task_id in task_map:
        visit(task_id)
    return findings


def check_claims() -> list[Finding]:
    findings: list[Finding] = []
    tests = strict_yaml(ROOT / "evals/test-catalog.yaml").get("tests", [])
    test_ids = [item.get("id") for item in tests]
    if len(test_ids) != len(set(test_ids)):
        findings.append(Finding("test.duplicate", "duplicate test ID", "evals/test-catalog.yaml"))
    gates = strict_yaml(ROOT / "evals/release-gates.yaml").get("gates", [])
    gate_ids = [item.get("id") for item in gates]
    if len(gate_ids) != len(set(gate_ids)):
        findings.append(Finding("gate.duplicate", "duplicate release gate ID", "evals/release-gates.yaml"))
    test_set = set(test_ids)
    for gate in gates:
        if gate.get("status") not in {"foundation_only", "unassessed", "blocked", "partial", "failed", "passed"}:
            findings.append(Finding("gate.status", f"unknown status for {gate.get('id')}", "evals/release-gates.yaml"))
        if not gate.get("tests"):
            findings.append(Finding("gate.tests", f"gate {gate.get('id')} has no tests", "evals/release-gates.yaml"))
        for test in gate.get("tests", []):
            if test not in test_set:
                findings.append(Finding("gate.reference", f"unknown test {test}", "evals/release-gates.yaml"))
    conformance = strict_yaml(ROOT / "evals/conformance-matrix.yaml").get("contracts", [])
    for item in conformance:
        for test in item.get("required_tests", []):
            if test not in test_set:
                findings.append(Finding("conformance.reference", f"unknown test {test}", "evals/conformance-matrix.yaml"))
    matrix = (ROOT / "evals/claim-proof-matrix.md").read_text(encoding="utf-8")
    for gate_id in gate_ids:
        if gate_id not in matrix:
            findings.append(Finding("claim.coverage", f"claim-proof matrix does not mention {gate_id}", "evals/claim-proof-matrix.md"))
    return findings


def check_links() -> list[Finding]:
    findings: list[Finding] = []
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        for target in pattern.findall(path.read_text(encoding="utf-8")):
            target = target.strip("<>").split("#", 1)[0]
            if not target or re.match(r"^(?:https?://|mailto:)", target):
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                findings.append(Finding("link.escape", f"link escapes packet: {target}", rel))
                continue
            if not candidate.exists():
                findings.append(Finding("link.missing", f"missing local link target {target}", rel))
    return findings


def check_integrity() -> list[Finding]:
    findings: list[Finding] = []
    for name in (MANIFEST, CHECKSUMS, INTEGRITY_REPORT):
        if not (ROOT / name).is_file():
            findings.append(Finding("integrity.missing", "run the designated refresh writer", name))
    if findings:
        return findings
    try:
        actual = strict_json(ROOT / MANIFEST)
        expected = build_manifest()
        if actual != expected:
            findings.append(Finding("integrity.manifest", "manifest inventory or hashes are stale", MANIFEST))
        lines = (ROOT / CHECKSUMS).read_text(encoding="utf-8").splitlines()
        observed: dict[str, str] = {}
        for number, line in enumerate(lines, 1):
            match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
            if not match or match.group(2) in observed:
                findings.append(Finding("integrity.checksum-format", f"invalid or duplicate line {number}", CHECKSUMS))
                continue
            observed[match.group(2)] = match.group(1)
        expected_hashes = {path.relative_to(ROOT).as_posix(): digest(path) for path in packet_files(include_manifest=True, include_checksums=False)}
        if observed != expected_hashes:
            findings.append(Finding("integrity.checksums", "checksum inventory or hashes are stale", CHECKSUMS))
        temps = list(ROOT.rglob("*.tmp"))
        if temps:
            findings.append(Finding("integrity.transient", "interrupted refresh temporary files present", temps[0].relative_to(ROOT).as_posix()))
    except Exception as error:
        findings.append(Finding("integrity.invalid", str(error), MANIFEST))
    return findings


_SAFE_GIT_ENVIRONMENT = {
    "PATH": "/usr/bin:/bin",
    "LC_ALL": "C",
    "LANG": "C",
    "GIT_OPTIONAL_LOCKS": "0",
    "GIT_TERMINAL_PROMPT": "0",
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_NO_LAZY_FETCH": "1",
    "GIT_NO_REPLACE_OBJECTS": "1",
    "GIT_PROTOCOL_FROM_USER": "0",
}
_VALIDATED_GIT_ROOTS: set[Path] = set()


def _git_environment() -> dict[str, str]:
    environment = {
        key: value for key, value in os.environ.items() if not key.startswith("GIT_")
    }
    environment.update(_SAFE_GIT_ENVIRONMENT)
    return environment


def _git(root: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [
            "git",
            "-c", "core.fsmonitor=false",
            "-c", "core.untrackedCache=false",
            "-c", "maintenance.auto=false",
            "-c", "gc.auto=0",
            "-c", "protocol.allow=never",
            "-c", "credential.helper=",
            "-C", str(root),
            *args,
        ],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        check=False,
        env=_git_environment(),
    )


def validate_supplied_root(raw_root: str | os.PathLike[str], label: str) -> tuple[Path | None, list[str]]:
    import stat as stat_module

    try:
        raw_text = os.fspath(raw_root)
    except TypeError:
        return None, [f"{label} root is not path-like"]
    if not isinstance(raw_text, str) or not raw_text or "\x00" in raw_text:
        return None, [f"{label} root is empty or invalid"]
    if os.path.normpath(raw_text) != raw_text:
        return None, [f"{label} root is not lexically normalized"]

    absolute = Path(os.path.abspath(raw_text))
    current = Path(absolute.anchor)
    components = [current]
    for part in absolute.parts[1:]:
        current = current / part
        components.append(current)
    for component in components:
        try:
            mode = os.lstat(component).st_mode
        except OSError as error:
            return None, [f"{label} root component is unavailable: {component}: {error.strerror}"]
        if stat_module.S_ISLNK(mode):
            return None, [f"{label} root contains a symlink component: {component}"]

    try:
        resolved = absolute.resolve(strict=True)
    except OSError as error:
        return None, [f"{label} root cannot be resolved: {error}"]
    if not resolved.is_dir():
        return None, [f"{label} root is not a directory"]
    return resolved, []


def validated_root_arg(value: str) -> Path:
    root, errors = validate_supplied_root(value, "supplied")
    if root is None:
        raise argparse.ArgumentTypeError("; ".join(errors))
    return root


def _decoded_git_path(result: subprocess.CompletedProcess[bytes], label: str) -> tuple[Path | None, list[str]]:
    if result.returncode != 0:
        return None, [f"{label} is unavailable"]
    try:
        value = result.stdout.decode("utf-8").strip()
    except UnicodeDecodeError:
        return None, [f"{label} is not UTF-8"]
    try:
        return Path(value).resolve(strict=True), []
    except OSError as error:
        return None, [f"{label} cannot be resolved: {error}"]


def _standalone_git_root(raw_root: str | os.PathLike[str], label: str) -> tuple[Path | None, list[str]]:
    root, errors = validate_supplied_root(raw_root, label)
    if root is None:
        return None, errors

    git_entry = root / ".git"
    try:
        import stat as stat_module
        git_mode = os.lstat(git_entry).st_mode
    except OSError as error:
        return None, errors + [f"{label} .git entry is unavailable: {error.strerror}"]
    if not stat_module.S_ISDIR(git_mode):
        return None, errors + [f"{label} .git is not a standalone directory"]
    expected_git = git_entry.resolve(strict=True)

    top, top_errors = _decoded_git_path(
        _git(root, "rev-parse", "--show-toplevel"), f"{label} top-level"
    )
    git_dir, git_dir_errors = _decoded_git_path(
        _git(root, "rev-parse", "--absolute-git-dir"), f"{label} git-dir"
    )
    common_dir, common_errors = _decoded_git_path(
        _git(root, "rev-parse", "--path-format=absolute", "--git-common-dir"),
        f"{label} common-dir",
    )
    errors += top_errors + git_dir_errors + common_errors
    if top is not None and top != root:
        errors.append(f"{label} top-level escapes the supplied root")
    if git_dir is not None and git_dir != expected_git:
        errors.append(f"{label} git-dir is not confined to root/.git")
    if common_dir is not None and common_dir != expected_git:
        errors.append(f"{label} common-dir is not confined to root/.git")
    return (root, errors) if not errors else (None, errors)


def _safe_git_path(value: str) -> bool:
    path = Path(value)
    return (
        bool(value)
        and not path.is_absolute()
        and "." not in path.parts
        and ".." not in path.parts
        and "\x00" not in value
        and ":" not in value
    )


def check_git_pin(
    raw_root: str | os.PathLike[str], commit: str, remote: str, label: str
) -> list[str]:
    root, errors = _standalone_git_root(raw_root, label)
    if root is None:
        return errors
    if re.fullmatch(r"[0-9a-f]{40}", commit) is None:
        return errors + [f"{label} commit pin is not a full lowercase object ID"]

    origin = _git(
        root, "config", "--local", "--no-includes", "--get", "remote.origin.url"
    )
    if (
        origin.returncode != 0
        or origin.stdout.decode("utf-8", errors="replace").strip() != remote
    ):
        errors.append(f"{label} raw local origin URL does not match lock")
    if _git(root, "cat-file", "-e", f"{commit}^{{commit}}").returncode != 0:
        errors.append(f"{label} pinned commit object is missing")
    if not errors:
        _VALIDATED_GIT_ROOTS.add(root)
    return errors


def _approved_git_root(raw_root: str | os.PathLike[str]) -> Path | None:
    root, errors = validate_supplied_root(raw_root, "Git")
    if root is None or errors or root not in _VALIDATED_GIT_ROOTS:
        return None
    return root


def git_blob(raw_root: str | os.PathLike[str], commit: str, path: str) -> bytes | None:
    root = _approved_git_root(raw_root)
    if (
        root is None
        or re.fullmatch(r"[0-9a-f]{40}", commit) is None
        or not _safe_git_path(path)
    ):
        return None
    result = _git(root, "cat-file", "blob", f"{commit}:{path}")
    return result.stdout if result.returncode == 0 else None


def git_tree_files(
    raw_root: str | os.PathLike[str], commit: str, path: str
) -> list[str] | None:
    root = _approved_git_root(raw_root)
    if (
        root is None
        or re.fullmatch(r"[0-9a-f]{40}", commit) is None
        or not _safe_git_path(path)
    ):
        return None
    result = _git(root, "ls-tree", "-z", "--name-only", f"{commit}:{path}")
    if result.returncode != 0:
        return None
    try:
        return sorted(
            item.decode("utf-8") for item in result.stdout.split(b"\0") if item
        )
    except UnicodeDecodeError:
        return None


def check_pinned_blob(
    root: str | os.PathLike[str],
    commit: str,
    path: str,
    expected_sha256: str,
    label: str,
) -> list[str]:
    blob = git_blob(root, commit, path)
    if blob is None:
        return [f"{label} pinned file is missing: {path}"]
    if hashlib.sha256(blob).hexdigest() != expected_sha256:
        return [f"{label} pinned file digest mismatch: {path}"]
    return []

def check_family_root(path: Path | None) -> list[Finding]:
    if path is None:
        return []
    findings: list[Finding] = []
    lock = strict_json(ROOT / "reference/family-source-lock.json")
    if lock["publication_status"] != "resolved":
        return [Finding("family.pending", "cannot verify a family root while the lock is pending", "reference/family-source-lock.json")]
    commit = lock["git_commit"]
    for error in check_git_pin(path, commit, lock["repository"], "family"):
        findings.append(Finding("family.git-pin", error, str(path)))
    packet_path = lock["packet_path"]
    for error in check_pinned_blob(path, commit, f"{packet_path}/PACKET-MANIFEST.json", lock["packet_manifest_sha256"], "family"):
        findings.append(Finding("family.manifest", error, f"{packet_path}/PACKET-MANIFEST.json"))
    for error in check_pinned_blob(path, commit, f"{packet_path}/PACKET-CHECKSUMS.sha256", lock["packet_checksums_sha256"], "family"):
        findings.append(Finding("family.checksums", error, f"{packet_path}/PACKET-CHECKSUMS.sha256"))
    for item in lock["contracts"]:
        target = f"{packet_path}/{item['path']}"
        for error in check_pinned_blob(path, commit, target, item["sha256"], "family contract"):
            findings.append(Finding("family.contract", error, item["path"]))
    return findings


def run(family_root: Path | None = None) -> list[Finding]:
    findings = check_files()
    findings.extend(check_parsing_and_text())
    schemas, registry, schema_findings = schema_registry()
    findings.extend(schema_findings)
    if not schema_findings:
        findings.extend(check_schemas_and_fixtures(schemas, registry))
    findings.extend(check_graphs())
    findings.extend(check_claims())
    findings.extend(check_links())
    findings.extend(check_integrity())
    findings.extend(check_family_root(family_root))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Plectarium product build packet without implementing the product.")
    parser.add_argument("--refresh-derived", action="store_true", help="Explicitly refresh packet manifest, checksums, and integrity report before checking.")
    parser.add_argument("--family-root", type=validated_root_arg, help="Explicit local family repository root for immutable pin verification.")
    parser.add_argument("--json", action="store_true", help="Emit structured result output.")
    args = parser.parse_args()
    if args.refresh_derived:
        refresh()
    findings = run(args.family_root if args.family_root else None)
    if args.json:
        print(json.dumps({"result": "PASS" if not findings else "FAIL", "packet": PACKET_NAME, "version": PACKET_VERSION, "findings": [item.as_dict() for item in findings], "limitations": ["Product implementation and readiness are not assessed."]}, indent=2))
    else:
        for item in findings:
            location = f" [{item.path}]" if item.path else ""
            print(f"[FAIL] {item.code}: {item.message}{location}", file=sys.stderr)
        if not findings:
            print("[PASS] Plectarium packet structure, contracts, fixtures, graphs, claims, manifest, and checksums")
            print("[INFO] product implementation, security efficacy, operations, and release readiness remain unassessed")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
