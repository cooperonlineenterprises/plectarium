"""Explicit offline schemas and bounded internal content identities.

No schema lookup fetches a URL. No version resolution selects a substitute.
Validated documents do not establish permission or cross-record semantics.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import re
from typing import Any, Callable, Mapping
from urllib.parse import urldefrag, urljoin, urlsplit

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource
from referencing.jsonschema import DRAFT202012

CANONICAL_VERSION = "plectarium.canonical-json.v1"
MAX_INTEGER = 2**53 - 1
DRAFT = "https://json-schema.org/draft/2020-12/schema"


class ContractError(ValueError):
    """A bounded refusal, with no input values included in diagnostics."""


@dataclass(frozen=True)
class Limits:
    max_bytes: int = 1_048_576
    max_depth: int = 64
    max_nodes: int = 100_000

    def __post_init__(self) -> None:
        if any(type(v) is not int or v < 1 for v in
               (self.max_bytes, self.max_depth, self.max_nodes)):
            raise ContractError("limits must be positive integers")


def _text(data: bytes | str, limits: Limits) -> str:
    try:
        raw = data.encode("utf-8") if type(data) is str else data
        if type(raw) is not bytes or len(raw) > limits.max_bytes:
            raise ContractError("input type or byte limit rejected")
        return raw.decode("utf-8")
    except UnicodeError as exc:
        raise ContractError("input is not valid UTF-8") from None


def _check(value: Any, limits: Limits, *, canonical: bool = False) -> None:
    count = 0
    encoded_size = 0
    active: set[int] = set()

    def visit(item: Any, depth: int) -> None:
        nonlocal count, encoded_size
        count += 1
        if count > limits.max_nodes or depth > limits.max_depth:
            raise ContractError("document structure limit exceeded")
        kind = type(item)
        if kind is str:
            if len(item) > limits.max_bytes:
                raise ContractError("document byte limit exceeded")
            try:
                encoded_size += len(json.dumps(item, ensure_ascii=False).encode("utf-8"))
            except UnicodeError as exc:
                raise ContractError("string contains an invalid Unicode scalar") from None
        elif item is None or kind is bool:
            encoded_size += 4 if item is None or item is True else 5
        elif kind is int:
            if canonical and abs(item) > MAX_INTEGER:
                raise ContractError("integer exceeds the canonical profile")
            try:
                encoded_size += len(str(item))
            except ValueError as exc:
                raise ContractError("integer length limit exceeded") from None
        elif kind is float:
            if canonical or not math.isfinite(item):
                raise ContractError("number is unsupported by this encoding")
            encoded_size += len(json.dumps(item))
        elif kind in (dict, list):
            if id(item) in active:
                raise ContractError("cyclic documents are rejected")
            active.add(id(item))
            encoded_size += 2 + max(0, len(item) - 1)
            if kind is dict:
                encoded_size += len(item)
                for key, child in item.items():
                    if type(key) is not str:
                        raise ContractError("object keys must be strings")
                    visit(key, depth + 1)
                    visit(child, depth + 1)
            else:
                for child in item:
                    visit(child, depth + 1)
            active.remove(id(item))
        else:
            raise ContractError("non-JSON value rejected")
        if encoded_size > limits.max_bytes:
            raise ContractError("document byte limit exceeded")

    visit(value, 0)


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ContractError("duplicate object key")
        result[key] = value
    return result


def _constant(_: str) -> None:
    raise ContractError("nonfinite JSON number rejected")


def parse_json(data: bytes | str, *, limits: Limits = Limits()) -> Any:
    try:
        value = json.loads(_text(data, limits), object_pairs_hook=_pairs,
                           parse_constant=_constant)
        _check(value, limits)
        return value
    except ContractError:
        raise
    except (ValueError, RecursionError) as exc:
        raise ContractError("malformed or excessively nested JSON") from None


class _YamlLoader(yaml.SafeLoader):
    def compose_node(self, parent: Any, index: Any) -> Any:
        event = self.peek_event()
        if isinstance(event, yaml.AliasEvent) or getattr(event, "anchor", None):
            raise ContractError("YAML aliases and anchors are rejected")
        return super().compose_node(parent, index)


# Remove YAML 1.1's implicit dates, yes/no booleans, octal and nonfinite numbers.
_YamlLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in resolvers if tag not in {
        "tag:yaml.org,2002:timestamp", "tag:yaml.org,2002:bool",
        "tag:yaml.org,2002:int", "tag:yaml.org,2002:float",
    }] for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
_YamlLoader.add_implicit_resolver("tag:yaml.org,2002:bool", re.compile(r"^(true|false)$"), list("tf"))
_YamlLoader.add_implicit_resolver("tag:yaml.org,2002:int", re.compile(r"^-?(0|[1-9][0-9]*)$"), list("-0123456789"))
_YamlLoader.add_implicit_resolver("tag:yaml.org,2002:float", re.compile(
    r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+(?:[eE][+-]?[0-9]+)?|[eE][+-]?[0-9]+)$"), list("-0123456789"))


def _yaml_mapping(loader: _YamlLoader, node: Any) -> dict[str, Any]:
    pairs = []
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if type(key) is not str or key == "<<":
            raise ContractError("YAML mapping key rejected")
        pairs.append((key, loader.construct_object(value_node, deep=True)))
    return _pairs(pairs)


_YamlLoader.add_constructor("tag:yaml.org,2002:map", _yaml_mapping)


def parse_yaml(data: bytes | str, *, limits: Limits = Limits()) -> Any:
    try:
        value = yaml.load(_text(data, limits), Loader=_YamlLoader)
        _check(value, limits)
        return value
    except ContractError:
        raise
    except (yaml.YAMLError, ValueError, TypeError, RecursionError) as exc:
        raise ContractError("malformed or unsupported YAML") from None


def canonical_bytes(value: Any, *, limits: Limits = Limits()) -> bytes:
    _check(value, limits, canonical=True)
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True,
                         separators=(",", ":"), allow_nan=False).encode("utf-8")
    if len(encoded) > limits.max_bytes:
        raise ContractError("canonical byte limit exceeded")
    return encoded


def content_digest(data: bytes) -> str:
    """Hash exact bytes, including opaque external payloads, without interpretation."""
    if type(data) is not bytes:
        raise ContractError("digest input must be exact bytes")
    return "sha256:" + hashlib.sha256(data).hexdigest()


def _no_retrieval(uri: str) -> Resource:
    raise NoSuchResource(ref=uri)


@dataclass(frozen=True)
class Receipt:
    schema_id: str
    schema_digest: str
    encoding: str
    content_digest: str
    canonical: bytes
    authority_effect: str = "none"


class SchemaRegistry:
    """An immutable snapshot of caller-supplied, digest-pinned schema bytes."""

    def __init__(self, schemas: Mapping[str, bytes], *,
                 expected_digests: Mapping[str, str], limits: Limits = Limits()):
        if not schemas or set(schemas) != set(expected_digests):
            raise ContractError("every schema requires one exact digest pin")
        self._limits = limits
        self._format_checker = FormatChecker()
        self._schemas: dict[str, Any] = {}
        self._digests: dict[str, str] = {}
        self._versions: dict[str, str] = {}
        self._migrations: dict[tuple[str, str], Callable[[Any], Any]] = {}
        for schema_id, data in schemas.items():
            if type(schema_id) is not str:
                raise ContractError("schema identity must be a string")
            if content_digest(data) != expected_digests[schema_id]:
                raise ContractError("schema content differs from its pin")
            value = parse_json(data, limits=limits)
            if (type(value) is not dict or value.get("$id") != schema_id or
                    not urlsplit(schema_id).scheme or urldefrag(schema_id)[1] or
                    value.get("$schema") != DRAFT):
                raise ContractError("schema identity or dialect rejected")
            try:
                Draft202012Validator.check_schema(value)
            except Exception as exc:
                raise ContractError("invalid schema definition") from None
            self._schemas[schema_id] = value
            self._digests[schema_id] = expected_digests[schema_id]
            version_rule = value.get("properties", {}).get("schema_version")
            version = version_rule.get("const") if type(version_rule) is dict else None
            if version is not None:
                if type(version) is not str or version in self._versions:
                    raise ContractError("duplicate or malformed document version")
                self._versions[version] = schema_id
        self._registry = Registry(retrieve=_no_retrieval).with_resources(
            (key, Resource.from_contents(value)) for key, value in self._schemas.items())
        for schema_id, value in self._schemas.items():
            self._check_references(value, schema_id)

    @classmethod
    def from_directory(cls, directory: Path, *, expected_digests: Mapping[str, str],
                       limits: Limits = Limits()) -> SchemaRegistry:
        directory = Path(directory).absolute()
        if any(path.is_symlink() for path in (directory, *directory.parents)):
            raise ContractError("schema directory has a symlink component")
        values: dict[str, bytes] = {}
        for path in sorted(directory.glob("*.schema.json")):
            if path.is_symlink() or not path.is_file() or path.stat().st_size > limits.max_bytes:
                raise ContractError("unsafe schema file")
            data = path.read_bytes()
            value = parse_json(data, limits=limits)
            schema_id = value.get("$id") if type(value) is dict else None
            if type(schema_id) is not str or schema_id in values:
                raise ContractError("schema file identity is missing or duplicated")
            values[schema_id] = data
        return cls(values, expected_digests=expected_digests, limits=limits)

    def _check_references(self, value: Any, base: str, *, root: bool = True,
                          seen: set[tuple[str, int]] | None = None) -> None:
        if type(value) is bool:
            return
        if type(value) is not dict:
            raise ContractError("reference target is not a schema")
        seen = set() if seen is None else seen
        key = (base, id(value))
        if key in seen:
            return
        seen.add(key)
        if type(value) is dict:
            if "format" in value and (type(value["format"]) is not str or
                    value["format"] not in self._format_checker.checkers):
                raise ContractError("declared schema format is unavailable in this runtime")
            if "$schema" in value and value["$schema"] != DRAFT:
                raise ContractError("nested schema dialect is unsupported")
            if not root and "$id" in value:
                raise ContractError("nested schema identities require a future profile")
            if "$dynamicRef" in value or "$recursiveRef" in value:
                raise ContractError("dynamic schema references are unsupported")
            if "$ref" in value:
                ref = value["$ref"]
                if type(ref) is not str:
                    raise ContractError("schema reference is malformed")
                target, fragment = urldefrag(urljoin(base, ref))
                if target not in self._schemas:
                    raise ContractError("schema reference is outside the pinned registry")
                if fragment and not fragment.startswith("/"):
                    raise ContractError("schema reference anchors are unsupported")
                try:
                    resolved = self._registry.resolver(base_uri=base).lookup(ref)
                except Exception as exc:
                    raise ContractError("schema reference does not resolve") from None
                try:
                    Draft202012Validator.check_schema(resolved.contents)
                except Exception:
                    raise ContractError("reference target is not a valid schema") from None
                # A pointer can explicitly turn annotation data into a schema.
                # Validate that target too; memoization permits reference cycles.
                self._check_references(resolved.contents, target,
                                       root=not bool(fragment), seen=seen)
            # Use the pinned specification's schema-bearing locations. Defaults,
            # examples, const/enum values and property-map keys are literal data.
            try:
                children = list(Resource.from_contents(
                    value, default_specification=DRAFT202012).subresources())
            except Exception:
                raise ContractError("schema subtree or dialect is unsupported") from None
            for child in children:
                self._check_references(child.contents, base, root=False, seen=seen)

    def schema_for_version(self, version: str) -> str:
        try:
            return self._versions[version]
        except (KeyError, TypeError) as exc:
            raise ContractError("unknown exact document version") from None

    def validate(self, value: Any, *, schema_id: str | None = None) -> None:
        _check(value, self._limits)
        if schema_id is None:
            if type(value) is not dict:
                raise ContractError("document version is required")
            schema_id = self.schema_for_version(value.get("schema_version"))
        if type(schema_id) is not str or schema_id not in self._schemas:
            raise ContractError("unknown exact schema identity")
        validator = Draft202012Validator(self._schemas[schema_id], registry=self._registry,
                                         format_checker=self._format_checker)
        try:
            error = next(validator.iter_errors(value), None)
        except Exception as exc:
            raise ContractError("schema evaluation failed") from None
        if error is not None:
            raise ContractError("document violates pinned schema constraint: " + str(error.validator))

    def receipt(self, value: Any, *, schema_id: str | None = None) -> Receipt:
        self.validate(value, schema_id=schema_id)
        schema_id = schema_id or self.schema_for_version(value["schema_version"])
        data = canonical_bytes(value, limits=self._limits)
        return Receipt(schema_id, self._digests[schema_id], CANONICAL_VERSION,
                       content_digest(data), data)

    def register_migration(self, source: str, target: str,
                           transform: Callable[[Any], Any]) -> None:
        self.schema_for_version(source)
        self.schema_for_version(target)
        key = (source, target)
        if source == target or key in self._migrations or not callable(transform):
            raise ContractError("migration registration rejected")
        self._migrations[key] = transform

    def migrate(self, value: Any, target: str) -> Any:
        self.validate(value)
        source = value["schema_version"]
        self.schema_for_version(target)
        if source == target:
            return parse_json(canonical_bytes(value, limits=self._limits), limits=self._limits)
        transform = self._migrations.get((source, target))
        if transform is None:
            raise ContractError("no explicitly registered migration")
        supplied = parse_json(canonical_bytes(value, limits=self._limits), limits=self._limits)
        try:
            result = transform(supplied)
        except Exception as exc:
            raise ContractError("explicit migration failed") from None
        self.validate(result, schema_id=self.schema_for_version(target))
        return parse_json(canonical_bytes(result, limits=self._limits), limits=self._limits)
