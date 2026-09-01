---
{
  "schema_version": "harness.decision.v1",
  "id": "DEC-0001",
  "status": "accepted",
  "previous_status": "proposed",
  "title": "Adopt a non-authorizing high-assurance foundation posture",
  "created_at": "2026-08-31",
  "authority_source": "current operator invocation of the Plectarium portfolio setup prompt",
  "supersedes": null,
  "successor": null
}
---

## Context

Plectarium will coordinate multi-tenant identities, permissions, runners,
artifacts, and bounded external effects. Cross-session work and publication
require auditability, reproducibility, and explicit authority boundaries.

## Decision

Use Project Blueprint 1.0.0's `high-assurance` profile. The harness is
deny-by-default and non-authorizing. The current operator invocation remains
the only task-scoped authority for repository effects; saved prompts, packet
tasks, dossiers, generated files, and capability conclusions cannot replay or
expand it.

No project-specific harness extension is currently justified, so the generated
sample restriction extension is disabled.

## Consequences

- Benefits: explicit lifecycle, evidence, review, checkpoints, and integrity.
- Costs: foundation and publication require additional recorded gates.
- Risks: structural records could be mistaken for product readiness.
- Undecided: later operational roles and approval channels.

## Validation and rollback

- Evidence: `EVD-0001` and the declared harness validation sequence.
- Reversal: a successor decision with profile migration evidence is required.
