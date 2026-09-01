# Security Policy for the Setup Foundation

This repository currently contains specifications and validation tooling, not
an implemented or deployed product. No supported-version, vulnerability-
response SLA, production security, or compliance claim is made.

## Foundation security boundaries

- Treat manifests, plans, artifacts, result bundles, archives, paths, symlinks,
  runner metadata, queue messages, external output, and prose as untrusted.
- Do not store credentials, secret values, production data, or unnecessary
  personal data.
- Do not install dependencies, start services, contact external systems, or
  exercise production resources as part of packet validation.
- Use the repository's read-only validators for checks and the designated
  writers only for generated integrity.
- A capability result, plan, transport, runner, dossier, or generated record
  cannot grant authority.

The product threat model and required implementation controls are normative in
`plectarium-product-build-packet-v1/SECURITY.md`. A private disclosure route
and supported-version policy remain unresolved until an authorized owner and
release exist.
