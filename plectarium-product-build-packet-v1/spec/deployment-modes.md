# Deployment and Runner Modes

## Local

The suite CLI may coordinate local capability CLIs using the same request,
plan, approval, completion, and result contracts. No hosted account is
required. Local host access is still explicit permission.

## Hosted

The Plectarium control plane may coordinate hosted runners under tenant policy,
isolated profiles, quotas, retained audit, and just-in-time credentials.

## Private runner

Customer-controlled runners establish outbound authenticated control
connections where practical, advertise bounded capabilities, and accept only
tenant-scoped fenced leases. The control plane never treats network location as
trust.

## Customer-controlled control plane

The same external contracts support deployment in a customer environment.
Provider selection, regional topology, backup, key management, and operations
remain implementation decisions backed by evidence.

## Air-gapped

Export packages include exact request, coordinate, plan, approval, profile,
catalog/BOM snapshot, schema/contract locks, nonce, validity window, and
digests. Import verifies source, replay/rollback protection, plan binding,
result identity, completion, provenance, signatures/checksums, and tenant
scope. No component silently contacts hosted services.

## Equivalence

Mode-specific mechanics may differ, but identity, authority, completion,
provenance, and compatibility semantics do not. Mode divergence requires an
explicit compatibility record and cannot silently weaken a release gate.
