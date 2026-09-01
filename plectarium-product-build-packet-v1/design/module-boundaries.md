# Module Boundaries

| Module | Owns | Must not own |
|---|---|---|
| Identity and tenancy | principals, tenant scope, sessions, access checks | capability permissions or secret values |
| Catalog and BOM | source locks, exact coordinates, snapshots, compatibility, support BOM | capability domain schemas |
| Policy and approval | plan-bound decisions, constraints, expiry, revocation | hidden plan edits or downstream authority |
| Jobs and scheduling | state machine, attempts, quotas, idempotency, reconciliation | capability completion meaning |
| Runner coordination | registration, compatibility, fenced leases, profiles, heartbeat | ambient credentials or in-process engines |
| Artifact and result catalog | immutable bytes/metadata, verification, lineage, retention status | domain conclusions or mutable payload truth |
| Interfaces and experience | web/CLI/API/event projections | divergent semantics or privilege |
| Operations and release | audit, telemetry, migration, backup, SLO evidence, suite BOM release | family contracts or capability releases |

Cross-module calls use typed application contracts. Direct table ownership
violations and cyclic synchronous dependencies require an architecture review.
