---
{
  "schema_version": "harness.checkpoint.v1",
  "id": "CHK-0002",
  "title": "Plectarium initial-publication and closure-candidate checkpoint",
  "created_at": "2026-08-31",
  "task": "TASK-0002",
  "source_revision_or_fingerprint": "git:8842fe6543d0c63d56a0a34e336192e66f76cae1",
  "supersedes": "CHK-0001",
  "decision_refs": ["DEC-0001", "DEC-0002"],
  "evidence_refs": ["EVD-0002", "EVD-0003"],
  "limitations": ["Cannot attest the later push of the closure commit containing this checkpoint."]
}
---

- Exact remote: `https://github.com/cooperonlineenterprises/plectarium.git`
- Visibility/default branch: private / `main`
- Foundation commit: `8842fe6543d0c63d56a0a34e336192e66f76cae1`
- First-push equality: verified
- Packet manifest SHA-256:
  `d77071033dad0c4a9160bba46d56304c542e021bf47d9202ee6e8fde96b1bf03`
- Packet checksum-ledger SHA-256:
  `76362d8f259986eba1758c5a7aca069b83e33e7cb90cbb3da7a7619d50b88347`

Push the closure commit normally once, then directly verify local, tracking,
and remote equality plus a clean worktree. Do not create a third evidence
commit under this task.
