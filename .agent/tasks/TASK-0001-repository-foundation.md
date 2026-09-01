---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0001",
  "status": "completed",
  "previous_status": "review",
  "title": "Establish the local Plectarium repository foundation",
  "authority_basis": "current operator invocation of the Plectarium portfolio setup prompt",
  "owner": "primary portfolio agent",
  "created_at": "2026-08-31",
  "updated_at": "2026-08-31",
  "dependencies": [],
  "supersedes": null,
  "closure_evidence": ["EVD-0001", "EVD-0002"],
  "external_effects": "none; local plectarium files and designated integrity writers only",
  "limitations": [
    "Git initialization and GitHub publication transferred to TASK-0002",
    "product implementation and readiness outside scope"
  ]
}
---

## Scope

In scope:

- adopt project-specific high-assurance governance and dossier content;
- create the setup-only product constitution, executable specification, build
  tasks, schemas, fixtures, evaluator, validator, manifest, and checksums;
- resolve and verify the immutable family source lock;
- refresh and validate packet and live root integrity.

Out of scope:

- product code, dependencies, services, deployment, or production resources;
- family/capability/Octon changes;
- Git initialization, commits, remote creation, pushes, and equality verification,
  which are owned by successor `TASK-0002`.

## Acceptance criteria

- [x] One canonical product packet owns suite semantics without family forks.
- [x] Packet check and negative fixtures pass after designated packet refresh.
- [x] Harness mutation tests pass in the declared Python runtime.
- [x] Immutable family commit, manifest digest, checksums digest, and consumed contract digests are pinned and checked.
- [x] Root generated integrity is refreshed and read-only harness check passes.
- [x] Local foundation review records limitations and no external effects.

## Risks and gates

- Side effects: local files and designated integrity refresh only.
- Required approvals: successor task/current prompt for exact publication; separate authority
  for later product implementation.
- Sensitive data: prohibited.
- Rollback: preserve local work and record partial effects; never force-push.

## Evidence and closure

- Evidence: `EVD-0001` and `EVD-0002` record local validation and family equality.
- Review: `REV-0001` closes the local-foundation review.
- External effects: none.
- Residual limitations: packet validation does not establish product readiness.
- Next action: execute `TASK-0002` for initial and closure publication.
