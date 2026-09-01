# PLEC-FND-001 — Validate product authority and immutable family source

- Status: `ready` (planning metadata only)
- Inputs: charter, invariants, ADR-001/002, family source lock, current family packet
- Objective: prove one owner per concept, exact family provenance, and no hidden implementation assumptions.
- Permitted surface: review reports, ADR proposals, source-lock resolution, validation fixtures.
- Forbidden: product code, family schema edits/copies, network fetches without authority.
- Outputs: authority crosswalk, resolved family lock, conflict/open-question record.
- Acceptance: exact commit/packet/contract digests verify; no contradiction is hidden.
- Tests/evidence: source-lock positive/negative fixtures and independent review.
- Handoff: unblocks `PLEC-FND-002`; creates no code-bearing authority.
