# Source Map

| Product concept | Canonical owner | Source used |
|---|---|---|
| Plectarium identity and repository scope | Current operator invocation | Workspace-preserved prompt v2, provenance only after invocation |
| Family ID, character registry, shared capability contracts | Family repository | Immutable lock in `family-source-lock.json` |
| Suite product semantics and BOM | This packet | Charter, invariants, specs, schemas, accepted ADRs |
| Capability-domain semantics | Each capability repository | Never copied into this packet |
| Octon governance and downstream action | Octon/human governance | Outside Plectarium product authority |
| Current implementation/readiness | Direct repository/runtime evidence | Project dossier current-state and future release evidence |

Project Blueprint 1.0.0 supplies harness/dossier structure only. The family
source is pinned to published commit
`0b6c476682e416bd4fb770622c56758f5a380f09`; mutable working-tree observation
does not replace that immutable reference.
