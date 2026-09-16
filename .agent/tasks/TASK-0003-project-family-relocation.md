---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0003",
  "status": "validating",
  "previous_status": "in_progress",
  "title": "Adopt the relocated Plectarium repository and immutable-pin validation",
  "authority_basis": "Current operator request dated 2026-09-15 for local Plectarium architectural remediation and workspace migration",
  "owner": "migration_implementation_agent",
  "created_at": "2026-09-15",
  "updated_at": "2026-09-15",
  "dependencies": [],
  "supersedes": null,
  "closure_evidence": ["EVD-0004"],
  "external_effects": "Local non-overwriting filesystem relocation, repository-local edits, validation, a local candidate commit, review, and local integration only; no push or other remote effect.",
  "limitations": [
    "Historical task, evidence, review, checkpoint, event, and provenance-lock bytes are preserved.",
    "Independent T1 review and serial local integration remain pending.",
    "Product implementation, publication, deployment, production access, and readiness are outside scope."
  ]
}
---

## Scope

- Preserve the independent Plectarium repository boundary while adopting its
  canonical checkout at `repos/plectarium`.
- Replace current host/path-specific validation commands with canonical sibling
  paths and an explicit local Python override.
- Validate immutable upstream pins from exact local commit objects and pinned
  blobs without requiring mutable upstream `HEAD` or `origin/main` equality.
- Replace stale current publication routing with a successor migration view
  while preserving every historical record and pin.
- Refresh only designated generated integrity after source and lifecycle
  records freeze.

## Acceptance criteria

- [x] The relocation baseline HEAD, tree, origin, and recovery bundle match the
  approved relocation manifest.
- [x] Packet, harness, mutation, immutable-pin, integrity, and
  `git diff --check` validation pass on the repository-local candidate.
- [x] Historical publication and provenance records remain byte-preserved.
- [x] No remote, deployment, product, production, or paid effect occurs.
- [ ] A distinct T1 reviewer approves the exact committed candidate.
- [ ] The approved candidate is integrated serially into local `main`.

## Candidate handoff

`EVD-0004` records the relocation baseline, implemented candidate, validation,
and limitations. This task remains in `validating`; it enters `review` only
after a repository-owned independent review record exists. No push is
authorized.
