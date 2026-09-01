# Claim-Proof Matrix

| Claim | Required proof | Gate |
|---|---|---|
| Packet is internally coherent | Read-only validator, negative fixtures, fresh manifest/checksums | GATE-PACKET |
| Plectarium owns no domain semantics | Opaque payload preservation, dependency/table review, direct CLI independence | GATE-BOUNDARY |
| Catalog identity is exact and multi-family | Collision, missing-family, substitution, stale/unknown schema fixtures | GATE-NAMESPACE |
| Execution cannot outrun approval | Plan-digest TOCTOU, subset, denial, expiry, revocation, transport tests | GATE-AUTHORITY |
| Tenants are isolated | IDOR and metadata/bytes/cache/queue/runner/index/audit side-channel tests | GATE-TENANCY |
| Job state is truthful | Transition model, duplicates, fencing, cancellation, retry, orphan/race tests | GATE-LIFECYCLE |
| Runner effects are bounded | Profile, resource, network, browser, credential, impersonation/escape tests | GATE-RUNNER |
| Results are immutable and attributable | Family conformance, tamper, archive, lineage, successor/purge tests | GATE-RESULT |
| Suite support is reproducible | Exact coordinate/BOM, constrained/incompatible/unknown/withdrawn tests | GATE-COMPAT |
| Deployment modes preserve semantics | Common conformance corpus plus no-network air-gap tests | GATE-MODES |
| Privacy/retention behavior is explicit | Minimization, redaction, hold, purge, residency-policy evidence | GATE-PRIVACY |
| Product recovers from failures | Queue/store/runner/key outage, migration, restore, reconciliation exercises | GATE-RESILIENCE |
| Experience presents truth accessibly | Workflow, malicious content, accessibility, partial/unknown language tests | GATE-UX |
| Service-level claims are measured | Workload model, load/capacity/error budget and recovery evidence | GATE-SLO |
| Distribution is verifiable | Reproducible build, SBOM, provenance, checksums/signatures | GATE-SUPPLY |
| Mature v1 is releasable | All required current gates plus independent limitations review | GATE-RELEASE |
