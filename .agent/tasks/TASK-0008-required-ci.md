---
{
  "schema_version": "harness.task.v1",
  "id": "TASK-0008",
  "title": "Qualify and integrate Plectarium's required repository CI gate",
  "status": "review",
  "previous_status": "validating",
  "authority_basis": "Current operator resume instruction on 2026-09-27 explicitly authorizes PR #1 public-HTTPS CI updates, validation, its required-check ruleset amendment, protected merge-commit integration, and post-merge verification. This authority is limited to this PR; no general autonomous merging, release, deployment, or additional spending.",
  "owner": "Plectarium repository maintainer via current Codex task",
  "created_at": "2026-09-27",
  "updated_at": "2026-09-27",
  "dependencies": [
    "TASK-0005"
  ],
  "supersedes": null,
  "closure_evidence": [],
  "external_effects": "Scoped candidate push, hosted validation, exact required-check ruleset amendment, PR ready transition and protected merge commit for PR #1 are authorized. Use existing GitHub authentication and read-only workflow token. Public family access requires no new credential.",
  "limitations": [
    "Existing uncommitted architecture work is excluded and preserved",
    "CI is not product readiness or qualified autonomous integration"
  ]
}
---

## Scope

Build from reviewed contract foundation `47181c370ebfd4fcd47177f169d192910c49fd32`,
retaining its two prerequisite commits in PR #1. Reuse the isolated ci/required-check
checkout. Preserve every unrelated change in the original checkout, including
TASK-0006/0007 and EVD-0013/0014; their identities are not reused.

Current work removes the mandatory family secret/SSH path in favor of the public
HTTPS source, updates CI documentation and dated evidence, runs all checks,
qualifies the existing ruleset, and integrates this exact PR through its protected
merge-commit path. Product schemas, family source lock and digests, tests, runtime
pins, accepted decisions, and unrelated controls remain unchanged.

## Acceptance criteria

- [x] Applicable local harness, packet, hostile-pin, contract and workflow checks pass on the updated candidate.
- [x] Public HTTPS supplies the exact family commit and lock-bound manifest/checksum/contract bytes without a new credential.
- [ ] Fresh hosted repository checks, immutable family pin and aggregate required checks all succeed.
- [x] protect-main requires required from the observed GitHub Actions app with strict up-to-date checks; all other protections are preserved.
- [ ] PR #1 is marked ready and merged with a merge commit after exact head/base revalidation, without bypass or force-push.
- [ ] Actual remote-main commit/tree/parents and passing post-merge CI are recorded before closure.
- [ ] Original tracked/nonignored files, HEAD and dirty status remain unchanged.

The task remains open through integration and post-merge verification. Candidate
success, a ruleset change or a merge request alone cannot satisfy closure.

## Validation and recovery

Run the declared harness check/tests, packet check with an explicit standalone
public family checkout, hostile pin tests, product tests and contract demo.
Exercise the aggregate's success/failure/skipped/cancelled combinations. Refresh
only with the designated harness writer, never within hosted CI.

Inspect current PR head/base and remote policy before effects. Changed inputs
require renewed validation. After the merge request, read back actual state;
reconcile an unknown result before retrying. Public integration preserves history.
If GitHub refuses execution, retain the exact error and stop the dependent
ruleset/merge steps; never change billing, spending or waive a mandatory check.

## Historical scope and attempts — September 27, 2026

The initial instruction authorized a CI PR and required-check configuration but
excluded merging and required separate approval for new private-family access.
EVD-0015 preserves local qualification; EVD-0016 preserves the private-access gap
and GitHub billing/spending refusal before execution. The original PR remained
draft and no ruleset or credential change occurred. Those observations are dated
history, not current access requirements or proof of resolved billing.

The current explicit resume instruction extends only this task to public-HTTPS
verification and PR #1 integration. Repository visibility was changed by the
owner, then rechecked before updating the workflow. No deploy key is needed.

## Pre-integration checkpoint

EVD-0019 records real hosted success and the verified ruleset amendment. The
final metadata checkpoint still requires its own fresh hosted success, protected
integration and observed post-merge validation before closure.
