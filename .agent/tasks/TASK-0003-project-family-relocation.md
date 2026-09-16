---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0003",
  "status": "completed",
  "previous_status": "review",
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
    "EVD-0008",
    "EVD-0009"
  ],
  "external_effects": "Local non-overwriting filesystem relocation, repository-local edits, validation, a local candidate commit, review, and local integration only; no push or other remote effect.",
  "limitations": [
    "All prior task, evidence, review, checkpoint, and event history remains preserved.",
    "Independent T1 reviewer /root/candidate_review_a approved exact integrated head 8bf3ca231f97c81151b677b322f1bffd96204723 using gpt-6-astra at max reasoning.",
    "The closure-only metadata commit requires a final read-only metadata audit.",
    "Future implementation or external action requires separate current authority.",
    "Product and production readiness remain unassessed."
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
- [x] The integrated evidence-bearing head received final read-only T1 approval.

## Completed integration and metadata-audit boundary

Independent T1 review `REV-0007` approved exact integrated head
`8bf3ca231f97c81151b677b322f1bffd96204723` with tree `1c76a7574151af15b66515028a7dc2376f770fa9`. Evidence `EVD-0009` records the main,
parent, preserved candidate branch, origin tracking, worktree, cleanliness,
validation, and no-effect observations.

The migration task is complete. The commit containing this closure-only review
and lifecycle metadata is newer than the reviewed head and remains subject to a
final read-only metadata audit. No product or production readiness is claimed,
and no push or other external effect is authorized.
