# Scheduling, Quotas, and Retention

## Scheduling

Scheduling selects only runners compatible with the exact capability
distribution, tenant, region/residency constraints, execution profile,
network/controlled-resource requirements, and approval. Fairness and priority
must not bypass security or tenant quotas.

## Quotas

Quota dimensions may include concurrent jobs, CPU, memory, elapsed time,
browser sessions, network egress, artifact bytes, retained bytes, queue depth,
and controlled-resource sessions. Evaluation is tenant-scoped and auditable.
Exhaustion produces explicit queued, denied, throttled, or partial outcomes;
work is not silently dropped.

## Retention

Retention policy distinguishes control metadata, job events, raw artifacts,
canonical results, derived projections, caches, audit, and export bundles.
Legal hold and qualified privacy requirements may prevent or require purge.

Canonical records remain immutable while present. A permitted purge removes
bytes through a recorded lifecycle and leaves only the minimum authorized
tombstone/audit evidence; it must not pretend the bytes remain verifiable.
Default durations, residency, and legal obligations remain unresolved pending
qualified owner decisions.
