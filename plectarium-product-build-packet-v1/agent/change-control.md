# Change Control

1. Identify the authoritative concept owner and affected decisions.
2. Classify the change as compatible, additive, transitional, breaking, or conflicting.
3. Use a successor ADR for accepted meaning changes.
4. Define schema/API/event/storage migrations and downgrade behavior.
5. Update specs, schemas, fixtures, tasks, gates, source map, manifest, and checksums atomically.
6. Revalidate family conformance against the immutable source lock.
7. Record security, tenancy, compatibility, operations, and rollback impact.
8. Never edit derived integrity independently.

Family contract changes are consumed through a new source lock and explicit
migration. Plectarium cannot silently patch or stabilize a family contract.
