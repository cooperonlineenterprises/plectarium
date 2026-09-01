# Cancellation and Recovery Sequence

1. Authorized actor records `cancel_requested` with job revision.
2. Scheduler stops new lease issuance and sends cancellation to the current fenced attempt.
3. Runner acknowledges and terminates, reports an already-raced terminal result,
   or becomes unreachable.
4. Unreachable state remains explicit until lease expiry and reconciliation.
5. Reconciler compares job revision, lease/fencing token, runner report, and uploaded content.
6. Job becomes `cancelled`, `completed`, or `failed` with exact reason; it never
   reports cancellation merely because a request was sent.
7. Retry creates a new attempt only when replay safety and approval remain valid.
