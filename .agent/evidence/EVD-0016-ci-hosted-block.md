---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0016",
  "title": "Hosted CI admission refused before execution",
  "task": "TASK-0008",
  "recorded_at": "2026-09-27",
  "subject_revision_or_fingerprint": "58547e3c5708982626786affa040538ae559bea2; GitHub Actions run 36342719832",
  "result": "blocked_external_prerequisites_no_job_steps_executed",
  "fresh_until": null,
  "supersedes": null
}
---

## Direct observations

Draft PR https://github.com/cooperonlineenterprises/plectarium/pull/1 publishes
branch ci/required-check with the two reviewed foundation commits and the scoped
CI change. All three checks in run
https://github.com/cooperonlineenterprises/plectarium/actions/runs/36342719832
were refused with no job steps. GitHub's annotations report recent account
payment failures or a spending limit. The API does not establish which cause
applies. No billing setting, budget, repository visibility, or runner was changed.

The repository and applicable organization secret inventories were empty and no
Actions environments existed. The workflow's required private family credential
is therefore unconfigured. Approval was requested for a dedicated read-only
family deploy key stored only as the suite Actions secret; none has been created.

The existing protect-main ruleset was read and preserved. It still has an empty
bypass list, zero-approval merge-only PRs, and deletion/force-push prohibitions.
No required-check rule was added because hosted success has not been observed.

A hash comparison confirmed the original checkout's HEAD, dirty status and all
tracked/nonignored regular files unchanged. The independent candidate clone owns
these changes. A fresh isolated Python 3.13.9 environment additionally installed
the exact requirements with --no-deps, passed pip check and the contract demo;
that is a supplemental local packaging check, not hosted Python 3.14 qualification.

## Resume and limits

Resolve the organization's Actions billing restriction through its proper owner.
After explicit approval, provision only the named read-only family credential.
Rerun hosted checks, inspect exact candidate results, then add the app-bound
required context and strict up-to-date policy with read-back. Preserve every
other rule. Keep the PR unmerged unless separately instructed.

EVD-0015's local results remain bounded to their recorded code/workflow inputs.
These observations do not prove hosted correctness, source integration, product
readiness or standing autonomy. TASK-0008 remains blocked and uncompleted.
