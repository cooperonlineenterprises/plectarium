# PLEC-RUN-001 — Implement runner lease and execution profile contracts

- Status: `blocked`; dependencies: IAM, catalog, policy, jobs, and security foundation tasks.
- Objective: coordinate exact capability distributions through fenced expiring leases and enforced profiles.
- Outputs: registration, pull/lease/heartbeat/cancel protocol, profile adapters, opaque credential redemption.
- Forbidden: ambient host rights, secret persistence, in-process capability engines.
- Acceptance: expired/replayed/mismatched leases and profile escapes fail closed.
- Evidence: network/write/browser/resource/credential/heartbeat/runner-impersonation tests.
