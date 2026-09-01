# Packet Integrity Report

Generated only by `scripts/validate-packet.py --refresh-derived`.

- Packet: `plectarium-product-build-packet-v1`
- Version: `1.0.0`
- Algorithm: SHA-256
- Manifest excludes itself and the checksum sidecar.
- Checksum sidecar includes the manifest and excludes itself.
- Integrity establishes byte consistency, not product readiness.
- The family publication pin is resolved; validate its exact commit and file digests with `--family-root` before relying on it.
