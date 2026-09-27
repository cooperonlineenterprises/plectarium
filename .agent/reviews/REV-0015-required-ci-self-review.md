---
{
  "schema_version": "harness.review.v1",
  "id": "REV-0015",
  "title": "Focused CI source and authority-boundary self-review",
  "task": "TASK-0008",
  "review_mode": "self_review",
  "status": "closed",
  "recorded_at": "2026-09-27"
}
---

## Review

Checked the workflow for pinned Actions/runtime/dependencies, read-only token,
no persisted checkout credentials, explicit family source and full commit,
mandatory real family verification, no path-based skip, and an always-evaluated
aggregate that rejects failure/cancellation/skip. Main/manual runs are not
cancelled by later PR runs. CI does not refresh integrity, merge or release.

The private-read key is confined to family checkout/preflight, unavailable to
the separate repository-check job, and removed by the checkout action before
packet validation. The dedicated key must have no write permission. Fork jobs
without that secret remain failed, not exempt. Existing controls remain intact.

EVD-0015 records local results. The concrete remaining issue is unconfigured
private family access; hosted success and ruleset read-back are not yet claimed.
This is author self-review, not independent review or a grant of authority.
