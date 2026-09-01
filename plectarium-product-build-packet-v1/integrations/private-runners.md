# Private Runner Integration

Private runners use tenant-scoped authenticated outbound control connections
where practical, advertise exact distributions and profiles, and accept only
expiring fenced leases. Network placement, customer ownership, or attestation
does not grant plan permission.

Credential values remain at the customer/broker boundary. Heartbeat and logs
are bounded, redacted, and correlated. Loss of connectivity creates an explicit
unknown/reconciling state rather than an assumed failure or cancellation.
