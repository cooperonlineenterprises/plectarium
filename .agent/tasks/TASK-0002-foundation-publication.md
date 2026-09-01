---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0002",
  "status": "in_progress",
  "previous_status": "ready",
  "title": "Publish and close the Plectarium repository foundation",
  "authority_basis": "current operator invocation of the Plectarium portfolio setup prompt",
  "owner": "primary portfolio agent",
  "created_at": "2026-08-31",
  "updated_at": "2026-08-31",
  "dependencies": ["TASK-0001"],
  "supersedes": null,
  "closure_evidence": [],
  "external_effects": "Local Git initialized on main after exact remote absence and authentication checks; GitHub creation and pushes remain pending.",
  "limitations": [
    "task status is non-authorizing and remains subordinate to current operator authority",
    "maximum one initial foundation push and one narrow closure-evidence push",
    "product implementation and later pushes remain unauthorized"
  ]
}
---

## Scope

In scope:

- inspect the exact local foundation and Git boundary;
- initialize local Git on `main`, stage reviewed foundation content, and create
  one intent-focused foundation commit;
- recheck and create/adopt only the exact private authorized GitHub repository;
- push normally, record equality evidence, create one narrow closure-evidence
  commit, push normally, and verify final equality/cleanliness.

Out of scope:

- product implementation, dependencies, tags, releases, packages, deployment,
  force push, alternate repository names, or unrelated GitHub settings.

## Acceptance criteria

- [ ] Exact staged content passes packet, harness, mutation, secret, transient, and boundary checks.
- [ ] Exact private remote is empty/authorized and `main` is published normally.
- [ ] Initial local/tracking/remote commit equality is recorded.
- [ ] Narrow closure evidence is validated and pushed normally.
- [ ] Final local/tracking/remote equality and clean worktree are recorded.

## Risks and gates

- Side effects: local Git and exact authorized GitHub repository publication.
- Required approvals: only current operator authority; this task creates none.
- Sensitive data: prohibited; use existing credential mechanisms without inspection.
- Recovery: stop on collision, auth, permission, non-fast-forward, or partial effect.

## Evidence and closure

- Evidence: to be recorded after each exact external transition.
- Review: staged inventory and final closure candidate require review.
- External effects: none yet.
- Residual limitations: structural publication does not establish product readiness.
- Next action: inspect exact staging and remote collision state.
