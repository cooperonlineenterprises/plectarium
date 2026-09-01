# Cohesive Product Experience

## Primary workflows

The application must let an authorized user:

1. discover families and exact capability versions without executing code;
2. understand operations, requirements, limitations, and compatibility;
3. create a request with exact subject and scope;
4. inspect the capability-authored plan and requested effects;
5. approve, narrow, deny, or let the plan expire through an authoritative channel;
6. observe queue, lease, running, cancellation, recovery, and terminal state;
7. inspect immutable result bytes, completion, limitations, provenance, and lineage;
8. compare supported result projections without changing canonical payloads;
9. export/import verified bundles when the deployment mode requires it.

## Truthful presentation

UI language must distinguish control state from capability completion, absence
of findings from complete coverage, checksum verification from signer trust,
compatibility from support, cancellation request from cancellation, and a
capability conclusion from downstream authority.

Unknown, stale, partial, denied, unavailable, incompatible, corrupt, and
unverified states must remain visible. Character identities are presentation
metadata; machine identity always remains explicit.

## Accessibility and localization

All critical approval and completion meaning must be available without color,
animation, hover, or character imagery. Exact accessibility acceptance level,
browser support matrix, and localization scope require owner decisions and
fresh evaluation; the packet makes no current conformance claim.

## Interface unity

Web, suite CLI, and API project the same application services and schemas.
Convenience interfaces cannot add hidden installation, broader permissions, or
different completion semantics.
