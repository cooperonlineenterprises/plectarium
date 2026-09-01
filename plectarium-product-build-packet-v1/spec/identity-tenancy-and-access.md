# Identity, Tenancy, and Access

## Principal classes

Users, service accounts, runner identities, and import/export signers are
distinct principals. Authentication provider choice is adapter-specific and
must not alter authorization semantics.

## Tenant scope

Every request, plan, approval, job, attempt, runner binding, artifact, result,
catalog view, quota, retention rule, and audit event carries tenant scope.
Resource IDs are not authorization. Access checks occur at the authoritative
service boundary and again when issuing storage/runner capabilities.

Physical byte deduplication, if later chosen, cannot expose cross-tenant
existence, timing, size, checksum, or access metadata. Tenant authorization
records remain independent even for identical content.

## Approval rights

The right to submit, inspect, approve, administer runners, configure policy,
export data, or release a suite BOM are separate. Approvers cannot approve
outside their tenant/resource/permission scope. Self-approval policy is
explicit and auditable; no default is invented here.

## Local mode

Local mode may map the operating-system user to one explicit local tenant, but
must retain plan review and effect boundaries. It does not silently grant
hosted, production, network, or credential authority.

## Audit

Authentication and authorization decisions record principal, tenant, action,
resource, policy/approval sources, outcome, time, and correlation ID without
recording secret values.
