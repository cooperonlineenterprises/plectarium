# Air-Gap Export and Import Sequence

1. Resolve exact catalog/BOM and family contract locks.
2. Create request, capability plan, approval, profile, nonce, validity window,
   and export manifest with content digests.
3. Sign according to accepted offline policy; `not_present` remains explicit otherwise.
4. Transfer through an authorized medium; no network fallback occurs.
5. Offline verifier checks source, tenant, digest, freshness, replay/rollback,
   schemas, coordinate, and approval before execution.
6. Runner produces family result and transfer manifest with complete provenance.
7. Import verifies all bytes, source context, completion, signatures/checksums,
   lineage, and compatibility before cataloging.
8. Replay, stale BOM, unknown schema, or mismatch is quarantined, never coerced.
