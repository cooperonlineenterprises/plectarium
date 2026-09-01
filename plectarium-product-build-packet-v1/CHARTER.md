# Plectarium Product Charter

**Authority:** Highest Plectarium product authority  
**Status:** Established by the current portfolio foundation authority

## Purpose

Plectarium gives people and organizations a coherent way to discover, select,
authorize, run, inspect, compare, retain, and verify independently versioned
specialist capabilities without turning those capabilities into one engine.

## Users

- developers, reviewers, architects, operators, and release owners;
- tenant administrators and permission approvers;
- local and hosted CI systems;
- private and air-gapped runner operators;
- auditors and evidence consumers;
- Octon and other harnesses using narrow contracts.

## Product promise

Plectarium will provide:

- a multi-family-capable catalog with exact identity and version discovery;
- one cohesive web/application and suite-CLI experience;
- explicit request, capability plan, permission review, job, cancellation,
  quota, retention, and recovery semantics;
- coordination across local, hosted, private, customer-controlled, and
  air-gapped runners;
- immutable artifact/result records with provenance, lineage, checksum,
  signature, freshness, and compatibility status;
- an exact supported suite bill of materials;
- truthful state and limitations across every interface.

## Constitutional boundaries

Plectarium is not a capability, domain engine, generic harness, plugin
marketplace, package installer, automatic remediation system, or downstream
deployment/publication authority. It must not:

- implement capability-specific findings, claims, conclusions, or algorithms;
- require a capability to depend on Plectarium, Octon, MCP, AI, or hosting;
- import sibling capability source or share mutable domain tables;
- treat transport, runner location, an approval UI, or a result as stronger
  authority;
- turn Sibyl into the scheduler or Plectarium into Release Assurance;
- extract a shared capability runtime before the family threshold and ADR.

## Octon relationship

Plectarium is part of the Octon ecosystem. The relationship is descriptive and
integrative, not a runtime dependency or transfer of governance authority.

## Success

Mature-v1 success requires fresh evidence for every release gate, including
tenant isolation, authority binding, lifecycle truth, runner security,
artifact integrity, multi-mode equivalence, resilience, operations, and
release provenance. A complete packet or Minimum Complete Control Plane is not
itself a mature product.
