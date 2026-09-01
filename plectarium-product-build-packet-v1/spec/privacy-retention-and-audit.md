# Privacy, Retention, Audit, and Observability

## Data minimization

Requests, plans, logs, telemetry, and indexes retain only data required for the
accepted operation and declared product purpose. Secret values are prohibited.
Capability artifacts keep their declared sensitivity and access restrictions.

## Retention and purge

Retention is typed by data class and tenant policy. Purge is authorized,
audited, resumable, and verifiable. Purged content cannot remain presented as
available or checksum-verifiable. Legal hold and qualified privacy decisions
are external authority inputs, not inferred by the product.

## Audit

Audit covers authentication, authorization, approvals, policy changes,
catalog/BOM changes, runner registration and leases, credential redemption
metadata, artifact/result lifecycle, exports/imports, administrative actions,
and release decisions. Events are append-only, access-controlled, and
tamper-evident according to accepted threat policy.

## Observability

Metrics, traces, and logs preserve tenant boundaries and correlation without
capturing secret or unnecessary payload data. Required signals include queue
age, scheduling latency, lease health, cancellation latency, retries,
verification failures, storage errors, quota pressure, and reconciliation.

## Incident readiness

Implementation must define detection, containment, evidence preservation,
tenant communication authority, credential revocation, runner quarantine,
recovery, and post-incident reassessment. The packet does not create an
incident-response SLA.
