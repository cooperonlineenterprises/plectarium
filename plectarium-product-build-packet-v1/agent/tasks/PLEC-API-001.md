# PLEC-API-001 — Implement API event and suite CLI projections

- Status: `blocked`; dependencies: `PLEC-MCA-001`, `PLEC-MCA-002`
- Objective: expose one application semantic layer through versioned API, events, and suite CLI.
- Forbidden: transport privilege, secret-bearing messages, interface-specific completion.
- Acceptance: semantic equivalence, idempotency, pagination isolation, error truth, and backward compatibility pass.
- Evidence: golden cross-interface corpus plus auth/tenant/duplicate/error negative tests.
