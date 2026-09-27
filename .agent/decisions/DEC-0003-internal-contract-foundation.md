---
{"schema_version":"harness.decision.v1","id":"DEC-0003","status":"accepted","previous_status":"proposed","title":"Adopt the bounded internal contract foundation","created_at":"2026-09-25","authority_source":"Current operator portfolio continuation after PLEC-FND-001 and independent REV-0008","supersedes":null,"successor":null}
---

Use Python 3.11+ for a small internal `src/plectarium_contracts` library and
checkout-only demonstration. Reuse the existing pinned PyYAML/jsonschema runtime.
This chooses no public package/CLI name, control-plane framework or service.
Packet PLEC-021/ADR-007 specifies exact offline schema registration and internal
canonical JSON encoding. Family contracts stay external and immutable.

Allow only this source package through the old foundation-only packet check;
retain prohibitions on other product roots, family schema copies, unsafe paths,
unreviewed dependency/build roots and stale integrity. Application validation
remains distinct from packet/harness validation.

This decision is additive to DEC-0001/0002 and does not reinterpret their
accepted boundaries. Later public interfaces, authorization, execution,
packaging and stable wire canonicalization require their own tasks and evidence.
