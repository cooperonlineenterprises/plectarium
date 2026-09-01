# Family Contract Consumption Profile

Plectarium consumes the family packet identified by
`reference/family-source-lock.json`. The initial known family ID is
`standalone-capability-family`. The immutable family Git commit, packet
manifest, checksum ledger, and six consumed contract digests are resolved in
the lock and verified by the packet check against the published local family
checkout.

## Consumption rules

- Validate capability manifests, result envelopes, result references,
  permission sets, and completion documents against the exact pinned family
  schemas before suite ingestion.
- Store contract schema ID, source path, source SHA-256, packet version,
  manifest digest, and family commit with each ingestion profile.
- Wrap the family document with suite tenant, catalog, verification, retention,
  and access metadata; do not redefine its domain fields.
- Preserve unknown family extensions as data when the pinned schema permits
  them; otherwise report incompatible rather than coerce.
- Never infer missing `family_id` from repository, character name, or Plectarium membership.
- A newer family packet is a migration candidate, not an automatic update.

## Provisional contract handling

The family v0 contracts remain provisional. Plectarium must advertise the
exact consumed schema versions and maintain positive/negative conformance
fixtures. Stabilization or SDK extraction remains a family decision after the
required implementation evidence.

## Independent validation

The packet validator checks source-lock structure. A release pipeline must be
given the pinned family checkout or artifact explicitly and verify commit,
manifest, checksums, contract digests, and fixtures without implicit network
fetching.
