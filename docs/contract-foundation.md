# Internal contract foundation

PLEC-FND-002 provides a checkout-local Python library under
`src/plectarium_contracts`. The public suite interface remains a later task.
Use Python 3.11+ with the exact dependencies in `requirements-contracts.txt`;
the final development runtime is isolated under the project-owned non-Git
`local/contract-runtime/venv`. The original packet interpreter lacked optional
format support and is refused when a required checker is unavailable.

From this checkout, set `PLECTARIUM_PACKET_PYTHON` to an interpreter with those
exact dependencies (the local `../local/contract-runtime/tooling.env` supplies
the workstation binding), then run:

```sh
"${PLECTARIUM_PACKET_PYTHON:-python3}" -I -B -m unittest discover -s tests -p 'test_*.py'
"${PLECTARIUM_PACKET_PYTHON:-python3}" -I -B scripts/contract_demo.py
```

The demonstration reads the packet manifest's exact schema pins, validates a
job fixture, emits an immutable schema/content receipt and rejects v99. It
does not schedule a job, assert tenant authorization or execute a capability.

## API and data boundaries

- `parse_json` rejects duplicate keys, invalid UTF-8, nonfinite numbers,
  malformed structure and configured byte/depth/node limits.
- `parse_yaml` accepts JSON-shaped safe YAML with duplicate-key checks; anchors,
  aliases, merge keys, non-string keys and non-JSON values are rejected. Dates
  and YAML 1.1 yes/no/octal implicit forms remain strings. Explicit safe tags
  must still produce finite JSON-shaped values.
- `SchemaRegistry` requires caller-supplied exact schema bytes and digests.
  The directory loader refuses symlinks and duplicate identities. The host
  decides which pin set is trusted; an observed hash is not trust by itself.
- The registry resolves only supplied draft-2020-12 schemas and exact document
  versions. Missing references, unsupported anchors/dynamic IDs and unknown
  versions fail; there is no network retrieval, fallback or automatic upgrade. Declared formats
  must have an available checker; missing optional dependencies never silently
  disable date-time or other format assertions.
  Traversal follows actual draft-2020-12 subschemas; annotation data stays data.
  Reference targets are checked as schemas even when stored in annotation data.
  Cycle tracking permits supported recursive references. Nested dialect changes
  are rejected. Boolean version subschemas require an
  explicit schema ID and do not invent an automatic version mapping.
- `validate` checks schema shape. It does not implement approval, permission
  subsets, tenant isolation, fencing, state transitions or other S1 semantics.
  The policy-widened packet fixture is structurally valid but semantically
  invalid; PLEC-POL-001 owns its runtime refusal.
- `receipt` additionally applies the internal canonical profile from ADR-007.
  It records the schema hash, encoding version, exact canonical bytes and their
  SHA-256. Its authority effect is always `none`.
- Migration functions are explicitly registered by trusted application code for
  an exact source/target pair. Both ends validate; source data is copied and
  never silently mutated. No migrations are enabled by default.

Canonical JSON permits bounded exact integers, JSON containers, strings,
booleans and null. Finite fractional values can parse and validate but cannot
yet receive this canonical identity. Unicode is preserved without normalization;
this encoding does not claim RFC 8785 compatibility. External payloads use
`content_digest(bytes)` and stay opaque. A checksum is neither a signature nor
permission to act.

## Remaining work

The source layout is deliberately limited to this internal package. PLEC-SEC-001,
PLEC-IAM-001, PLEC-CAT-001 and their dependent policy/job/artifact/runner/BOM tasks
remain unimplemented. No S1-wide completion, control-plane execution, stable
public package, supported BOM, service, release or production readiness is
claimed. The library is tested locally, not a cross-platform support promise.

Input size/depth/node limits are structural bounds, not a process sandbox or a
hard CPU/memory execution limit for arbitrary admitted schema expressions.
Schema-evaluation resource exhaustion and concurrent filesystem replacement
remain security/operational qualification work. Pins detect changed bytes;
they do not by themselves establish trust in the schema provider.
