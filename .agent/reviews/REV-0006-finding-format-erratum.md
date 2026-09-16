---
{
  "schema_version": "harness.review.v1",
  "id": "REV-0006",
  "title": "Plectarium finding-map and formatting erratum",
  "task": "TASK-0003",
  "review_mode": "review_record_metadata_and_format_erratum",
  "status": "completed",
  "recorded_at": "2026-09-15",
  "evidence_refs": [
    "EVD-0007"
  ],
  "supersedes": "REV-0005",
  "reviewer_identity": "/root/candidate_review_a",
  "reviewer_role": "read_only_reviewer",
  "recorded_by": "/root/input_resolver",
  "transition_owner": "/root",
  "findings": [
    {
      "id": "CRA-07",
      "severity": "P2",
      "status": "preserved_correctly",
      "summary": "Review-record meaning and actor mapping must distinguish reviewer, recorder, and transition owner."
    },
    {
      "id": "CRA-11",
      "severity": "P3",
      "status": "resolved",
      "summary": "The prior erratum assigned inaccurate metadata labels/severities.",
      "resolution": "Added this successor with the controlling CRA mapping and preserved CRA-07 as P2."
    },
    {
      "id": "CRA-12",
      "severity": "P3",
      "status": "resolved",
      "summary": "Current task criteria and routing banners contained literal backslash-n bytes.",
      "resolution": "Converted only those literal escapes to real Markdown line breaks and added a zero-hit scan."
    }
  ],
  "limitations": [
    "This successor corrects metadata and current-file formatting; it is not repeat T1 approval of its own evidence head.",
    "The migration task remains at review and local-main integration remains pending.",
    "Product, security, release, and production readiness remain unassessed."
  ]
}
---

## Erratum

This successor preserves `REV-0005` and `EVD-0006` byte-for-byte.
The accurate controlling finding map is recorded in `EVD-0007`.

CRA-07 retains its original P2 review-record meaning and actor-mapping scope. CRA-11 and CRA-12 are the new P3 metadata and literal-format corrections.

The task remains in `review` with repeat independent T1 review and explicit
serial fast-forward integration still pending. No push is authorized.
