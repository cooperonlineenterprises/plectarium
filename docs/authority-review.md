# PLEC-FND-001 authority review

Candidate prepared September 25, 2026 against suite baseline c4c2cc4 and the
unchanged product packet 1.0.0. This report is evidence for the current local
continuation request, not an operating permission channel. Independent review
and exact command evidence belong to TASK-0004.

## Concept ownership

| Concept | Owner and source | Suite boundary |
| --- | --- | --- |
| Family identity, provisional manifest/result/permission/completion schemas | External family commit and source lock | Consume exact bytes; no schema copies or stabilization |
| Capability domain inputs, plans, findings and conclusions | Independent capability repositories | Preserve opaque payload and qualified schema identity |
| Tenants, principals, catalog, policy decisions, jobs and runners | Suite Charter, invariants and normative schemas | Suite contracts only; no specialist algorithms |
| Artifacts, lineage, compatibility and exact suite BOM | Suite contracts | Checksum, signature, trust, freshness and support stay separate |
| Authentication, host approval, credentials and real execution | Accepted external host/provider authority | No default authorization and no authority from documents/results |
| Workspace paths and repository discovery | Plectarium workspace catalog | Navigation only; no child state ownership |
| Octon governance | Octon owner | Integration does not transfer governance or create dependency |

Charter and invariants take precedence over normative specifications/schemas,
accepted ADRs, release gates, workstreams and packet tasks. Live repository
tasks bind the current request; packet task status remains planning metadata.

## Immutable source

The existing lock names family commit
`0b6c476682e416bd4fb770622c56758f5a380f09`, packet 1.2.0, manifest digest
`54116db0e4f518ffe793df3d3ebd2b87064f00aab10b373bf1909f9126b24867`, and
ledger digest `e0134782dff26755d450f2aa2117d4a8d8afebbf53578e51c9dbbb809fabf4ee`.
The packet check reads exact local Git objects, verifies the expected origin
and standalone root, and compares each of the six named contract digests.
Family HEAD need not equal the pinned commit. Later family documentation or
product changes do not silently update this consumption profile.

The source-lock and its hashes are unchanged. No network fetch is performed.
Local existence and digest equality do not establish signer trust, current
remote equality, supported capability versions, or mature contract stability.

## Explicit assumptions and remaining questions

- OQ-001: any first implementation module name is internal, not a finalized
  public namespace. No public package or stable CLI claim is made.
- OQ-002/003: authorization providers and storage/queue technologies remain
  provider-neutral. Foundational contracts must accept explicit context; they
  cannot fabricate authenticated principals or run services.
- OQ-004: signature/attestation mode policy is open. Checksum success cannot
  become a trust claim; absent/not-checked status stays visible.
- OQ-005/006: no invented retention, residency, legal or performance defaults.
- OQ-007: air-gap execution/bootstrap remains gated; schema validation alone
  does not close the transfer or trust contract.
- OQ-008: supported suite BOM remains unassessed until actual artifacts and
  conformance evidence exist. Synthetic fixtures never promote compatibility.
- The foundation validator currently prohibits product roots. The first
  implementation task must adopt a narrow internal source layout through a
  successor decision and retain packet, family-fork, path and integrity checks.
- Canonical content encoding is not specified by a wire algorithm in the
  current packet. The next task must document a versioned internal encoding
  and its number/string constraints before assigning product content identity;
  it must not imply interoperability with a different canonicalization scheme.
- Current schemas prove shape, not cross-record authorization, permission
  subset, fencing, lifecycle, tenant isolation or digest/byte correspondence.
  Their owning S1 tasks must implement and falsify those semantic checks.

No hidden contradiction has been resolved by implementation convenience. The
above open questions permit a bounded contract layer under their documented
limits; they do not permit a real control-plane run or release.
