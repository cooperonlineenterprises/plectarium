# Plectarium Architecture

**Status:** Accepted logical architecture; deployable and technology choices remain gated

## Modular control plane

Begin with one modular product boundary rather than a service per capability.

```text
Web application / suite CLI / API
                 |
        Application services
                 |
 +---------------+----------------+
 | identity and tenancy            |
 | catalog, compatibility, BOM     |
 | policy and permission approval  |
 | jobs, scheduling, quotas        |
 | runner coordination             |
 | artifacts, results, provenance  |
 | audit, operations, retention    |
 +---------------+----------------+
                 |
  runner leases and immutable contracts
                 |
 local / hosted / private / air-gapped runners
                 |
 independently versioned capability CLIs or OCI jobs
```

Module boundaries are semantic and testable even when initially deployed
together. A module becomes an independent deployable only when security,
scaling, failure isolation, ownership, or operational evidence justifies it.

## Logical data ownership

- Transactional control state owns tenant-scoped identities, policy decisions,
  jobs, attempts, leases, quotas, and metadata.
- Immutable content-addressed storage owns manifests, plans, artifacts, and
  result bytes.
- A durable queue provides at-least-once delivery; it is not canonical state.
- Append-only job and audit events support reconciliation and investigation.
- Credential brokers retain secret values; Plectarium stores opaque,
  short-lived references only.

Plectarium creates no capability-domain tables. Search indexes and UI
projections may index declared metadata, never silently reinterpret payloads.

## Execution flow

1. Ingest a capability manifest only after family-contract, identity, digest,
   and compatibility validation.
2. Resolve an exact capability coordinate and runner-compatible distribution.
3. Ask the capability to produce an inspectable plan for the exact request.
4. Store the plan bytes immutably and bind review to their canonical digest.
5. Record an external policy/human decision; approval may narrow but not widen
   requested permissions.
6. Schedule an immutable attempt using one operation-specific execution profile.
7. Issue a fenced, expiring runner lease and just-in-time credential references.
8. Preserve heartbeat, cancellation, retry, and recovery events truthfully.
9. Validate result contract, identity, completion, bytes, checksums,
   signatures, provenance, and lineage before cataloging.
10. Render projections without changing canonical capability semantics.

## Capability boundary

Capabilities normally execute out of process or as version-pinned OCI jobs.
Direct CLI and CI use remain first-class and do not require Plectarium.
Cross-capability consumption uses immutable durable-result references; the
suite never links capability engines in process.

## Storage and delivery semantics

Exactly-once distributed execution is not claimed. Queue delivery is
at-least-once. Tenant-scoped idempotency keys, immutable attempts, monotonic
fencing tokens, compare-and-set terminalization, and content identity provide
effectively-once control-state outcomes without hiding duplicate work.

## Future topology

Later code-bearing work may create `apps/web`, `apps/control-plane`,
`apps/suite-cli`, product components, interfaces, execution profiles,
compatibility, distributions, deployment, and tests. These paths are not
materialized by the foundation task.
