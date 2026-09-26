---
{"schema_version":"harness.decision.v1","id":"DEC-0004","status":"accepted","previous_status":"proposed","title":"Require declared format support in the isolated contract runtime","created_at":"2026-09-25","authority_source":"Current local contract implementation and validation request; independent FND2-R5 and direct reproduction require the missing format dependency to satisfy the accepted schema contract.","supersedes":null,"successor":null}
---

The original packet interpreter silently skipped optional date-time/URI
format checks. A malformed timestamp received a structural receipt, so that
environment cannot support the intended strict contract claim.

Keep the language, internal layout, canonical encoding and schema bytes from
DEC-0003. Add exact maintained RFC 3339/RFC 3986 format-validator dependencies
and their pinned transitive dependency to requirements-contracts.txt. Install
the exact runtime only under this project's non-Git local/contract-runtime;
no global or sibling environment is changed. Public PyPI reads are a bounded
development effect, not provider access or release publication.

Registry admission must reject every actual schema format whose checker is
unavailable. It must never silently downgrade assertions because an optional
dependency is missing. Unknown formats require a reviewed supported runtime;
there is no automatic installation or fetch inside the library.

This strengthens implementation fidelity without changing the seventeen
normative schema bytes or any family contract. Validate both malformed values
and simulated missing-checker environments. Record installation and runtime
versions separately from product or platform qualification.
