# Plectarium suite — internal contract foundation

The suite now has a bounded internal Python contract/identity library. Its
[operation and limits](docs/contract-foundation.md) describe strict offline
parsing, schema pins, canonical receipts and explicit migration hooks. The
[authority review](docs/authority-review.md) precedes this first code-bearing
slice. See [.agent/state/current.json](.agent/state/current.json) for current
validation and review state. Later S1 semantics and the control plane remain
unimplemented.

## Historical repository-foundation documentation

# Plectarium

> **Current routing.** Live operational status is owned only by
> `.agent/state/current.json` and the active task named there. Older publication,
> evidence, and push language below is historical context, not authority.

Plectarium is a cohesive product experience and optional control plane for
independently usable specialist capabilities. It is part of the Octon
ecosystem, but it does not require Octon and does not inherit Octon authority.

This repository currently contains a governed, setup-only product
constitution, executable specification, and AI build packet. Product code,
dependencies, services, deployment assets, and production resources are
intentionally absent.

The repository foundation was published through the bounded `TASK-0002`
sequence. That publication creates no product-readiness or later-push
authority.

Start with:

- `AGENTS.md` for repository instructions;
- `.agent/START_HERE.md` for live governance and current work;
- `project-dossier/README.md` for intended/current/conformance separation;
- `plectarium-product-build-packet-v1/README.md` for the product specification.

The family contract is consumed by immutable reference. Plectarium must not
fork family schemas or implement capability-domain semantics.

Structural validation is not evidence of product, security, operational, or
release readiness.

The setup-only validation sequence uses the generated harness plus the
already-configured Python 3.14 packet runtime recorded in
`.agent/validators.json`; no dependency installation is implied or authorized.
