#!/usr/bin/env python3
"""Checkout-only structural contract demonstration, not a public suite CLI."""

from dataclasses import asdict
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from plectarium_contracts import ContractError, SchemaRegistry, parse_json


def main() -> int:
    packet = ROOT / "plectarium-product-build-packet-v1"
    manifest = parse_json((packet / "PACKET-MANIFEST.json").read_bytes())
    pins = {}
    for entry in manifest["files"]:
        if entry["path"].startswith("spec/schemas/"):
            schema = parse_json((packet / entry["path"]).read_bytes())
            pins[schema["$id"]] = "sha256:" + entry["sha256"]
    registry = SchemaRegistry.from_directory(packet / "spec/schemas", expected_digests=pins)
    value = parse_json((packet / "fixtures/schema/job.valid.json").read_bytes())
    receipt = registry.receipt(value)
    display = asdict(receipt)
    display["canonical"] = receipt.canonical.decode("utf-8")
    display["limitations"] = ["Structural validation only; job semantics and execution authority are not assessed."]
    print(json.dumps(display, indent=2, ensure_ascii=False))
    changed = dict(value, schema_version="plectarium.job.v99")
    try:
        registry.validate(changed)
    except ContractError:
        print("[PASS] unknown breaking version refused", file=sys.stderr)
    else:
        raise RuntimeError("unknown version unexpectedly accepted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
