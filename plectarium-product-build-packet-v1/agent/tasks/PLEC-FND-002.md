# PLEC-FND-002 — Implement schema registry and canonical content identity

- Status: `blocked`; dependency: `PLEC-FND-001`
- Objective: implement strict JSON/YAML/schema handling, version registry, canonical encoding, digest, and migration fixtures.
- Inputs: `spec/schemas/`, family contract profile, change control.
- Forbidden: product meaning changes, implicit network schema resolution, family forks.
- Outputs: registry, validators, canonical digest API, positive/negative/migration vectors.
- Acceptance: duplicate keys, unknown breaking versions, bad references, and digest changes are detected deterministically.
- Evidence: test catalog entries `TEST-SCHEMA-*` and family conformance results.
