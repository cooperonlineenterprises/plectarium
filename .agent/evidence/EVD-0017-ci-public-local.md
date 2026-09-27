---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0017",
  "title": "Public family access and updated CI local qualification",
  "task": "TASK-0008",
  "recorded_at": "2026-09-27",
  "subject_revision_or_fingerprint": "Base 67deb13e8c4434a99698ed2255250c3906036a33; workflow SHA-256 d75396009a8008732c122a4b7eca6ca8feb3ad71d157dcf5a895b78ad0a2124d",
  "result": "public_access_and_local_validation_passed_hosted_pending",
  "fresh_until": null,
  "supersedes": null
}
---

## Authority and observed baseline

The current operator explicitly authorized public-HTTPS workflow updates, scoped
validation and ruleset amendment, protected merge-commit integration of PR #1,
and post-merge verification. It grants no general autonomous merging, release,
deployment or additional spending. Existing authenticated GitHub access and the
read-only workflow token are in scope; no new credential is needed.

At 2026-09-27 20:14 UTC, GitHub reported octon, plectarium and plectarium-family
public, retaining numeric repository identities 1385977828, 1353053797 and
1353037438. PR #1 was draft at 67deb13e8c4434a99698ed2255250c3906036a33, with main
still c4c2cc4e1c02f2632c00b6a220dee60f192e0da8. The isolated checkout matched that
head and had no source changes. The original dirty checkout was inventoried for
preservation; its unrelated architecture work remains excluded.

## Direct qualification

A fresh standalone checkout fetched public HTTPS commit
0b6c476682e416bd4fb770622c56758f5a380f09 with system/global Git configuration,
credential helpers, authorization extraheaders and interactive prompts disabled.
No private-family access or deploy key was used. The packet validator then
verified the actual pinned Git objects and all lock-bound manifests/digests.

Python 3.14.0 in the existing isolated runtime passed 15 harness tests, 10 hostile
pin tests and 31 contract/layout tests, plus the contract demonstration. The
read-only harness check passed after designated refresh. The first check had
found ignored .agent/.DS_Store host metadata in the isolated clone; its exact
bytes were preserved outside source before the successful rerun.

The updated workflow parsed as YAML. Its repository-check job, required aggregate,
family digest-verification command, product schemas, family lock, test sources,
dependency pins and prior EVD-0015/0016 bytes are unchanged from the reviewed
baseline. All 16 aggregate-result combinations were exercised: only both-success
passes. The workflow contains no family-key preflight, SSH input or origin rewrite.

## Evidence and limits

Raw API observations, anonymous-fetch receipts, local logs and workflow checks
are retained in this task's external public-resume evidence directory. The earlier
billing and private-access facts remain dated history in EVD-0015/0016. Public
visibility does not prove billing admission. Fresh hosted checks, ruleset readback,
actual protected integration and post-merge validation remain gates; task closure
is not claimed by these local results.
