"""检查交换数据中用于回查的事实。"""
import unittest

import numpy as np

from separator_gaussian_input import load_record


class ExchangeRecordTests(unittest.TestCase):
    def test_exchange_contract(self):
        record = load_record()
        self.assertTrue(record["factors"][0] == record["factors"][1])
        self.assertTrue(record["observations"][0]["mask"] != record["observations"][1]["mask"] and record["observations"][1]["noise"][0][1] != 0)
        self.assertTrue(record["exact"][0]["variable"] == record["exact"][1]["variable"] and record["exact"][0]["value"] != record["exact"][1]["value"])
        self.assertTrue(all(np.min(np.linalg.eigvalsh(f["precision"])) >= -1e-12 for f in record["factors"]))
        self.assertTrue(any(event == ["remove_factor", "common"] for event in record["operations"]) and all(np.allclose(np.sum(f["precision"], axis=1), 0) for f in record["factors"] if f["id"].startswith("link")))
