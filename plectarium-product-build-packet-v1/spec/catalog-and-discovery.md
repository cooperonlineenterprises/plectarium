# Catalog, Discovery, Compatibility, and Suite BOM

## Identity

The canonical coordinate is:

```text
(family_id, capability_id, capability_version, artifact_digest)
```

Manifest schema ID/digest, protocol version, distribution variant, and runner
requirements are attached. Character identity is display metadata. Tags,
ranges, repository names, and friendly names are never canonical resolved
identity.

## Ingestion

Static discovery must not execute product code. Ingestion validates the pinned
family contract, coordinate consistency, duplicate identity, schema IDs,
artifact digest, provenance, signature state, limits, and supported media
types. Same coordinate with different bytes is quarantined as substitution or
republication, never overwritten.

Catalog snapshots are immutable and content-addressed. Withdrawal or support
changes create successor metadata without erasing historical jobs/results.

## Compatibility

Compatibility dimensions include family contract, capability manifest,
request/plan/result schemas, runner protocol, execution profile, distribution
platform, policy constraints, and Plectarium projection support.

Allowed status:

```text
supported
supported_with_constraints
incompatible
unknown
withdrawn
```

Every assertion identifies exact subjects, evidence, effective interval,
constraints, owner, and reassessment trigger. Unlisted is `unknown`.

## Suite BOM

Plectarium owns the supported suite BOM. Each entry resolves one exact
coordinate and required contract/profile digests. Version ranges may select a
candidate, but a released BOM contains only exact versions and digests.

The family repository does not own this support promise, and a workspace lock
does not substitute for it.
