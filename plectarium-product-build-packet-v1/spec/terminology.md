# Plectarium Terminology

| Term | Meaning |
|---|---|
| Family source lock | Immutable repository/packet/contract identity for one capability family. |
| Capability coordinate | Family ID, capability ID, exact version, artifact digest, and relevant schema identity. |
| Catalog snapshot | Immutable view of validated catalog entries at one content digest. |
| Suite BOM | Exact capability coordinates supported by one Plectarium distribution or release. |
| Capability plan | Capability-authored immutable description of intended work and effects. |
| Plan binding | Suite record linking request, plan bytes/digest, subject, scope, permissions, profile, and expiry. |
| Permission decision | External human/policy decision that may deny or narrow a plan, never widen it. |
| Job | Tenant-scoped orchestration record distinct from capability completion. |
| Attempt | Immutable execution try under one job and fencing token. |
| Runner lease | Expiring, fenced right for one runner to execute one accepted attempt. |
| Execution profile | Declarative filesystem, process, network, browser, controlled-resource, credential, and resource boundary. |
| Artifact record | Tenant-authorized immutable metadata for content-addressed bytes. |
| Result record | Suite wrapper around a family-validated capability result reference and verification state. |
| Verification state | Checksum/signature/schema/producer validation facts; not trust or action authority. |
| Compatibility assertion | Dated, evidence-backed relation between exact coordinates and constraints. |
| Control completion | Terminal job orchestration state. |
| Capability completion | Family-defined work completion preserved from the result. |
| Air-gap bundle | Content-addressed export/import manifest with replay and source-context protection. |
