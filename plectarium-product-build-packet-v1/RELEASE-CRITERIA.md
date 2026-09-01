# Plectarium Mature-v1 Release Criteria

**Authority:** Normative release gate index  
**Current result:** not assessed; no implementation exists

A mature release requires fresh, subject-bound evidence for every required
gate in `evals/release-gates.yaml`.

## Product boundary

- No capability-domain algorithm, conclusion, mutable domain table, or sibling
  source import exists in Plectarium.
- Direct capability CLI/CI operation works without the suite.
- Plectarium and Octon remain related without runtime/authority coupling.

## Identity and authority

- Multi-family coordinates cannot collide and resolve exact versions/digests.
- Capability plans are immutable and approvals bind the exact plan digest.
- Permission narrowing, denial, expiry, and transport equivalence pass.
- Capability results never authorize deployment, publication, mutation, or
  another downstream action.

## Security and tenancy

- Tenant, principal, runner, artifact, cache, queue, audit, and deduplication
  isolation pass adversarial tests.
- Operation profiles enforce filesystem, process, browser, network, controlled
  resource, credential, and resource limits.
- Secret and sensitive-data handling passes review and negative tests.

## Jobs and runners

- Lifecycle transitions, idempotency, retries, cancellation, fencing,
  heartbeat, timeout, orphan reconciliation, and terminal races are truthful.
- Local, hosted, private, customer-controlled, and air-gapped modes preserve
  contract and authority semantics.

## Results and compatibility

- Artifacts/results are immutable, content-addressed, tenant-authorized, and
  provenance/lineage aware.
- Checksum, signature, signer trust, compatibility, freshness, completion, and
  limitations remain separate and visible.
- The suite BOM contains exact supported coordinates and unknown compatibility
  never appears supported.

## Operations and delivery

- Measured SLO, capacity, resilience, backup/restore, migration, audit,
  retention, privacy, accessibility, and incident exercises pass.
- Distributions are reproducible and carry SBOM, provenance, checksums, and
  signatures required by accepted policy.
- Open blockers, exceptions, owners, expiry, and reassessment triggers are explicit.

Packet validation alone satisfies none of these product release gates.
