---
{"schema_version":"harness.review.v1","id":"REV-0010","title":"Focused reference-target review and second repair","task":"TASK-0005","review_mode":"independent","status":"closed","recorded_at":"2026-09-25"}
---

The independent reviewer verified FND2-R2 through R4 on contracts.py
98668787303a3a257c59ad02b3b141de587317416dd14aef8b605cc9b384059d,
but retained FND2-R1 as P1. A JSON pointer into default or examples could reach
a draft-07 schema outside ordinary subschema traversal and bypass the intended
2020-12 constraint. The 26-test candidate remained rejected.

The maintainer's second repair validates the resolved reference target as a
schema, then applies the same dialect, identity and reference restrictions to
it with cycle-safe memoization. Unreferenced annotation values remain literal
data. New tests cover both annotation-pointer bypasses, supported and malformed
reference targets, and a valid recursive schema. All 29 tests pass locally.

Final focused re-review of the new source is required before closure. No
repository changes or operating approval were made by the reviewer. Resource
exhaustion, concurrent filesystem replacement and platform qualification remain
outside the demonstrated scope.
