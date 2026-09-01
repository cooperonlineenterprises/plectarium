# Plan, Approval, and Execution Sequence

```text
requester → catalog: resolve exact coordinate
requester → capability through runner: create plan
runner → artifact store: write immutable plan bytes
control plane → approver: present digest, scope, effects, limits
approver → policy module: approve subset / deny / expire
scheduler → policy/catalog: revalidate all bindings
scheduler → runner: issue fenced lease
runner → capability CLI/OCI: execute accepted plan
runner → artifact store: upload immutable result
result catalog → family contracts: validate identity/completion/provenance
control plane → requester: show control state and capability completion
```

No message in this sequence grants authority beyond the recorded approval.
