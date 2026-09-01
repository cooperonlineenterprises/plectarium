# Artifact, Result, Provenance, and Lineage

## Artifact records

Artifact identity is content-addressed SHA-256 plus media type and size. The
record also preserves tenant authorization, producer, subject, creation time,
schema, encryption/retention classification, and verification state. Location
is mutable routing metadata and never canonical identity.

## Result ingestion

Plectarium validates the exact pinned family result-reference and envelope
schemas, coordinate consistency, subject/scope, completion, payload references,
checksums, provenance, and declared limitations. Domain payloads remain opaque.

## Verification states

Checksum status: `verified`, `mismatch`, `missing`, `not_checked`.  
Signature status: `verified`, `invalid`, `untrusted_signer`, `unsupported`,
`not_present`, `not_checked`.  
Schema status: `valid`, `invalid`, `unknown_schema`, `not_checked`.

These states do not imply signer trust, compatibility, freshness, or action authority.

## Lineage

Every derived projection, imported result, comparison, bundle, or export uses
typed lineage edges to exact content IDs. Cycles, missing parents, cross-tenant
references, and incompatible transformations are rejected. Inference distance
and transformation identity remain explicit.

## Immutability and correction

Canonical bytes and records are never overwritten. Correction uses a new
content ID and successor/annotation relation. Withdrawal, quarantine, purge,
or trust changes are append-only status records and preserve historical audit
within authorized retention.

## Freshness

Plectarium preserves capability-defined freshness basis and material-change
triggers. It does not invent a universal TTL or upgrade stale evidence.
