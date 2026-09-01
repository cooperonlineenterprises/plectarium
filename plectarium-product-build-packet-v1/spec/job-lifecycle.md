# Job Lifecycle

Control-plane state is distinct from family capability completion.

## States

```text
received
planning
awaiting_approval
queued
leased
running
cancel_requested
finalizing
completed
denied
expired
cancelled
failed
```

Normal flow:

```text
received → planning → awaiting_approval → queued → leased → running
         → finalizing → completed
```

`awaiting_approval` may terminate as `denied` or `expired`. `queued`, `leased`,
or `running` may enter `cancel_requested`, followed by `cancelled`, `failed`,
or a legitimately raced terminal result. Invalid transitions are rejected and
recorded.

## Completion preservation

A `completed` control job must include the family result reference and preserve
one capability completion state: `complete`, `complete_with_limitations`,
`partial`, `failed`, or `cancelled`. The UI must show both layers. A denied or
expired job may have no capability result and must not synthesize one.

## Attempts and leases

Retries create immutable attempt records. Exactly one current attempt holds a
monotonic fencing token. Lease acknowledgement, start, heartbeat, completion,
expiry, and reconciliation are append-only events. A stale attempt may upload
quarantined bytes but cannot terminalize the job.

## Cancellation

`cancel_requested` is an intent, not proof of termination. The runner must
acknowledge, a terminal result may race, or reconciliation must establish lease
expiry/process termination before `cancelled` is displayed.
