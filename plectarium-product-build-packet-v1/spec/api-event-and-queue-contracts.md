# API, Event, and Queue Contracts

## API

All mutating API operations require tenant-scoped authorization, correlation
ID, canonical request digest, and idempotency key where replay is possible.
Errors use stable problem codes and never hide denied, stale, partial, or
incompatible states.

Pagination, filtering, and search operate on declared metadata and cannot
leak cross-tenant existence. Artifact download uses short-lived scoped access
and rechecks authorization.

## Events

Events are immutable facts with schema version, event ID, tenant, aggregate ID,
aggregate revision, time, actor/source, correlation/causation IDs, and payload
digest. Consumers tolerate duplicates, reject impossible regressions, and
reconcile from canonical state.

## Queue

Queue messages are delivery envelopes, not authority or truth. They contain no
secret values and reference immutable request/plan/profile records. Delivery is
at-least-once. Poison messages are quarantined with bounded diagnostics.

## Transactional publication

Canonical state changes and outgoing event intent require an atomic
transaction/outbox-equivalent boundary. The exact technology is deferred.
Consumers use idempotent application and monotonic aggregate revisions.

## Interface equivalence

Web, suite CLI, API, queue workers, and future adapters invoke the same
application services. Transport-specific metadata cannot widen permission,
scope, or result claims.
