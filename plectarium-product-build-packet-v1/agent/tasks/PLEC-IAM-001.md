# PLEC-IAM-001 — Implement tenant and principal authorization contracts

- Status: `blocked`; dependencies: `PLEC-FND-002`, `PLEC-SEC-001`
- Objective: provide provider-neutral user/service/runner identity and tenant-scoped resource authorization.
- Outputs: authorization service port, resource checks, audit events, isolation corpus.
- Forbidden: using IDs as authorization, secret storage, one transport bypass.
- Acceptance: cross-tenant metadata/byte/cache/queue/runner access and existence probes fail.
- Evidence: IDOR, confused-deputy, self-approval, and session/revocation tests.
