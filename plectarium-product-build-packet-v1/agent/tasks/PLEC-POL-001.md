# PLEC-POL-001 — Implement request plan binding and permission decisions

- Status: `blocked`; dependencies: `PLEC-FND-002`, `PLEC-IAM-001`
- Objective: bind an immutable capability plan to external approval, narrowing, expiry, revocation, and audit.
- Outputs: request/plan store, normalized view, decision service, scheduling revalidation.
- Forbidden: editing the capability plan, widening requested rights, treating result as approval.
- Acceptance: every material substitution invalidates approval; accepted rights are a subset.
- Evidence: TOCTOU, deny, expiry, revocation, and transport-equivalence tests.
