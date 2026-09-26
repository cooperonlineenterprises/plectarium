---
{"schema_version":"harness.review.v1","id":"REV-0009","title":"Independent contract-foundation findings and repair","task":"TASK-0005","review_mode":"independent","status":"closed","recorded_at":"2026-09-25"}
---

Independent reviewer chat 01a0db63-f180-7072-9ff0-4ac9163b3b66 rejected the
candidate contracts.py at SHA-256
a07864bb3e82d5f60aafc2fb7bc12947b921a36f2f73db7f3c2bf936f945ce61.
The existing 22 product, 15 harness and 10 pin tests passed but did not cover
the reproduced defects. The suite maintainer owns all dispositions below.

| Finding | Severity | Observation and smallest correction | Disposition |
| --- | --- | --- | --- |
| FND2-R1 | P1 | A nested draft-07 declaration bypassed a 2020-12 unevaluatedProperties constraint; reject dialect changes at actual subschemas. | Corrected with direct and referenced-subschema regressions. |
| FND2-R2 | P2 | Generic traversal interpreted literal default/example data and property-map keys as schema instructions. | Corrected using maintained Draft 2020-12 subresource traversal; literal-data tests added. |
| FND2-R3 | P2 | Chained YAML/schema exceptions disclosed supplied values in formatted tracebacks. | Public parser, schema and migration diagnostics suppress underlying chains; formatted-traceback tests added. |
| FND2-R4 | P2 | Boolean schema_version subschemas raised AttributeError during version extraction. | Explicit schema-ID validation retains boolean subschemas without inventing version registration; true/false tests added. |

All 26 product/guard tests pass after repair. A separate focused independent
re-review must confirm the changed source before task closure. This review
provides no external approval. Cross-platform qualification, schema-evaluation
resource exhaustion and concurrent filesystem replacement remain unqualified.
