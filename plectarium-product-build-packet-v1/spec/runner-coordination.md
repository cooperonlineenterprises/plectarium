# Runner Coordination and Execution Profiles

## Runner identity and registration

A runner has tenant/ownership scope, protocol version, supported platforms,
exact capability distributions, profile support, region/network attributes,
attestation state, and freshness. Registration advertises capability; it does
not grant a lease or permission.

## Pull and lease protocol

Private runners should use authenticated outbound polling or streaming where
practical. A lease binds tenant, job, attempt, plan digest, coordinate,
execution profile, permission decision, credential references, fencing token,
TTL, heartbeat interval, output limits, and upload targets.

Runners must reject mismatches, expired/revoked leases, unsupported profiles,
unknown coordinates, or broader permissions. Heartbeats carry status and
bounded metrics, not secrets or arbitrary log content.

## Required profiles

- `offline_read_only`: no project execution or network; bounded reads/outputs.
- `sandboxed_project_execution`: accepted project commands in a confined environment.
- `browser_execution`: declared origins, storage, downloads, network, and browser lifecycle.
- `private_network_observation`: explicit destinations/data categories and no ambient egress.
- `controlled_resource_read`: least-privileged infrastructure/database/production observation with writes unsupported.

Profiles are declarative contracts with platform-specific enforcement and
negative tests. No evidence profile supports infrastructure apply, database
write, deployment, publication, or arbitrary communication.

## Credentials

Leases carry opaque references. Runners redeem them just in time under exact
audience/scope/TTL and must not echo values. Revocation, failed redemption, and
unexpected credential use are visible terminal or limitation states.

## Recovery

Lost heartbeat causes lease expiry and reconciliation, not immediate
assumption of process death. Retry requires replay-safe declaration or renewed
approval. Orphan uploads remain quarantined until bound to a valid attempt.
