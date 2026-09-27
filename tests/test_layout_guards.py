"""The implementation transition retains the packet's source confinement."""

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "suite_packet_layout_test", ROOT / "plectarium-product-build-packet-v1/scripts/validate-packet.py")
packet = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = packet
spec.loader.exec_module(packet)


class LayoutTests(unittest.TestCase):
    def test_only_adopted_python_package_is_allowed(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);source=root/'src/plectarium_contracts';source.mkdir(parents=True)
            (source/'contracts.py').write_text('"""Internal contract source."""\n')
            with patch.object(packet,'REPO',root):
                self.assertFalse([f for f in packet.check_files() if f.code.startswith('implementation')])
                (root/'src/rogue.py').write_text('pass\n')
                self.assertIn('implementation.scope',{f.code for f in packet.check_files()})

    def test_broken_source_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'src').symlink_to(root/'missing',target_is_directory=True)
            with patch.object(packet,'REPO',root):
                self.assertIn('implementation.path',{f.code for f in packet.check_files()})

    def test_other_product_roots_and_family_copies_still_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'apps').mkdir();source=root/'src/plectarium_contracts';source.mkdir(parents=True)
            (source/'completion.v0.schema.json').write_text('{}')
            with patch.object(packet,'REPO',root):
                codes={f.code for f in packet.check_files()}
                self.assertIn('implementation.present',codes)
                self.assertIn('implementation.scope',codes)


if __name__=='__main__':unittest.main()
