from __future__ import annotations

from dataclasses import FrozenInstanceError
import json
from pathlib import Path
import sys
import tempfile
import traceback
import unittest
from unittest.mock import patch
from jsonschema import FormatChecker

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from plectarium_contracts import (
    ContractError, Limits, SchemaRegistry, canonical_bytes, content_digest,
    parse_json, parse_yaml,
)

PACKET = ROOT / "plectarium-product-build-packet-v1"
SCHEMAS = PACKET / "spec/schemas"


def registry_from(values):
    bodies = {v["$id"]: json.dumps(v).encode() for v in values}
    return SchemaRegistry(bodies, expected_digests={k:content_digest(v) for k,v in bodies.items()})


def version_schema(version):
    return {"$schema":"https://json-schema.org/draft/2020-12/schema",
            "$id":f"https://example.invalid/{version}", "type":"object",
            "required":["schema_version","count"], "additionalProperties":False,
            "properties":{"schema_version":{"const":version},"count":{"type":"integer"}}}


class ParsingTests(unittest.TestCase):
    def test_duplicate_and_escaped_keys(self):
        for value in [b'{"a":1,"a":2}', b'{"a":1,"\\u0061":2}', b'{"n":{"x":1,"x":2}}']:
            with self.subTest(value=value), self.assertRaises(ContractError):parse_json(value)

    def test_invalid_json_unicode_and_nonfinite(self):
        for value in [b'{',b'null null',b'\xff',b'NaN',b'Infinity',b'1e999',b'"\\ud800"']:
            with self.subTest(value=value), self.assertRaises(ContractError):parse_json(value)

    def test_structure_and_byte_bounds(self):
        with self.assertRaises(ContractError):parse_json(b'"12345"',limits=Limits(max_bytes=3))
        with self.assertRaises(ContractError):parse_json(b'[[[[0]]]]',limits=Limits(max_depth=2))
        with self.assertRaises(ContractError):parse_yaml('a: [1, 2, 3]',limits=Limits(max_nodes=3))
        with self.assertRaises(ContractError):Limits(max_bytes=True)

    def test_yaml_json_equivalence_and_scalar_profile(self):
        self.assertEqual(parse_yaml('a: true\nb: 12\nc: null\nd: 1.5'),
                         parse_json('{"a":true,"b":12,"c":null,"d":1.5}'))
        self.assertEqual(parse_yaml('a: yes\nb: 012\nc: 2026-09-25'),
                         {'a':'yes','b':'012','c':'2026-09-25'})

    def test_yaml_ambiguity_and_unsafe_tags(self):
        for text in ['a: 1\na: 2','a: &x [1]\nb: *x','a: {<<: {b: 1}}',
                     '1: value','a: !!python/object:thing {}','a: !!float .nan',
                     '---\na: 1\n---\na: 2']:
            with self.subTest(text=text),self.assertRaises(ContractError):parse_yaml(text)

    def test_canonical_known_vector_and_roundtrip(self):
        expected='{"a":[null,true,2],"é":"kept"}'.encode()
        value={'é':'kept','a':[None,True,2]}
        self.assertEqual(canonical_bytes(value),expected)
        self.assertEqual(canonical_bytes(parse_json(expected)),expected)
        self.assertEqual(content_digest(b'abc'),'sha256:ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')
        self.assertNotEqual(content_digest(expected),content_digest(expected+b'\n'))

    def test_canonical_rejects_unsupported_values_and_preserves_unicode(self):
        cycle=[];cycle.append(cycle)
        for value in [1.0,2**53,{1:'bad'},b'bytes',cycle,'\ud800']:
            with self.subTest(kind=type(value)),self.assertRaises(ContractError):canonical_bytes(value)
        self.assertNotEqual(canonical_bytes('é'),canonical_bytes('e\u0301'))
        with self.assertRaises(ContractError):canonical_bytes('abc',limits=Limits(max_bytes=2))


class RegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bodies={parse_json(p.read_bytes())['$id']:p.read_bytes() for p in SCHEMAS.glob('*.json')}
        cls.pins={k:content_digest(v) for k,v in bodies.items()}
        cls.registry=SchemaRegistry.from_directory(SCHEMAS,expected_digests=cls.pins)

    def test_packet_structural_fixture_corpus(self):
        index=parse_yaml((PACKET/'fixtures/index.yaml').read_bytes())
        for item in index['fixtures']:
            schema=parse_json((SCHEMAS/item['schema']).read_bytes())['$id']
            value=parse_json((PACKET/'fixtures'/item['path']).read_bytes())
            with self.subTest(path=item['path']):
                # Permission subset is a semantic policy rule, not JSON Schema shape.
                if item['expected_valid'] or item.get('semantic_checks'):
                    self.registry.validate(value,schema_id=schema)
                else:
                    with self.assertRaises(ContractError):self.registry.validate(value,schema_id=schema)

    def test_unknown_versions_and_ids_do_not_fallback(self):
        for value in [{},{'schema_version':'plectarium.job.v99'},{'schema_version':[]}]:
            with self.assertRaises(ContractError):self.registry.validate(value)
        with self.assertRaises(ContractError):self.registry.validate({},schema_id='https://other.invalid/schema')
        with self.assertRaises(ContractError):self.registry.validate({},schema_id=[])

    def test_in_memory_validation_cannot_bypass_size_limits(self):
        schema=version_schema('one');data=json.dumps(schema).encode()
        r=SchemaRegistry({schema['$id']:data},expected_digests={schema['$id']:content_digest(data)},limits=Limits(max_bytes=1024))
        with self.assertRaises(ContractError):r.validate({'schema_version':'one','count':'x'*1025})

    def test_receipt_is_immutable_and_bound_to_exact_schema_and_bytes(self):
        value=parse_json((PACKET/'fixtures/schema/job.valid.json').read_bytes())
        receipt=self.registry.receipt(value)
        self.assertEqual(receipt.schema_digest,self.pins[receipt.schema_id])
        self.assertEqual(receipt.authority_effect,'none')
        self.assertEqual(receipt.content_digest,content_digest(receipt.canonical))
        value['revision']+=1
        self.assertNotEqual(self.registry.receipt(value).content_digest,receipt.content_digest)
        with self.assertRaises(FrozenInstanceError):receipt.authority_effect='approved'

    def test_pin_and_duplicate_identity_refusals(self):
        schema=version_schema('one');data=json.dumps(schema).encode()
        with self.assertRaises(ContractError):SchemaRegistry({schema['$id']:data},expected_digests={schema['$id']:'sha256:'+'0'*64})
        with self.assertRaises(ContractError):SchemaRegistry({schema['$id']:data},expected_digests={})
        other=dict(schema,**{'$id':'https://example.invalid/other'})
        with self.assertRaises(ContractError):registry_from([schema,other])

    def test_missing_external_and_fragment_refs_never_use_network(self):
        for ref in ['https://example.com/unpinned','missing.json','#/$defs/missing']:
            schema=version_schema('one');schema['properties']['count']={'$ref':ref}
            with patch('urllib.request.urlopen',side_effect=AssertionError('network')) as network:
                with self.assertRaises(ContractError):registry_from([schema])
                network.assert_not_called()

    def test_nested_identity_and_unknown_dialect_are_rejected(self):
        schema=version_schema('one');schema['properties']['count']['$id']='https://example.invalid/nested'
        with self.assertRaises(ContractError):registry_from([schema])
        schema=version_schema('one');schema['$schema']='https://unknown.invalid/draft'
        with self.assertRaises(ContractError):registry_from([schema])

    def test_registered_schema_bytes_are_an_immutable_snapshot(self):
        schema=version_schema('one');r=registry_from([schema]);schema['properties']['count']={'type':'string'}
        r.validate({'schema_version':'one','count':3})
        with self.assertRaises(ContractError):r.validate({'schema_version':'one','count':'3'})

    def test_directory_symlink_and_changed_bytes_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            base=Path(temp).resolve();schema=version_schema('one');data=json.dumps(schema).encode()
            pins={schema['$id']:content_digest(data)}
            (base/'one.schema.json').write_bytes(data)
            SchemaRegistry.from_directory(base,expected_digests=pins).validate({'schema_version':'one','count':1})
            (base/'one.schema.json').write_bytes(data+b' ')
            with self.assertRaises(ContractError):SchemaRegistry.from_directory(base,expected_digests=pins)
            (base/'one.schema.json').unlink();(base/'one.schema.json').symlink_to(SCHEMAS/'job.schema.json')
            with self.assertRaises(ContractError):SchemaRegistry.from_directory(base,expected_digests=pins)

    def test_explicit_migration_is_validated_and_does_not_mutate_source(self):
        r=registry_from([version_schema('one'),version_schema('two')]);value={'schema_version':'one','count':2}
        with self.assertRaises(ContractError):r.migrate(value,'two')
        r.register_migration('one','two',lambda v:dict(v,schema_version='two',count=v['count']+1))
        self.assertEqual(r.migrate(value,'two'),{'schema_version':'two','count':3})
        self.assertEqual(value,{'schema_version':'one','count':2})
        with self.assertRaises(ContractError):r.migrate(value,'three')
        with self.assertRaises(ContractError):r.register_migration('one','two',lambda v:v)

    def test_bad_migration_result_is_rejected(self):
        r=registry_from([version_schema('one'),version_schema('two')])
        r.register_migration('one','two',lambda v:dict(v,count='wrong'))
        with self.assertRaises(ContractError):r.migrate({'schema_version':'one','count':1},'two')

    def test_schema_diagnostics_do_not_echo_input_values(self):
        r=registry_from([version_schema('one')])
        with self.assertRaises(ContractError) as caught:r.validate({'schema_version':'one','count':'private-value'})
        self.assertNotIn('private-value',str(caught.exception))

    def test_nested_dialect_changes_are_rejected_before_receipts(self):
        for placement in ('allOf','$defs'):
            for dialect in ('http://json-schema.org/draft-07/schema#','https://unknown.invalid/draft'):
                child={'$schema':dialect,'type':'object','unevaluatedProperties':False}
                schema=version_schema('one')
                if placement=='allOf':schema['allOf']=[child]
                else:
                    schema['$defs']={'changed':child}
                    schema['allOf']=[{'$ref':'#/$defs/changed'}]
                with self.subTest(placement=placement,dialect=dialect),self.assertRaises(ContractError):registry_from([schema])

    def test_literals_and_property_names_are_not_schema_instructions(self):
        schema=version_schema('one')
        literal={'$ref':'https://not-registered.invalid/value','$id':'literal','$schema':'literal'}
        schema['default']=literal
        schema['examples']=[literal]
        schema['properties'].update({'$id':{'type':'string'},'$ref':{'type':'string'},
                                     'literal':{'const':literal},'choice':{'enum':[literal]}})
        r=registry_from([schema])
        value={'schema_version':'one','count':1,'$id':'value','$ref':'value',
               'literal':literal,'choice':literal}
        r.validate(value)
        self.assertEqual(parse_json(r.receipt(value).canonical),value)

    def test_referenced_annotation_targets_cannot_switch_dialect(self):
        hidden={'$schema':'http://json-schema.org/draft-07/schema#',
                'type':'object','unevaluatedProperties':False}
        for pointer in ('#/default/hidden','#/examples/0'):
            schema=version_schema('one')
            schema['default']={'hidden':hidden};schema['examples']=[hidden]
            schema['properties']['value']={'$ref':pointer}
            with self.subTest(pointer=pointer),self.assertRaises(ContractError):registry_from([schema])

    def test_supported_annotation_targets_validate_and_reject_scalars(self):
        schema=version_schema('one')
        schema['default']={'hidden':{'type':'object','unevaluatedProperties':False}}
        schema['properties']['value']={'$ref':'#/default/hidden'}
        r=registry_from([schema])
        r.receipt({'schema_version':'one','count':1,'value':{}})
        with self.assertRaises(ContractError):r.receipt({'schema_version':'one','count':1,'value':{'extra':1}})
        schema['default']['hidden']=42
        with self.assertRaises(ContractError):registry_from([schema])
        schema['default']['hidden']={'type':'not-a-json-schema-type'}
        with self.assertRaises(ContractError):registry_from([schema])

    def test_recursive_references_are_checked_without_preflight_recursion(self):
        schema=version_schema('one')
        schema['$defs']={'node':{'anyOf':[{'type':'null'},
            {'type':'array','items':{'$ref':'#/$defs/node'}}]}}
        schema['properties']['value']={'$ref':'#/$defs/node'}
        r=registry_from([schema])
        r.receipt({'schema_version':'one','count':1,'value':[None,[None]]})
        with self.assertRaises(ContractError):r.validate({'schema_version':'one','count':1,'value':[7]})

    def test_boolean_version_subschemas_use_only_explicit_schema_identity(self):
        for rule in (True,False):
            schema=version_schema('one');schema['properties']['schema_version']=rule
            schema['required']=['count']
            r=registry_from([schema])
            self.assertEqual(r.receipt({'count':1},schema_id=schema['$id']).authority_effect,'none')
            with self.assertRaises(ContractError):r.schema_for_version('one')
            if rule:r.validate({'schema_version':'unregistered','count':1},schema_id=schema['$id'])
            else:
                with self.assertRaises(ContractError):r.validate({'schema_version':'one','count':1},schema_id=schema['$id'])

    def test_complete_exception_chains_do_not_disclose_input_values(self):
        marker='PRIVATE'+'_'+'PROBE_MARKER'
        schema=version_schema('one');schema['type']=marker
        r=registry_from([version_schema('one'),version_schema('two')])
        def failed_migration(value):raise ValueError(marker)
        r.register_migration('one','two',failed_migration)
        invalid_yaml='private: !unknown '+marker
        operations=[lambda:parse_yaml(invalid_yaml),lambda:registry_from([schema]),
                    lambda:r.migrate({'schema_version':'one','count':1},'two')]
        for operation in operations:
            try:operation()
            except ContractError as exc:
                self.assertNotIn(marker,''.join(traceback.format_exception(exc)))
                self.assertTrue(exc.__suppress_context__)
            else:self.fail('expected a bounded refusal')

    def test_declared_formats_fail_closed_when_unavailable(self):
        schema=version_schema('one')
        schema['properties']['timestamp']={'type':'string','format':'date-time'}
        with patch.dict(FormatChecker.checkers,{},clear=True):
            with self.assertRaises(ContractError):registry_from([schema])
        schema['properties']['timestamp']['format']='unregistered-format'
        with self.assertRaises(ContractError):registry_from([schema])

    def test_timestamp_formats_are_enforced_for_validation_and_receipts(self):
        value=parse_json((PACKET/'fixtures/schema/job.valid.json').read_bytes())
        self.registry.receipt(value)
        for stamp in ('not-a-date','2026-02-30T12:00:00Z','2026-09-25T12:00:00',
                      '2026-09-25T25:00:00Z'):
            with self.subTest(stamp=stamp):
                malformed=dict(value,created_at=stamp)
                with self.assertRaises(ContractError):self.registry.validate(malformed)
                with self.assertRaises(ContractError):self.registry.receipt(malformed)


if __name__=='__main__':unittest.main()
