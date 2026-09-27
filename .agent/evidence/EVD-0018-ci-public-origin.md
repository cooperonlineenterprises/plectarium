---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0018",
  "title": "Hosted public execution and exact-origin correction",
  "task": "TASK-0008",
  "recorded_at": "2026-09-27",
  "subject_revision_or_fingerprint": "Hosted candidate 1c316ba80921925c2a6facbdd7cef77730e06909; corrected workflow SHA-256 d4b27ce1f2cb3297f19efdedffaedf519ebf40432005647c62cec5d4882cd600",
  "result": "execution_admitted_origin_mismatch_corrected_fresh_hosted_check_pending",
  "fresh_until": null,
  "supersedes": null
}
---

## Hosted observation and correction

Run https://github.com/cooperonlineenterprises/plectarium/actions/runs/36347633545
executed on the public-access candidate. Repository checks succeeded. The family
job reached its verifier and failed because the checkout Action recorded origin
https://github.com/cooperonlineenterprises/plectarium-family without the `.git`
suffix required by the unchanged source lock. The following missing-blob reports
were consequences of refusing that unapproved root, not evidence that the public
Git objects were absent. The aggregate correctly failed.

This run establishes that GitHub admitted execution for this candidate; it is not
an assertion about account payment state or future runner availability. Earlier
billing refusals remain preserved in EVD-0016.

The corrected workflow initializes an isolated family repository with the exact
canonical HTTPS origin from the outset and fetches/checks out the full lock pin.
Credential helpers, authorization extraheaders, system/global Git configuration
and prompts are disabled for this public fetch. No post-checkout origin rewrite,
SSH path, deploy key or weakened verifier is needed. The actual fetch-step shell
was executed locally in a fresh directory and passed; packet validation against
that resulting standalone Git checkout passed all pinned-byte checks.

The repository-check job, aggregate, test sources, schema/lock bytes, runtime and
dependency pins remain unchanged. New hosted results for the corrected source are
required before ruleset amendment or merge. No source integration or closure is
claimed by this correction.
