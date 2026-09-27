# Repository CI

The `validate` workflow checks pull requests to `main`, pushes to `main`, and
explicit workflow dispatches. It runs the declared repository validation against
the exact event checkout. Pull requests use GitHub's candidate merge checkout.
It does not refresh integrity files, merge, publish, release, or deploy.

`repository checks` runs the harness/dossier check, harness mutation tests, packet
structure/integrity check, hostile family-pin tests, offline contract tests, and
the checkout-only demonstration. `immutable family pin` separately verifies the
real Git objects at the consumed family commit, including the packet manifests
and every consumed contract digest. Packet structure alone does not satisfy it.

The stable `required` check depends on both jobs and succeeds only when both
report `success`. Failure, cancellation, unavailable source bytes, or a skipped job
cannot produce a passing gate. No path filter suppresses a required run.

## Runtime and authority

- GitHub-hosted Ubuntu 24.04 with Python 3.14.0; no broader platform claim.
- Checkout and Python setup Actions are pinned to full reviewed commit IDs.
- Each execution job installs `requirements-contracts.txt` into an ephemeral
  virtual environment outside the checkout, with automatic dependencies disabled
  and `pip check` required. No developer/global environment is changed.
- The workflow token has repository `contents: read` only. The aggregate job has
  no token permissions. Checkouts do not persist their credentials.
- New pull-request runs cancel older runs for the same PR. Main and manually
  dispatched runs have independent identities.
- The family pin and schemas remain unchanged. Family files are checked out
  beside the suite for verification, never copied into its product or package.

CI receipts establish bounded validation, not product readiness, grant coverage,
independent review, or a protected verifier baseline for autonomous integration.
The latter still requires the separately qualified governance and host controls.

## Public family access

The family repository is public. The pinned checkout Action uses HTTPS and the
ordinary read-only workflow token; it needs no family secret, deploy key, SSH
input, or origin rewrite. It accepts only the exact commit in the resolved
source lock and the fixed `cooperonlineenterprises/plectarium-family` repository.
The packet validator verifies the pinned Git objects, packet manifest/checksum,
and every consumed contract digest. No family code is executed.

Unavailable public Git objects or mismatched source identities/digests fail the
mandatory family job. Public visibility does not waive verification and is not
proof that GitHub admitted or successfully executed a workflow.

### Earlier qualification attempt — September 27, 2026

EVD-0015 and EVD-0016 retain the earlier private-repository observation and
unconfigured-credential requirement. Runs 36342719832 and 36343043493 were refused
before any job steps because GitHub reported an account payment or spending-limit
restriction. No family key was created. The owner subsequently made the suite
and family repositories public and authorized this PR's scoped integration.
New hosted results, rather than the visibility change, determine whether that
execution restriction remains. Billing and spending settings are unchanged.

## Ruleset admission

After the hosted workflow has demonstrated the real `required` check, require
that exact context from GitHub Actions in `protect-main` and enable strict
up-to-date checks. Preserve the existing empty bypass list, zero human approvals,
merge-only PR rule, and force-push/deletion prohibitions. Enabling this CI gate
does not enable autonomous merging.

## Local equivalent

Using the exact existing contract environment, run the commands in
`.agent/validators.json`. Pass an explicit standalone family repository to:

```text
python -B plectarium-product-build-packet-v1/scripts/validate-packet.py --family-root /absolute/path/to/family/repo
```

The family checkout must contain the lock's exact Git commit and canonical local
origin URL. A missing, incorrect, or merely copied directory is not a valid pin.
