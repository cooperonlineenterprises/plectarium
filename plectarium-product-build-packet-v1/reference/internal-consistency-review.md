# Internal Consistency Review

The charter, invariants, decisions, module ownership, schemas, task graph, and
claim gates use the same boundaries:

- family contracts are external and immutable;
- Plectarium owns suite control semantics and exact BOM only;
- capability plans/results remain capability-owned domain documents;
- control state and family completion are distinct;
- all modes preserve authority and provenance;
- only `PLEC-FND-001` starts ready;
- setup integrity is not implementation readiness.

The family source is resolved to closure commit
`0b6c476682e416bd4fb770622c56758f5a380f09`; packet and consumed-contract
digests are checked by the packet validator against the clean family worktree.
The contracts remain provisional by family authority despite exact byte pinning.
