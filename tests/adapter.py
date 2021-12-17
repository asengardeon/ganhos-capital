import unittest

from capital.adapter.json_adapter import JsonAdapter


class AdapterJSONTestcCase(unittest.TestCase):
    def test_execute(self):
        json = '[{	"operation": "buy",	"unit-cost": 10,	"quantity": 10000}, {	"operation": "sell",	"unit-cost": 20,	"quantity": 5000}]'
        adapter = JsonAdapter()
        result = adapter.json_to_unit_list(json)
        self.assertEqual(len(result), 2)
