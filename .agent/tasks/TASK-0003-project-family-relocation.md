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
    "EVD-0005"
  ],
  "external_effects": "Local non-overwriting filesystem relocation, repository-local edits, validation, a local candidate commit, review, and local integration only; no push or other remote effect.",
  "limitations": [
    "Historical task, evidence, review, checkpoint, event, and provenance-lock bytes remain preserved except this authorized task lifecycle transition.",
    "Independent T1 reviewer /root/candidate_review_a approved the exact source commit bc9f2f29e277c08e6a38ede204cc56965dc316a2 using gpt-6-astra at max reasoning.",
    "The evidence-bearing closure head requires final read-only T1 review before any local integration.",
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
- [x] The approved source candidate is handed off for evidence-only closure; any local integration remains gated by final review of the evidence-bearing head.

## Closure and final-review boundary

Independent T1 review `REV-0004` approved exact source commit
`bc9f2f29e277c08e6a38ede204cc56965dc316a2` (tree `686bab41981b5e1a5455f9ad28f2599837b9b5eb`). Correction evidence `EVD-0005`
records the resolved findings and split validation.

This evidence-only successor closes `TASK-0003` without changing the reviewed
source candidate. The commit containing this review/task closure was not part
of that source review and therefore requires final read-only T1 review before
any serial local integration. No push or other remote effect is authorized.
