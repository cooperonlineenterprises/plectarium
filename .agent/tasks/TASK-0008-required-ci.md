---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0008",
  "title": "Prepare and qualify Plectarium's required repository CI gate",
  "status": "validating",
  "previous_status": "in_progress",
  "authority_basis": "Current operator instruction on 2026-09-27 to proceed with the proposed focused CI PR and add the passing check to the main ruleset. This does not authorize autonomous integration or create standing delegation.",
  "owner": "Plectarium repository maintainer via current Codex task",
  "created_at": "2026-09-27",
  "updated_at": "2026-09-27",
  "dependencies": ["TASK-0005"],
  "supersedes": null,
  "closure_evidence": [],
  "external_effects": "Candidate publication, PR creation, hosted validation, and the specified required-check ruleset amendment are in scope; no merge, release, deployment, or unrelated hosted change. A new family-read credential requires its own explicit access authorization.",
  "limitations": ["Existing uncommitted architecture work is excluded and preserved", "CI is not product readiness or qualified autonomous integration"]
}
---

## Scope

Build from reviewed commit `47181c370ebfd4fcd47177f169d192910c49fd32`, retaining
the two prerequisite contract-foundation commits not yet on hosted main. Add only
CI, its operating documentation, and scoped governance/evidence records. Work in
an isolated clone; preserve the original checkout and all uncommitted changes.
TASK-0006/0007 and EVD-0013/0014 already exist in that original working tree;
their identities are reserved even though their unrelated changes are excluded.

No product schema, family lock, accepted decision, or existing verification
threshold changes. The existing protected main and zero-approval PR path remain.

## Acceptance criteria

- [x] All existing harness, packet, hostile-pin and contract checks pass on the CI candidate.
- [x] The workflow pins its Actions/runtime/dependencies and verifies exact external family Git bytes.
- [ ] `required` passes only when every mandatory job passes, including real family verification.
- [ ] A focused PR exists with current hosted checks and declared prerequisite commits.
- [ ] Read-back of `protect-main` binds `required` to GitHub Actions with strict up-to-date checks and preserves all other controls.
- [ ] Original tracked/nonignored files, HEAD, and dirty status are unchanged.

This task ends at a qualified CI PR and configured required-check gate. Integrating
the PR is a separate source operation; neither task closure nor CI success claims
that the workflow is already present on main.

## Validation and recovery

Run the declared harness check/tests, packet check with exact family-root input,
hostile pin tests, product tests, and contract demonstration. Inspect the YAML
and exercise success/failure/skipped/cancelled aggregate inputs. Refresh only
through the designated harness integrity writer after changing candidate records.
Never refresh during hosted CI.

Missing family-read access blocks hosted qualification and ruleset completion;
finish the code and local evidence before requesting that concrete access.
Keep failed attempts and do not waive the family check. Preserve the prior
ruleset JSON for exact recovery of a narrowly failed amendment. Do not bypass,
force-push, alter main directly, or merge this PR as part of the task.
