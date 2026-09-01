# PLEC-JOB-001 — Implement truthful job attempts and reconciliation

- Status: `blocked`; dependencies: `PLEC-FND-002`, `PLEC-POL-001`
- Objective: implement the control lifecycle, immutable attempts, idempotency, fencing, cancellation, and reconciliation.
- Forbidden: exactly-once claims, mutable attempt history, cancellation-by-request-only.
- Acceptance: invalid transitions fail; stale attempts cannot terminalize; duplicate delivery is idempotent.
- Evidence: exhaustive transition table, crash/replay/orphan/timeout/finalization race tests.
