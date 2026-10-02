from copy import deepcopy
from pathlib import Path
import unittest

from reference.tsm_pilot.contracts import ContractError, loads, validate


class SchemaFixtures(unittest.TestCase):
    def test_profile_fixtures(self):
        directory = Path(__file__).resolve().parents[1] / "schemas/fixtures"
        manifest = loads((directory / "cases.json").read_text(encoding="utf-8"))
        base = loads((directory / manifest["base"]).read_text(encoding="utf-8"))
        for case in manifest["cases"]:
            with self.subTest(case=case["name"]):
                record = deepcopy(base)
                for change in case["changes"]:
                    target = record
                    for part in change["path"][:-1]:
                        target = target[part]
                    target[change["path"][-1]] = change["value"]
                if case["valid"]:
                    validate(record)
                else:
                    with self.assertRaises(ContractError):
                        validate(record)
