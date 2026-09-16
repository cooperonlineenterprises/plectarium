---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0004",
  "title": "Plectarium relocation baseline and candidate validation",
  "task": "TASK-0003",
  "recorded_at": "2026-09-15",
  "subject_revision_or_fingerprint": "baseline commit abeeccda9e34453e1cf425b4064f9cd98233ef13; tree a057348b283b92862fd693951694884040eb6fb3; relocation manifest sha256 2efeb8c17bd4d534f16884678ae790d37eaae53710ef7cf4acc56cbcf7251c11; exact candidate commit pending",
  "result": "pass_pending_independent_review",
  "fresh_until": null,
  "supersedes": null
}
---

## Approved baseline and recovery

The approved relocation manifest at
`/Users/jamesryancooper/Projects/plectarium/archive/migration-2026-09-15/relocation-manifest.json`
has SHA-256 `2efeb8c17bd4d534f16884678ae790d37eaae53710ef7cf4acc56cbcf7251c11`. It records the pre-move Plectarium checkout at
`/Users/jamesryancooper/Projects/octon-capabilities/plectarium` with:

- `HEAD` `abeeccda9e34453e1cf425b4064f9cd98233ef13`;
- tree `a057348b283b92862fd693951694884040eb6fb3`;
- origin `https://github.com/cooperonlineenterprises/plectarium.git`; and
- verified all-ref recovery bundle SHA-256 `710e8798e02558eeb5b0297751d4b6867cd0e3a22e223b371acac6fa5461a466`.

The bundle is retained under
`archive/migration-2026-09-15/checkpoints/plectarium-710e8798e02558eeb5b0297751d4b6867cd0e3a22e223b371acac6fa5461a466.bundle`.
It covers Git objects and refs only, as limited by the manifest.

## Post-move identity and candidate

Direct inspection after the non-overwriting same-filesystem moves found the
standalone checkout at
`/Users/jamesryancooper/Projects/plectarium/repos/plectarium`, with the expected
origin and the baseline commit/tree preserved in repository history and the
verified bundle. The authoring branch is
`codex/plectarium-workspace-migration`; no nested family Git repository,
symlink bridge, submodule conversion, remote rewrite, or history rewrite was
introduced.

The candidate removes mutable-upstream-HEAD coupling from packet provenance
checks. Explicit local upstream roots are checked by origin identity, pinned
commit-object existence, and exact blob bytes at the pinned commit. It adds
focused newer-HEAD, missing-commit, and wrong-digest regressions and updates
only current command/navigation surfaces plus designated derived integrity.

## Validation

Using `PLECTARIUM_PACKET_PYTHON=/Users/jamesryancooper/.pyenv/versions/3.14.0/bin/python3`:

- the read-only harness and dossier check passed;
- all 18 harness and mutation tests passed, including three focused pin tests;
- the full packet check passed with canonical sibling repositories;
- designated packet and harness integrity refreshes completed only after source
  edits froze; and
- JSON/Python parsing and `git diff --check` passed.

The designated refresh and final read-only checks are repeated after this
lifecycle record freezes. Independent T1 review must bind the exact committed
candidate; this evidence does not claim that review.

## Effects and limitations

No push, remote mutation, publication, deployment, provisioning, product
execution, production access, communication, paid service, or dependency
installation occurred. Temporary test writes were confined to temporary
directories. Operating-system access-time stability is not claimed. Product,
security, release, and production readiness remain unassessed.
