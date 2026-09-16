# Start Here

> Navigation only; this page grants no permission. Reinspect current
> instructions, repository state, and direct evidence.

## Current position

- Active work: corrected migration `TASK-0003` is validating.
- Current correction evidence: `EVD-0005`.
- The rejected source candidate `670d43e900293f70f118b0562af735795a06c242` remains preserved as the
  parent of the correction candidate.
- Historical publication records are noncurrent and grant no push or other
  external authority.
- Product implementation and readiness remain unassessed.

## Resume safely

1. Read root-to-leaf `AGENTS.md`, then `.agent/state/current.json`.
2. Read `TASK-0003` and successor evidence `EVD-0005`.
3. Inspect the exact branch, commit, tree, origin, and clean status.
4. Run the plain-`python3` default harness suite from
   `.agent/validators.json`.
5. Run the separate dependency-bearing `packet_pin_test` command with the
   configured packet interpreter.
6. Run the full packet check with the canonical sibling repositories.
7. Obtain independent T1 rereview before any serial local integration.

Do not push, publish, deploy, provision, execute product code, access
production, or infer readiness from these records.
