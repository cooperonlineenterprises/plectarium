# Failure, Retry, Idempotency, Cancellation, and Recovery

## Idempotency

An idempotency key is scoped by tenant and operation. It binds the canonical
request digest. Reuse with identical semantics returns the existing result;
reuse with different semantics is a conflict and security signal.

## Retry

Automatic retry is allowed only when the accepted plan declares the operation
replay-safe under identical subject, scope, permissions, profile, and inputs.
Every retry creates a new immutable attempt. Credential-consuming,
controlled-resource, browser, or other side-effect-sensitive work defaults to
renewed review unless explicitly proven replay-safe.

## Failure classes

Distinguish validation, incompatibility, authorization, scheduling, quota,
runner, lease, execution, cancellation, upload, verification, persistence,
and internal failures. Retriability is explicit and never inferred from a
generic error code.

## Partial effects

Unexpected writes, network, credential use, or controlled-resource effects are
security events. Plectarium preserves the exact attempt, stops or quarantines
according to policy, and never retries blindly.

## Recovery

Reconciliation compares transactional state, event history, leases, runner
reports, and uploaded content. Backup/restore must preserve content identity,
tenant authorization, monotonic revisions, fencing epochs, and audit ordering.
Restored stale leases cannot execute.
