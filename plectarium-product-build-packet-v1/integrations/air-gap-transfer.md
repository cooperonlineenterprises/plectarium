# Air-Gap Transfer Integration

Air-gap transfer uses `air-gap-bundle-manifest.schema.json`, exact contract/BOM
locks, content digests, nonce, validity window, and accepted signing policy.
Export and import are explicit authorized actions. No component contacts a
hosted endpoint as fallback.

Replay, rollback, stale support data, unknown family contract, plan mismatch,
tenant mismatch, tamper, or unverifiable result causes quarantine and a
truthful failure/limitation record.
