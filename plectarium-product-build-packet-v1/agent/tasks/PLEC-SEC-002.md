# PLEC-SEC-002 — Complete tenant runner artifact and credential adversarial testing

- Status: `blocked`; dependencies: privacy and operations tasks.
- Objective: test the implemented attack surface and close or explicitly accept findings.
- Coverage: IDOR, tenant side channels, runner impersonation/escape, TOCTOU, SSRF, archives, credentials, caches, queues, prompt/log injection, air-gap rollback, DoS.
- Acceptance: all critical/high findings resolved or release-blocking; limitations and test scope explicit.
- Evidence: independent security review and reproducible adversarial corpus.
