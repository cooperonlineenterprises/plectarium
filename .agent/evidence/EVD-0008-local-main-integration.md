---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0008",
  "title": "Plectarium observed local-main integration",
  "task": "TASK-0003",
  "recorded_at": "2026-09-15",
  "subject_revision_or_fingerprint": "integrated main 2b301b437490ca49317cabbcccf80a929f633817; tree 27f8d4fe25fa2e5538aafb60c9b9be44d2c782c4; evidence successor pending",
  "result": "pass_integrated_pending_final_read_only_review",
  "fresh_until": null,
  "supersedes": "EVD-0007"
}
---

## Direct integration observation

Immediately before this evidence record was added:

- the active branch was `main`;
- local `HEAD` was approved head `2b301b437490ca49317cabbcccf80a929f633817`;
- its tree was `27f8d4fe25fa2e5538aafb60c9b9be44d2c782c4`;
- preserved branch `codex/plectarium-workspace-migration` pointed to the same
  commit;
- repository status was clean;
- exactly one canonical worktree existed at `/Users/jamesryancooper/Projects/plectarium/repos/plectarium`;
- raw local origin remained `https://github.com/cooperonlineenterprises/plectarium.git`; and
- local `origin/main` remained pre-migration commit `abeeccda9e34453e1cf425b4064f9cd98233ef13`, so no
  migration commit was pushed.

## Family aggregate topology

After all serial fast-forward integrations, the workspace command
`python3 -I -B scripts/validate_portfolio.py --check` passed. It verified the
canonical sibling topology, exact local Git tuples, cleanliness, path
boundaries, and no-effect script rules. It performed no network or live-remote
inspection.

## Final-review boundary

Integration is directly observed, but the commit containing this evidence is a
new evidence-bearing head. The migration task remains at `review` until that
exact head receives final read-only T1 approval. This record does not claim
task completion or final review. No external effect occurred.
