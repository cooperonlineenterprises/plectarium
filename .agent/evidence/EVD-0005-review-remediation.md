---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0005",
  "title": "Plectarium rejected-candidate remediation and validation",
  "task": "TASK-0003",
  "recorded_at": "2026-09-15",
  "subject_revision_or_fingerprint": "rejected parent commit 670d43e900293f70f118b0562af735795a06c242; exact corrected candidate commit pending",
  "result": "pass_pending_independent_rereview",
  "fresh_until": null,
  "supersedes": "EVD-0004"
}
---

## Review findings and corrections

| Finding | Correction |
|---|---|
| CRA-01 / B1 | Renamed the dependency-bearing pin suite to `.agent/tests/packet_pin_test.py`, outside default `test_*.py` discovery, and registered a separate `packet_pin_test` command using `${PLECTARIUM_PACKET_PYTHON:-python3}`. |
| CRA-02 / B2 | Every validator Git subprocess now uses a local sanitized environment: inherited `GIT_*` is removed; prompts, optional locks, global/system config, lazy fetch, replacement refs, and user-selected protocols are disabled; `PATH` and locale are fixed. Raw origin identity is read with `git config --local --no-includes --get remote.origin.url`. |
| CRA-02 / B3 | CLI roots are lexically checked before resolution, every existing component is inspected with `lstat`, and symlink aliases and redundant traversal are rejected. `main` no longer resolves unvalidated arguments. |
| CRA-02 / B4 | Git top-level, `.git`, and common-dir must all be confined to the exact standalone checkout. The separate suite covers inherited `GIT_DIR`/`GIT_WORK_TREE`, URL rewriting, replacement refs, promised missing blobs without lazy fetch or writes, symlink aliases, redundant traversal, linked-worktree common dirs, newer upstream heads, missing commits, and wrong digests. |
| CRA-03 / B5 | Root and dossier navigation now defer to `.agent/state/current.json` and this successor evidence. Handoff pages contain no current instruction to push; dated observation bodies remain preserved behind explicit successor banners. |

## Validation split

After all source, navigation, and successor-evidence edits freeze:

- plain `python3 -B -m unittest discover -s .agent/tests -p 'test_*.py'`
  runs the 15-test standard-library harness/mutation suite;
- the configured Python 3.14 packet interpreter runs 10 dependency-bearing
  packet-pin regression tests through the registered `packet_pin_test`
  command;
- the read-only harness check and full packet check pass;
- strict JSON and Python parsing pass;
- designated packet and harness integrity refreshes are followed by read-only
  rechecks; and
- staged and committed diffs pass `git diff --check`.

The exact commands and results are rerun on the committed successor. This
record does not claim independent rereview or integration.

## Preservation, effects, and limitations

The rejected commit remains the direct parent; no amend, rebase, history
rewrite, or push occurs. Earlier tasks, evidence, reviews, checkpoints, events,
and provenance locks retain their existing bytes. New event lines are
append-only. No dependency installation, network access, remote mutation,
publication, deployment, production access, or product action occurred.
Product, security, release, and production readiness remain unassessed.
