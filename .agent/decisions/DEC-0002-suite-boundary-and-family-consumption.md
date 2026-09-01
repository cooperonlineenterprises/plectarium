---
{
  "schema_version": "harness.decision.v1",
  "id": "DEC-0002",
  "status": "accepted",
  "previous_status": "proposed",
  "title": "Own suite semantics and consume immutable family contracts",
  "created_at": "2026-08-31",
  "authority_source": "current operator invocation and family ADR-013/FAM-035/FAM-036",
  "supersedes": null,
  "successor": null
}
---

## Context

Plectarium needs a cohesive catalog and optional control plane while the family
and each capability retain their own authority and release lifecycle.

## Decision

Plectarium owns suite experience, tenant/policy/job/runner semantics, artifact
catalog, compatibility matrix, and suite BOM. It consumes the family packet by
full repository commit and packet digests, using the canonical
`family_id: standalone-capability-family`. It must not copy family schemas,
implement domain algorithms, import sibling source, or treat an Octon
relationship as a dependency or transfer of authority.

The immutable family commit and packet digests remain unresolved until the
family repository is published; this is an explicit prepublication gate.

## Consequences

- Benefits: exact source ownership and future multi-family catalog support.
- Costs: publication waits for an immutable family reference.
- Risks: a wrapper schema could drift into a semantic fork; conformance tests
  must validate family documents against the pinned external schemas.
- Undecided: final supported capability versions and signing policy by mode.

## Validation and rollback

- Evidence: family source lock validation and boundary/fixture gates.
- Reversal: a successor product and family decision is required.

## Resolution note — 2026-08-31

This nonsemantic current-state addendum does not change the accepted decision.
The family repository is now published and pinned at commit
`0b6c476682e416bd4fb770622c56758f5a380f09`; the packet manifest, checksum
ledger, and six consumed contract digests are resolved in
`plectarium-product-build-packet-v1/reference/family-source-lock.json` and
verified by `EVD-0002`. Future changes still require the successor path above.
