# Plectarium Open Questions

Each question may proceed only within the stated boundary. None is silently
answered by packet structure.

## OQ-001 — Package, binary, and protocol names

- Owner: Product and Interface Owners
- Evidence: collision, ecosystem, migration, and usability review
- May foundational implementation proceed? Yes, using explicit internal IDs.

## OQ-002 — Authentication and policy providers

- Owner: Identity and Security Owners
- Evidence: tenancy model, enterprise requirements, threat model, operational cost
- May foundational implementation proceed? Yes, behind provider-neutral ports.

## OQ-003 — Queue, transactional store, and object store technologies

- Owner: Architecture and Operations Owners
- Evidence: load model, failure tests, deployment modes, portability, cost
- May foundational implementation proceed? Yes, against logical contracts.

## OQ-004 — Signature and runner-attestation requirements by mode

- Owner: Security and Provenance Owners
- Evidence: threat model, trust domains, key lifecycle, offline verification
- May foundational implementation proceed? Yes; checksums and explicit
  `not_present`/`not_checked` states are mandatory.

## OQ-005 — Retention, residency, purge, and legal-hold defaults

- Owner: Product, Privacy, and Legal Owners
- Evidence: customer needs and qualified jurisdictional review
- May foundational implementation proceed? Yes, with no unsupported default.

## OQ-006 — Numeric SLO, RPO, and RTO targets

- Owner: Product and Operations Owners
- Evidence: measured workload, dependency budgets, recovery exercises, cost
- May foundational implementation proceed? Yes; instrumentation precedes claims.

## OQ-007 — Local and air-gapped key/bootstrap experience

- Owner: Distribution and Security Owners
- Evidence: usability, rollback, replay, recovery, and offline threat tests
- May foundational implementation proceed? Only after the transfer contract is accepted.

## OQ-008 — Initial supported suite BOM

- Owner: Release Owner and capability maintainers
- Evidence: implemented capability artifacts and conformance runs
- May foundational implementation proceed? Yes; an empty/unassessed support
  matrix is more truthful than hypothetical compatibility.
