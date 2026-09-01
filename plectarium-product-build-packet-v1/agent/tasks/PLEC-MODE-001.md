# PLEC-MODE-001 — Implement local hosted private and air-gapped modes

- Status: `blocked`; dependencies: API, runner, and BOM tasks.
- Objective: realize mode-specific mechanics without semantic or authority divergence.
- Outputs: direct/local adapter, hosted/private runner flow, customer deployment contract, air-gap transfer verifier.
- Acceptance: common conformance corpus passes in every supported mode; air gap has no network fallback.
- Evidence: replay/rollback/tamper/stale-BOM, private connectivity, and direct-CLI independence tests.
