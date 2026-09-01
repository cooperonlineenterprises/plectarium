# Logical Data Ownership

| Record | Canonical owner | Mutability |
|---|---|---|
| Family source lock | Catalog | successor only |
| Catalog entry/snapshot | Catalog | immutable; status overlays append |
| Tenant/principal/access binding | Identity | controlled versioned state |
| Request and plan bytes | Policy/jobs plus artifact store | immutable |
| Approval/revocation | Policy | append-only decisions |
| Job | Jobs | monotonic state machine |
| Attempt/lease/event | Jobs/runner coordination | append-only except lease expiry metadata |
| Artifact/result bytes | Artifact store | immutable or authorized purge |
| Result verification/lineage | Result catalog | append-only/successor |
| Compatibility assertion/BOM | Catalog/release | immutable releases, successor status |
| Audit | Audit module | append-only within retention |
| Secret value | External credential broker | never owned by Plectarium |

Indexes, caches, and projections are reconstructible and non-authoritative.
Queue messages are delivery records, not canonical state.
