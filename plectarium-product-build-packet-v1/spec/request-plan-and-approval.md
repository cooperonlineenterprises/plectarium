# Request, Capability Plan, and Approval

## Request

A request binds tenant, requester, exact capability coordinate, operation,
subject identity, scope, desired outputs, constraints, and idempotency key. It
contains no authority to execute.

## Capability-authored plan

The selected capability produces the canonical plan. Plectarium stores its
bytes immutably and records schema ID, SHA-256 content identity, capability
coordinate, request digest, subject/scope digest, requested permissions,
providers/tools, network/credential categories, outputs, limits, expected
limitations, and replay-safety declaration.

Plectarium may display a normalized summary but cannot change the plan. Any
material substitution—coordinate, tool/provider version, subject, scope,
permission, network, credential, profile, output semantics, or replay
rule—requires a new plan digest and review.

## Approval

An approval record identifies actor, authoritative policy/human sources, exact
plan digest, accepted permission subset, constraints, effective time, expiry,
and decision:

```text
approved
approved_with_narrowing
denied
expired
revoked
```

Accepted permissions must be a subset of requested permissions. An approval
does not authorize downstream action beyond executing the bound plan.

## TOCTOU defense

Scheduling and lease issuance revalidate request, coordinate, plan digest,
approval, permission subset, subject/scope binding, profile, expiry, tenant,
runner compatibility, and revocation. A mismatch returns to review or fails
truthfully; it is never patched in place.
