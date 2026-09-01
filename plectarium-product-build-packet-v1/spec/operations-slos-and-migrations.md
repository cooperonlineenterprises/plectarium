# Operations, SLOs, Migrations, and Recovery

## Operational requirements

Every deployment mode needs health, capacity, queue, runner, storage,
verification, audit, backup, restore, and migration runbooks. Operators must be
able to stop scheduling without losing canonical state and reconcile orphaned
work after dependency recovery.

## Service levels

Measure before promising. Candidate indicators include API availability,
catalog freshness, plan latency, approval-to-queue latency, queue age,
lease-start latency, cancellation acknowledgement, artifact durability,
verification latency, recovery time, and audit completeness.

Numeric targets, error budgets, RPO, and RTO remain open until an owner accepts
them using workload and recovery evidence. Air-gapped workflows require batch
timeliness criteria rather than hosted availability claims.

## Schema and state evolution

- Every persisted/API/event schema has an explicit version.
- Readers reject unknown breaking versions and preserve unknown compatible data.
- Migrations are forward/reverse or explicitly irreversible with backup and
  recovery gates.
- Dual-read/write transitions have bounded duration and reconciliation.
- Family contract upgrades are explicit compatibility migrations, never
  automatic branch tracking.
- A suite BOM remains reproducible after migration.

## Recovery exercises

Test queue loss, control-store failover, partial object upload, corrupted
indexes, stale restored leases, key/credential outage, runner partition,
family-schema rollback, and air-gap replay. Recovery evidence is versioned and
expires on material architecture change.
