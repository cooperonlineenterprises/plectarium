---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0002",
  "status": "completed",
  "previous_status": "review",
  "title": "Publish and close the Plectarium repository foundation",
  "authority_basis": "current operator invocation of the Plectarium portfolio setup prompt",
  "owner": "primary portfolio agent",
  "created_at": "2026-08-31",
  "updated_at": "2026-08-31",
  "dependencies": ["TASK-0001"],
  "supersedes": null,
  "closure_evidence": ["EVD-0003"],
  "external_effects": "Initialized local main; created exact private cooperonlineenterprises/plectarium; pushed foundation commit 8842fe6543d0c63d56a0a34e336192e66f76cae1 normally and verified equality. This task's closure commit is the second and final authorized push; its equality is verified directly after publication because a commit cannot attest its own push.",
  "limitations": [
    "the closure commit cannot contain evidence of its own later push",
    "the two-push publication authority is consumed after direct final equality verification",
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

- [x] Exact staged content passes packet, harness, mutation, secret, transient, and boundary checks.
- [x] Exact private remote was empty/authorized and `main` was published normally.
- [x] Initial local/tracking/remote commit equality is recorded.
- [x] Narrow closure evidence is validated and pushed normally.
- [x] Final local/tracking/remote equality and clean worktree are verified
  directly after the closure commit.

## Risks and gates

- Side effects: local Git and exact authorized GitHub repository publication.
- Required approvals: only current operator authority; this task creates none.
- Sensitive data: prohibited; use existing credential mechanisms without inspection.
- Recovery: stop on collision, auth, permission, non-fast-forward, or partial effect.

## Evidence and closure

- Evidence: `EVD-0003` records exact creation, the first push, equality, and
  the closure commit's direct-verification boundary.
- Review: `REV-0003`; checkpoint: `CHK-0002`.
- External effects: exact private repository creation and two normal pushes only.
- Residual limitations: structural publication does not establish product readiness.
- Next action: use the final published Plectarium commit as a sequencing and
  suite-boundary provenance pin for Titra; it is not a runtime dependency.
