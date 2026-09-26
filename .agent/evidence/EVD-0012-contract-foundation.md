---
{"schema_version":"harness.evidence.v1","id":"EVD-0012","title":"Strict offline contract and content-identity validation","task":"TASK-0005","recorded_at":"2026-09-25","subject_revision_or_fingerprint":"PLEC-FND-002 working tree following aec8b9c; exact source inventory in designated integrity","result":"passed_after_independent_review_and_format_runtime_repair","fresh_until":null,"supersedes":null}
---

Using the project-local Python 3.14 contract interpreter and the exact versions
in requirements-contracts.txt, all 31 product/guard tests pass. Coverage includes
duplicate and escaped keys, malformed/nonfinite/Unicode input, byte/depth/node
limits, safe YAML behavior and rejection cases, exact canonical vectors, raw
byte digests, immutable receipts, version/ref/pin failures, explicit migrations,
schema diagnostic redaction, the structural packet fixture corpus, and retained
source-layout confinement. Permission-subset semantics remain explicitly outside
the shape validator and are tested as that distinction, not claimed implemented.

The checkout demonstration validates the pinned job schema, emits canonical
content digest sha256:d364181c8b9d725f815b293d83bbc82c5f9d25083169220939594b235416994b,
and refuses an unknown v99 document. The receipt's authority effect is none.

The packet/family check and all ten hostile pin tests pass. All fifteen harness
tests pass after adapting only three temporary-directory mkdir calls to an
existing source root; their original assertions remain intact. The final harness
and whitespace checks pass. Packet and harness integrity were refreshed only by
their designated writers. The family lock and all seventeen normative suite
schema files are unchanged from the S0 baseline.

Public PyPI development dependencies were installed into the isolated
project-local runtime under DEC-0004. No global/sibling environment, service,
capability execution, credential, release, publication or deployment changed. Tests write
disposable directories only. This is a locally tested internal library, not a
cross-platform qualification or completion of the remaining S1 semantic tasks.

Independent REV-0009 found four defects in the first 22-test candidate. They
were repaired with maintained schema-location traversal, dialect rejection,
boolean version handling and sanitized exception chains. Four new tests cover
the reproduced cases and formatted diagnostics, including migration failures.
A focused independent re-review is required on the corrected source.

REV-0010 confirmed R2-R4 but retained an R1 bypass through annotation pointers.
Resolved reference targets now receive full schema/profile checks with cycle
tracking; three additional tests cover both pointer paths, malformed targets
and valid recursion. The corrected 29-test source awaits final focused review.

REV-0011 confirmed R1-R4 and identified missing optional format support as R5.
Registry admission now rejects unavailable/unknown actual schema formats, and
exact maintained format dependencies supply date-time and URI checks in the
isolated runtime. Two tests cover malformed timestamps and missing checkers.
The earlier dependency-free observations describe superseded candidate checks,
not the final runtime. Final independent format re-review remains required.

Final disposition: independent REV-0012 verifies all five findings corrected
and all stated checks passing on the exact reviewed source. Earlier pending
review statements above describe candidate history. Core source, tests and
dependency pins remain unchanged during this administrative closure.
