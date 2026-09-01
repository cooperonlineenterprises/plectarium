# Plectarium Product Security Constitution

**Status:** Normative target; no implemented control is claimed

## Objective

Plectarium must coordinate untrusted capabilities and controlled resources
without becoming a confused deputy, ambient credential path, cross-tenant data
channel, or authority amplifier.

## Trust boundaries

- untrusted capability manifests, plans, results, archives, and prose;
- untrusted subjects, repositories, project code, browser pages, networks,
  databases, infrastructure state, and external tool output;
- authenticated but least-privileged users, services, and runners;
- compromised, stale, duplicated, or impersonated runner sessions;
- queues, caches, indexes, object storage, telemetry, and AI providers;
- private and air-gapped transfer boundaries.

## Required controls

- deny by default at tenant, resource, operation, permission, and network scope;
- authenticate users, services, and runners separately;
- authorize approval rights independently from ordinary job-submission rights;
- bind execution to exact request, capability coordinate, plan digest, subject,
  scope, profile, runner, permissions, and expiry;
- use expiring fenced leases and reject stale or replayed completion;
- issue credentials by opaque reference, least scope, and shortest practical TTL;
- prohibit secret values in plans, queues, logs, metadata, and durable results;
- constrain filesystems, networks, processes, browsers, databases,
  infrastructure, production access, resources, and output paths by profile;
- validate paths, archives, media types, sizes, schemas, digests, signatures,
  lineage, and producer identity before catalog ingestion;
- isolate tenant authorization even if physical bytes are deduplicated;
- prevent cross-tenant existence or timing disclosure through caches/deduplication;
- treat result text and UI content as prompt-injection and active-content risks;
- preserve audit and verification status without equating signature validity
  with signer trust or action authority.

## Threat catalogue

Tenant breakout, IDOR, runner impersonation, stale leases, duplicate messages,
plan/approval TOCTOU, credential exfiltration, SSRF, network escape, malicious
archives, path traversal, symlink escape, result substitution, signature
confusion, lineage cycles, cache poisoning, quota evasion, denial of service,
log injection, prompt injection, air-gap rollback, and authority confusion must
all have negative fixtures and implementation evidence.

## Mode constraints

Private runners should establish outbound control connections where practical.
Air-gapped mode imports and exports explicit content-addressed bundles and
never silently contacts hosted services. A runner mode does not weaken the
accepted plan or permission envelope.

## Non-claims

This packet does not establish a security certification, compliance result,
supported-version policy, incident-response SLA, penetration result, or
production-readiness conclusion.
