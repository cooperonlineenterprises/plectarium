---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0003",
  "status": "review",
  "previous_status": "validating",
  "title": "Adopt the relocated Plectarium repository and immutable-pin validation",
  "authority_basis": "Current operator request dated 2026-09-15 for local Plectarium architectural remediation and workspace migration",
  "owner": "migration_implementation_agent",
  "created_at": "2026-09-15",
  "updated_at": "2026-09-15",
  "dependencies": [],
  "supersedes": null,
  "closure_evidence": [
    "EVD-0004",
    "EVD-0005",
    "EVD-0006",
    "EVD-0007",
    "EVD-0008"
  ],
  "external_effects": "Local non-overwriting filesystem relocation, repository-local edits, validation, a local candidate commit, review, and local integration only; no push or other remote effect.",
  "limitations": [
    "All prior task, evidence, review, checkpoint, and event history remains preserved.",
    "Local main contains approved migration head 2b301b437490ca49317cabbcccf80a929f633817; candidate branch remains preserved at that commit.",
    "origin/main remains at the pre-migration commit because no push was authorized or performed.",
    "The integrated evidence head requires final read-only T1 review before task completion.",
    "Product implementation, publication, deployment, production access, and readiness remain outside scope."
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
- [x] A distinct T1 reviewer approved the exact corrected source candidate.
- [x] The corrected evidence-bearing head received approval for serial local integration.
- [x] The approved candidate is integrated serially into local `main`.
- [ ] The integrated evidence-bearing head receives final read-only T1 review.

## Integrated state and final-review boundary

Immediately before this integration-evidence successor, local `main` equaled
approved head `2b301b437490ca49317cabbcccf80a929f633817` with tree `27f8d4fe25fa2e5538aafb60c9b9be44d2c782c4`; the preserved candidate branch
pointed to the same commit. Evidence `EVD-0008` records clean status, one
canonical worktree, unchanged origin, unchanged pre-migration `origin/main`,
and passing family aggregate strict topology.

This task remains in `review`. Final read-only T1 review of the integrated
evidence-bearing head is the sole remaining migration gate. Only after that
review may the primary integrator append a task-completion successor. No push
or other external effect is authorized.
