---
{
  "schema_version": "harness.review.v1",
  "id": "REV-0016",
  "title": "Public HTTPS CI scope and preservation self-review",
  "task": "TASK-0008",
  "review_mode": "self_review",
  "status": "closed",
  "recorded_at": "2026-09-27"
}
---

The public-access diff removes only the mandatory family-key preflight, SSH input
and SSH-origin normalization from the workflow; its source-mismatch diagnostic
now describes the fixed public repository. Exact family commit and digest
verification remain mandatory, as do all test steps and the fail-closed aggregate.
Action/runtime/dependency pins, token permissions and non-persistence are retained.

EVD-0017 records public fetch and local checks. Current task/documentation now
reflect the operator's specific PR integration authority and require observed
post-merge validation. Prior failures remain untouched. This author self-review
is not independent review, a grant or hosted execution evidence. Fresh hosted
results and protected merge readbacks remain required.
