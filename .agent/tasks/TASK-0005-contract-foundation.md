---
{"schema_version":"harness.task.v1","id":"TASK-0005","title":"Implement PLEC-FND-002 strict offline contracts and identity","status":"completed","previous_status":"review","authority_basis":"Current operator continuation of recommended suite foundational contracts after completed TASK-0004 and independent REV-0008.","owner":"plectarium suite maintainer","created_at":"2026-09-25","updated_at":"2026-09-25","dependencies":["TASK-0004","DEC-0003","DEC-0004"],"supersedes":null,"closure_evidence":["EVD-0012"],"external_effects":"Local implementation/tests/checkpoint and pinned public development dependency downloads into project-local isolation; no remote repository or production effect.","limitations":["Internal contract API only","No runtime approval, provider, service or execution profile","No stable public package or RFC canonicalization claim"]}
---

Implement strict bounded JSON/YAML parsing, exact offline schema/version
registration, reference checking, canonical content encoding/digest, explicit
migration hooks and immutable receipts. Use existing normative suite schemas
without copying family schemas or interpreting capability payloads.

Acceptance: duplicate/ambiguous keys, unknown versions, unresolved references,
unsafe schema paths, malformed/nonfinite values and changed digests are rejected
deterministically. Positive/adverse/round-trip/migration vectors pass, including
the packet's structural fixture corpus. Schema success must never imply semantic
authorization. Adopt source layout and encoding through DEC-0003/PLEC-021.

Run product tests, packet/family-pin checks, ten pin tests and fifteen harness
tests. Obtain read-only review, disclose all semantic tasks not implemented,
refresh only designated integrity writers and checkpoint locally. No push.

## Closure

PLEC-FND-002 closes under EVD-0012 and independent REV-0012 after all five
findings were corrected. Reviewed source hashes matched before this metadata
closure. The remaining S1 semantic tasks are not claimed implemented.
PLEC-SEC-001 and PLEC-CAT-001 are the next dependency-ready packet tasks.
Final source refresh/check and exact staging precede the local checkpoint.
