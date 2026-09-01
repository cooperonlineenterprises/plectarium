# PLEC-CAT-001 — Implement exact catalog discovery and snapshots

- Status: `blocked`; dependency: `PLEC-FND-002`
- Objective: ingest static family-valid manifests and produce immutable catalog snapshots.
- Outputs: coordinate resolver, ingestion/quarantine, snapshot content identity, status overlays.
- Forbidden: manifest execution, name/tag identity, domain payload interpretation.
- Acceptance: family collisions are distinct; same-coordinate/different-bytes is quarantined; missing family ID is rejected.
- Evidence: catalog collision, substitution, stale, unknown-schema, and withdrawal fixtures.
