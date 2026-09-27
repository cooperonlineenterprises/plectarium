---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0019",
  "title": "Hosted required gate and main ruleset verified",
  "task": "TASK-0008",
  "recorded_at": "2026-09-27",
  "subject_revision_or_fingerprint": "Candidate 227b7375081dc005f71b6b7d54548de90e098b53; run 36347869507; protect-main 24080688",
  "result": "hosted_success_and_ruleset_readback_verified_integration_pending",
  "fresh_until": null,
  "supersedes": null
}
---

## Observed hosted success

Run https://github.com/cooperonlineenterprises/plectarium/actions/runs/36347869507
completed successfully for head 227b7375081dc005f71b6b7d54548de90e098b53 against
main c4c2cc4e1c02f2632c00b6a220dee60f192e0da8. Both repository checks and immutable
family pin executed and succeeded, followed by the successful required aggregate.
The check's observed app was github-actions, numeric ID 15368. No family secret,
deploy key, private access or additional spending configuration was used.

## Ruleset effect and read-back

Under the current explicit operator instruction, protect-main (24080688) was
amended after that hosted success. At 2026-09-27 20:26 UTC, direct ruleset and
applicable-main-rule readbacks confirmed required from integration 15368 and
strict up-to-date checks. The empty bypass list, zero approvals, merge-only PR
policy, deletion/force-push prohibitions, target and every other pre-existing
rule parameter were preserved. Before/attempt/response/after evidence is retained
outside the source tree in the scoped operation receipt.

## Remaining acceptance

This source checkpoint records completed qualification and control effects while
TASK-0008 remains in review. Its changed metadata requires a fresh passing check
on the final PR head. Mark ready, revalidate exact head/current base and effective
rules, then merge only through the protected merge-commit path. Observe the actual
remote main commit/tree/parents and post-merge workflow before any closure claim.
A merge request, candidate pass or this record cannot substitute for those facts.

Post-integration receipts must be written after observation; they are not
pre-populated in the candidate. Retain those dated receipts and link their exact
commit/run identities from the PR completion record. Historical billing and
origin-mismatch failures remain in EVD-0016/EVD-0018.
