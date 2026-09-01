# Plectarium Evaluation Specification

## Layers

1. Packet integrity: files, schemas, fixtures, decisions, tasks, claims, manifest, checksums.
2. Contract conformance: family locks, coordinates, API/event/storage schemas, migrations.
3. Authority and tenancy: plan binding, permission subset, transport equivalence, cross-tenant isolation.
4. Distributed lifecycle: duplicates, fencing, cancellation, timeout, retry, orphan recovery.
5. Runner and artifact security: isolation, credentials, paths/archives, provenance, tamper.
6. Mode equivalence: direct/local, hosted, private, customer-controlled, air-gap.
7. Product experience: truthful states, accessibility, malicious content, operator usability.
8. Operations: load, SLOs, outages, migration, backup/restore, incident exercises.
9. Release: reproducibility, SBOM, provenance, exact BOM, current evidence.

## Claim discipline

Every run records exact subject revision, environment, dependency/capability
versions and digests, dataset/fixture identity, permissions, repetitions,
failures, raw artifacts, grader, limitations, freshness, and gate mapping.

Missing required evidence leaves a gate `unassessed`, `blocked`, `partial`, or
`failed`. It cannot pass. A test passing on one mode, tenant, provider, or
capability does not establish general support.

## Controls

When claiming suite or AI benefit, compare direct capability CLI/CI use without
Plectarium, the same workflow with Plectarium, and optional AI-assisted
projection. Measure outcome quality separately from process cost. Baseline
contamination, tiny samples, unbounded grader subjectivity, and hidden failures
invalidate broad claims.

## Adversarial emphasis

Include authority pressure, malicious manifests/results, tenant IDOR and side
channels, stale plan/lease/result substitution, secret leakage, archive/path
attacks, duplicate/reordered events, cancel races, prompt/log injection,
network/profile escape, resource exhaustion, and air-gap replay/rollback.
