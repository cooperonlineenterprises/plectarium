# PLEC-SEC-001 — Establish foundational threat and isolation controls

- Status: `blocked`; dependencies: `PLEC-FND-001`, `PLEC-FND-002`
- Objective: implement security primitives needed before identities, jobs, or runners.
- Inputs: product security constitution and execution-profile schema.
- Outputs: threat registry, safe path/archive handling, redaction, resource limits, profile enforcement interfaces.
- Forbidden: provider credentials, production access, security certification claims.
- Acceptance: malicious-input and boundary fixtures fail closed with bounded diagnostics.
- Evidence: authority, secret, archive, path, and resource negative tests.
