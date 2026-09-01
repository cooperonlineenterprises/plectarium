# Plectarium

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
