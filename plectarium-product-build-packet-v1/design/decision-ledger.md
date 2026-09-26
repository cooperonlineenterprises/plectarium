# Plectarium Decision Ledger

`design/decisions.yaml` is the machine-readable index. This ledger records
scope and consequences without duplicating normative specifications.

| ID | Status | Scope | Primary consequence |
|---|---|---|---|
| PLEC-001 | ESTABLISHED | Brand/ecosystem | Formal name is Plectarium; Octon relation is not dependency. |
| PLEC-002 | ESTABLISHED | Product boundary | Suite is not a specialist capability. |
| PLEC-003 | ESTABLISHED | Capability autonomy | Canonical CLI and independent releases remain mandatory. |
| PLEC-004 | ACCEPTED | Source ownership | Family contracts are locked externally, not copied. |
| PLEC-005 | ACCEPTED | Identity | Family, capability, exact version, digest, and contract all matter. |
| PLEC-006 | ACCEPTED | Deployment shape | Modules first; service extraction requires evidence. |
| PLEC-007 | ACCEPTED | Execution | CLI/OCI processes preserve engine boundaries. |
| PLEC-008 | ACCEPTED | Planning | Exact capability plan digest is the approval subject. |
| PLEC-009 | ESTABLISHED | Authority | Transport/result cannot grant broader action. |
| PLEC-010 | ACCEPTED | Completion | Job and capability completion are separate. |
| PLEC-011 | ACCEPTED | Distributed state | No exactly-once claim; fenced idempotent attempts. |
| PLEC-012 | ACCEPTED | Artifacts | Content and canonical records are immutable. |
| PLEC-013 | ACCEPTED | Verification | Crypto, trust, freshness, compatibility, and completion do not collapse. |
| PLEC-014 | ACCEPTED | Release | Plectarium owns exact suite support promises. |
| PLEC-015 | ACCEPTED | Modes | Local/private/air-gap mechanics retain semantic equivalence. |
| PLEC-016 | ACCEPTED | Credentials | Only short-lived opaque references cross the control boundary. |
| PLEC-017 | ACCEPTED | Tenancy | Isolation includes side channels and all supporting stores. |
| PLEC-018 | ESTABLISHED | Direct use | Suite hosting is optional. |
| PLEC-019 | DEFERRED | Shared code | Family extraction threshold remains unmet. |
| PLEC-020 | ESTABLISHED | AI/readiness | Neither AI nor structural setup is authority or product proof. |
| PLEC-021 | ACCEPTED | Internal contracts | Exact offline registry and versioned bounded encoding; no runtime or wire interoperability claim. |

Accepted decisions may change only through a successor ADR with migrations,
security/compatibility impact, affected schemas/tasks/tests, and rollback.
