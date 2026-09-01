# Plectarium Product Invariants

Conflicts require an explicit successor ADR; implementation convenience cannot
silently weaken these rules.

1. **Suite, not specialist.** Plectarium never owns capability-domain algorithms or conclusions.
2. **Independent engines.** Every capability remains usable through its canonical CLI without Plectarium, Octon, MCP, AI, or hosting.
3. **Exact coordinates.** Catalog and result identity include family ID, capability ID, exact version, schema identity, and artifact digest.
4. **Pinned external authority.** Family contracts are consumed by immutable source lock, never copied as a mutable Plectarium fork.
5. **Opaque domain payloads.** The suite validates and preserves declared contracts without reinterpreting domain meaning.
6. **Plan-bound execution.** Approval binds the exact immutable capability-authored plan digest, subject, scope, profile, and permission subset.
7. **No transport privilege.** Web, CLI, API, CI, queue, OCI, MCP, runner, or air-gap transport cannot expand authority.
8. **No evidence authority.** Results may inform decisions but never authorize mutation, publication, deployment, communication, or controlled-resource writes.
9. **Tenant isolation.** Metadata, artifacts, caches, queues, runners, credentials, indexes, and audit are tenant-authorized without cross-tenant existence disclosure.
10. **Truthful distributed state.** At-least-once delivery, retries, cancellation, timeouts, partial uploads, and reconciliation remain visible.
11. **Fenced attempts.** Stale or duplicate attempts cannot overwrite a newer accepted terminal result.
12. **Immutable results.** Canonical bytes and records are content-addressed; correction uses successor metadata, not silent mutation.
13. **Preserved provenance.** Completion, scope, freshness, checksums, signatures, signer trust, lineage, limitations, and compatibility remain distinguishable.
14. **Just-in-time credentials.** Secret values never enter durable plans, queues, logs, metadata, or result artifacts.
15. **Operation-specific isolation.** Profiles constrain effects by exact operation; runner location is not a security profile.
16. **Unknown is not supported.** Missing or stale compatibility evidence never becomes a support claim.
17. **Direct operation survives.** Suite BOM and hosted features do not make hosted execution mandatory.
18. **Modular first.** Deployable extraction requires evidence; capability count alone does not create microservices.
19. **AI remains optional.** AI is neither the semantic engine, authority, credential path, nor hidden executor.
20. **Readiness requires evidence.** Documentation and structural checks cannot satisfy implementation release gates.
