---
{
  "schema_version": "harness.review.v1",
  "id": "REV-0005",
  "title": "Plectarium migration review erratum",
  "task": "TASK-0003",
  "review_mode": "review_metadata_and_lifecycle_erratum",
  "status": "completed",
  "recorded_at": "2026-09-15",
  "evidence_refs": [
    "EVD-0006"
  ],
  "supersedes": "REV-0004",
  "reviewer_identity": "/root/candidate_review_a",
  "reviewer_role": "read_only_reviewer",
  "recorded_by": "/root/input_resolver",
  "transition_owner": "/root",
  "findings": [
    {
      "id": "CRA-07",
      "severity": "P3",
      "status": "resolved",
      "summary": "The repository review record mislabeled or mis-severitized the original source findings.",
      "resolution": "Added this erratum with the controlling CRA-01 through CRA-03 mapping; navigation is recorded only as an additional improvement."
    },
    {
      "id": "CRA-08",
      "severity": "P2",
      "status": "resolved",
      "summary": "Prior events attributed repository lifecycle recording and transitions to the read-only reviewer.",
      "resolution": "Preserved prior events and appended corrected attribution: T2 records evidence/review metadata and /root owns task transitions."
    },
    {
      "id": "CRA-09",
      "severity": "P2",
      "status": "resolved",
      "summary": "The migration task was prematurely completed and its explicit local-main integration criterion was removed.",
      "resolution": "Reopened through the legal lifecycle, restored the local-main integration criterion, and returned the task to review."
    }
  ],
  "limitations": [
    "This erratum corrects repository evidence labels and attribution; it is not a repeat T1 review of the corrected evidence head.",
    "The reviewed implementation source commit remains unchanged.",
    "Repeat T1 review and local-main integration remain pending."
  ]
}
---

## Erratum scope

This successor preserves `REV-0004` byte-for-byte and corrects only its
finding map, severities, authorship attribution, and lifecycle conclusion.
The controlling source-finding map is recorded in `EVD-0006`.

Reviewer `/root/candidate_review_a` performed read-only review only. T2 author and
recorder `/root/input_resolver` created the repository evidence records.
Primary integrator `/root` owns the appended task transitions. The approved
implementation source remains `bc9f2f29e277c08e6a38ede204cc56965dc316a2`.

## Disposition

- **CRA-07 (P3) — resolved:** Added this erratum with the controlling CRA-01 through CRA-03 mapping; navigation is recorded only as an additional improvement.
- **CRA-08 (P2) — resolved:** Preserved prior events and appended corrected attribution: T2 records evidence/review metadata and /root owns task transitions.
- **CRA-09 (P2) — resolved:** Reopened through the legal lifecycle, restored the local-main integration criterion, and returned the task to review.

The migration task is returned to `review`. This erratum does not approve its
own containing evidence head; repeat independent T1 review is required before
serial fast-forward integration into local `main`. No push is authorized.
