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
    "EVD-0006"
  ],
  "external_effects": "Local non-overwriting filesystem relocation, repository-local edits, validation, a local candidate commit, review, and local integration only; no push or other remote effect.",
  "limitations": [
    "Rejected evidence-head commits, prior reviews, prior events, evidence, checkpoints, and provenance locks remain preserved as history.",
    "Source commit bc9f2f29e277c08e6a38ede204cc56965dc316a2 retains its prior read-only review; corrected evidence and lifecycle attribution await repeat T1 review.",
    "Serial fast-forward integration into local main remains explicitly pending.",
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
- [ ] The corrected evidence-bearing head receives repeat independent T1 review.\n- [ ] The approved candidate is integrated serially into local `main`.

## Erratum and active review boundary

The implementation source commit `bc9f2f29e277c08e6a38ede204cc56965dc316a2` retains its prior read-only
review. Erratum evidence `EVD-0006` and review successor `REV-0005`
correct the finding labels, severities, authorship, and lifecycle attribution
without rewriting `EVD-0005`, `REV-0004`, or prior events.

The primary integrator reopened this task through `reopened`,
`in_progress`, and `validating`, then returned it to `review`. Repeat T1
review of the corrected evidence-bearing head is required before serial
fast-forward integration into local `main`. No push is authorized.
