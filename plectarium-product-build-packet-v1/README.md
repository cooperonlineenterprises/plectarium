# Plectarium Product Build Packet v1

**Packet version:** 1.0.0  
**Status:** setup-only Product Constitution, Executable Specification, and AI Build Packet

Plectarium provides one cohesive product experience, catalog, compatibility
view, and optional control plane for independently usable specialist
capabilities. It is part of the Octon ecosystem without requiring Octon or
inheriting its governance authority.

This packet defines intended product behavior. It contains no product code,
dependencies, services, deployment assets, or readiness evidence.

## Authority hierarchy

1. `CHARTER.md`
2. `spec/invariants.md`
3. normative specifications and JSON Schemas
4. accepted ADRs and `design/decisions.yaml`
5. `RELEASE-CRITERIA.md` and `evals/release-gates.yaml`
6. `agent/workstreams.yaml`
7. `agent/tasks/index.yaml` and task packets
8. implementation choices made under later authority

The external family packet governs family identity and shared capability
contracts. `reference/family-source-lock.json` pins that source after
publication. Plectarium wraps those contracts with suite metadata; it does not
copy or redefine them.

## Reading order

1. `CHARTER.md`, `spec/invariants.md`, and `ARCHITECTURE.md`.
2. `SECURITY.md` and the request/approval, job, runner, and result specs.
3. `design/decisions.yaml` and accepted ADRs.
4. `evals/claim-proof-matrix.md` and `evals/release-gates.yaml`.
5. `agent/implementation-dependency-graph.yaml` and `agent/tasks/index.yaml`.

## Validation

Read-only check:

```text
/Users/jamesryancooper/.pyenv/versions/3.14.0/bin/python3 -B scripts/validate-packet.py --family-root ../../family
```

Designated derived writer:

```text
/Users/jamesryancooper/.pyenv/versions/3.14.0/bin/python3 -B scripts/validate-packet.py --refresh-derived
/Users/jamesryancooper/.pyenv/versions/3.14.0/bin/python3 -B scripts/validate-packet.py --family-root ../../family
```

Validation proves packet integrity only. Product security, behavior,
performance, compatibility, operations, and release readiness remain
unassessed until implementation evidence satisfies the named gates. The exact
runtime path reflects the already-configured adoption host; portable
dependency bootstrap remains unresolved and no installation is implied.
