# Architecture or Outcome Model

## Context

Plectarium is a suite product and optional control plane in the Octon ecosystem.
It consumes independent capabilities through discovery, plan, permission,
execution, completion, and durable-result contracts.

## Actors and stakeholders

Users, tenant administrators, approvers, capability maintainers, runner
operators, auditors, and external harnesses. Exact ownership assignments are
not yet made.

## Components, capabilities, or workstreams

- Identity and tenancy
- Capability catalog, compatibility, and suite BOM
- Policy and permission approval
- Job scheduling and runner coordination
- Immutable artifacts, results, provenance, and lineage
- Web/application, API, event, and suite-CLI projections
- Audit, privacy, operations, migration, evaluation, and release

## Boundaries and invariants

- Capability engines remain independent and authoritative for their domains.
- The suite never treats evidence as downstream-action authority.
- Family and capability coordinates include exact versions and digests.
- Transport and runner mode cannot expand permission.
- Product state, queue delivery, completion, and cancellation are truthful.
- Tenant isolation includes metadata, artifacts, runners, caches, and audit.

## Relationships and flows

Catalog ingestion binds immutable family and capability identities. A
capability-authored plan is reviewed and approved by exact digest before a
fenced runner lease may execute it. Results enter an immutable artifact catalog
only after contract, identity, checksum, and provenance validation.

## Open design decisions

Provider selections, numeric SLOs, signing policy by mode, retention defaults,
package/CLI identifiers, and runner attestation remain in the RAIDQ register.
