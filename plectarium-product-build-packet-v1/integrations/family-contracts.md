# Family Contract Integration

Use the explicit immutable source lock. An implementation pipeline receives the
pinned family checkout or artifact as an input, verifies the lock, and validates
family documents against those external schemas. It does not fetch a branch
silently and does not vendor a mutable copy.

Suite wrappers add tenant, catalog, verification, retention, and access
metadata around the untouched family document. Contract mismatch is
`incompatible` or quarantined, never coerced.
