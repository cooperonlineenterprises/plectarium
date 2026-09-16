---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0006",
  "title": "Plectarium review-label, attribution, and lifecycle correction",
  "task": "TASK-0003",
  "recorded_at": "2026-09-15",
  "subject_revision_or_fingerprint": "rejected evidence head dd08feac7d393d439b94eec27f88b1b9453ad4a4; approved implementation source bc9f2f29e277c08e6a38ede204cc56965dc316a2; corrected evidence head pending",
  "result": "corrected_pending_repeat_T1_review",
  "fresh_until": null,
  "supersedes": "EVD-0005"
}
---

## Accurate source-finding map

| Finding | Severity | Accurate label | Resolution |
|---|---|---|---|
| CRA-01 | P1 | default test dependency regression | Separate the dependency-bearing packet-pin suite from plain test_*.py discovery. |
| CRA-02 | P1 | unsafe Git environment/config/object effects | Sanitize Git subprocesses and suppress config, replacement, lazy-fetch, protocol, and metadata escape effects. |
| CRA-03 | P2 | lexical path validation before resolve | Validate raw lexical paths and lstat components before resolution and confinement. |

Navigation and dossier routing were useful additional improvements, but were not CRA-03.

## Authorship and transition correction

The independent reviewer `/root/candidate_review_a` performed read-only review only.
`/root/input_resolver` acted as the T2 author and repository evidence
recorder under delegation. Primary integrator `/root` owns task lifecycle
transitions. Earlier review/event bytes remain preserved; appended events
correct the attribution without rewriting history.

## Lifecycle correction

The evidence-only head `dd08feac7d393d439b94eec27f88b1b9453ad4a4` prematurely marked `TASK-0003`
completed and replaced its explicit local-main integration criterion. The task
is reopened through `reopened`, `in_progress`, `validating`, and `review`
events. Its explicit serial fast-forward integration criterion is restored.
Repeat T1 review of the corrected evidence head remains required.

## Validation and effects

The reviewed implementation source remains `bc9f2f29e277c08e6a38ede204cc56965dc316a2`; no
implementation code, validator, test, configuration, packet provenance, or
historical record changed in this correction. After the navigation/lifecycle
records freeze, the designated harness refresh and the plain 15-test suite,
separate 10-test pin suite, full packet/harness checks, JSON parsing, and diff
checks are rerun. No push or other external effect occurred.
