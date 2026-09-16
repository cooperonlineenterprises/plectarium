---
{
  "schema_version": "harness.evidence.v1",
  "id": "EVD-0007",
  "title": "Plectarium finding-map and literal-line-break correction",
  "task": "TASK-0003",
  "recorded_at": "2026-09-15",
  "subject_revision_or_fingerprint": "rejected evidence head 7b17bf076217f4cf53f65ec5acda205fa0dc523e; corrected line-break and metadata successor pending",
  "result": "corrected_pending_repeat_T1_review",
  "fresh_until": null,
  "supersedes": "EVD-0006"
}
---

## Accurate finding map


| Finding | Severity | Accurate meaning |
|---|---|---|
| CRA-01 | P1 | Default test dependency regression |
| CRA-02 | P1 | Unsafe Git environment, configuration, and object effects |
| CRA-03 | P2 | Lexical path validation before resolution |
| CRA-07 | P2 | Review-record meaning and actor mapping must distinguish the read-only reviewer, repository recorder, and transition owner |

Navigation normalization was an additional improvement, not CRA-03. CRA-11
and CRA-12 are new P3 metadata and literal-format corrections; they do not
replace or lower the original CRA-07 P2 meaning.

## Literal-format correction

The active migration task and the three current README/dossier/current-state
routing banners contained literal backslash-plus-`n` bytes where Markdown
line breaks were intended. Those exact current files now contain real newline
bytes. A repository-wide current-navigation scan confirms no literal
backslash-`n` or backslash-`n>` sequence remains.

## Roles and lifecycle

The read-only reviewer role, T2 recorder `/root/input_resolver`, and primary
integrator `/root` remain distinct. The migration task stays in `review`;
repeat T1 review and serial fast-forward integration remain pending. No prior
review, evidence, or event byte was rewritten.

## Scope and validation

No implementation source, validator, test, configuration, packet integrity, or
provenance changed. After these metadata/format records freeze, designated
harness integrity is refreshed and the plain 15-test suite, isolated 10-test
pin suite, full harness/packet checks, diff checks, and literal-escape scan are
rerun. No external effect occurred.
