---
{"schema_version":"harness.task.v1","id":"TASK-0004","title":"Close PLEC-FND-001 authority and immutable family validation","status":"completed","previous_status":"review","authority_basis":"Current operator instruction to continue the recommended work, including Plectarium S0 validation and foundational contracts, with coordinated ownership and local checkpoints.","owner":"plectarium suite maintainer in family coordination chat","created_at":"2026-09-25","updated_at":"2026-09-25","dependencies":["TASK-0003"],"supersedes":null,"closure_evidence":["EVD-0011"],"external_effects":"Local source, validation and checkpoint only; no network, release, service or remote effect.","limitations":["Family contracts remain provisional","This task creates no product code","Independent review completed under REV-0008"]}
---

## Scope and authority

Complete packet PLEC-FND-001 before its code-bearing successor. Review Charter,
invariants, accepted ownership decisions, immutable family lock, open questions,
validation fixtures and implementation-stage assumptions. Produce an authority
crosswalk, exact local source-lock evidence and an independent review. Preserve
family and capability source; no packet meaning or source pin changes here.

The current user request authorizes S0/S1 continuation in this repository, local
tests and checkpoint commits. Verity and Titra have separate owners; Noerovia,
Eupora and Gnomia are coordinated in their existing chats. No sibling source is
imported or edited by this task. A result cannot authorize execution.

## Acceptance and validation

- One owner per concept and explicit non-transferring boundaries.
- Family commit, packet manifest/ledger and all six contract hashes verified.
- Positive and hostile source-lock tests and existing harness tests pass.
- All material implementation assumptions and open questions are visible.
- Independent read-only review closes before PLEC-FND-002 begins.

The existing explicit local interpreter provides the pinned packet dependencies;
no installation is necessary. Product roots remain absent until this gate closes.

## Closure

PLEC-FND-001 acceptance is met under EVD-0011 and independent REV-0008.
The four reviewed source hashes matched before this administrative closure.
PLEC-FND-002 is next under the current continuation request, after its layout
and encoding decision; no other packet task is marked completed.
