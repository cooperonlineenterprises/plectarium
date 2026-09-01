# Validation

A passing structural check proves only its stated scope. It does not prove
business, legal, privacy, security, accessibility, operational, or production
readiness.

Project-specific setup validation consists of:

1. read-only harness/dossier structural validation;
2. harness mutation/acceptance tests;
3. packet schema, fixture, graph, decision, claim, manifest, and checksum validation;
4. an explicit packet-derived refresh followed by a read-only packet check;
5. a later designated root-integrity refresh and final read-only harness check.

Product code, runtime, security, SLO, and release gates remain unassessed.
