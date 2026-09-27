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
report `success`. Failure, cancellation, missing credentials, or a skipped job
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

## Private family access

The ordinary workflow token cannot read the separate private family repository.
Configure a dedicated **read-only** deploy key on
`cooperonlineenterprises/plectarium-family`, with its private half stored as the
Plectarium Actions secret `PLECTARIUM_FAMILY_READ_KEY`. Do not enable write access
or reuse a developer credential. Provisioning this key is a separate explicit
access decision; this document and workflow create no access themselves.

The family checkout accepts only the exact commit in the resolved source lock
and the fixed family repository. After authenticated SSH checkout, its local
origin is normalized to the lock's canonical HTTPS spelling; the packet validator
then verifies the pinned Git objects and digests. No family code is executed.

Deploy keys do not expire automatically. The repository owner retains revocation
and rotation responsibility. Revoke by removing the family deploy key and the
suite secret; subsequent family verification must fail. A future GitHub App
credential may replace this route through a scoped reviewed change. Fork PRs
without the secret fail the family gate; they never receive a fabricated pass.

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
