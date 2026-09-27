---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0015",
  "title": "Local validation of the focused required-CI candidate",
  "task": "TASK-0008",
  "recorded_at": "2026-09-27",
  "subject_revision_or_fingerprint": "Contract foundation 47181c370ebfd4fcd47177f169d192910c49fd32; workflow SHA-256 e87216bf61246506c15db141fc7e2270b28f24e85a8ca2db7e0bb7b07a7a870d",
  "result": "local_checks_passed_hosted_qualification_pending",
  "fresh_until": null,
  "supersedes": null
}
---

## Observed checks

Python 3.14.0 in the existing isolated contract environment ran the unchanged
foundation test entry points against this isolated candidate on 2026-09-27:
15 harness mutation tests, 10 hostile Git-pin tests, and 31 contract/layout tests
passed. The packet validator passed with the actual standalone family repository,
resolving immutable commit 0b6c476682e416bd4fb770622c56758f5a380f09 and its lock-bound
manifest/checksum/contract bytes. The contract demonstration passed and rejected
an unknown breaking version. The harness structural check passed after its
explicit designated integrity refresh.

The workflow parsed as YAML. Its actual aggregate shell accepted success/success
and rejected all other 15 combinations of success/failure/cancelled/skipped.
Its missing-family-credential preflight returned failure. These shell probes do
not substitute for hosted Actions execution or SSH authentication.

Checkout v6.1.0 and setup-python v6.3.0 tag objects were read from GitHub and
matched the full pins in the workflow. Checkout's pinned implementation removes
authentication before returning when persist-credentials is false. Read-only
repository/organization secret and environment inventories found no configured
family-read credential. No secret values were read or copied.

## Scope and limitations

The two reviewed local foundation commits are necessary PR prerequisites; the
original checkout's uncommitted architecture records are excluded. This task
changes no product source, normative packet/schema, family lock, or dependency
version. Local logs are retained outside Git under the task's CI evidence area.

Hosted qualification and the required-check ruleset amendment are still pending.
Creating the dedicated read-only family credential requires explicit access
approval. The workflow refuses that missing input rather than skipping the check.
No independent reviewer, product readiness, signing profile, protected verifier,
standing grant, source integration, release, or deployment is established here.
