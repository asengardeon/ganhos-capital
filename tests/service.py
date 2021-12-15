import json
import unittest

from source.capital.service.process_capital import ProcessCapital


class ServiceTestCase(unittest.TestCase):

    def test_simple(self):
        json_value = '[{	"operation": "buy",	"unit-cost": 10,	"quantity": 10000}, {	"operation": "sell",	"unit-cost": 20,	"quantity": 5000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)


    def test_two_taxes(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 10000}, {"operation":"sell", "unit-cost":20, "quantity": 5000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 10000)

    def test_three_taxes(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 10000},{"operation":"sell", "unit-cost":20, "quantity": 5000},{"operation":"sell", "unit-cost":5, "quantity":5000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 10000)
        self.assertEqual(result[2]['tax'], 0)

    def test_three_taxes_2(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 10000},{"operation":"sell", "unit-cost":20, "quantity": 5000},{"operation":"sell", "unit-cost":5, "quantity":5000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 0)
        self.assertEqual(result[2]['tax'], 5000)


    def test_three_taxes_zero(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 10000},{"operation":"buy","unit-cost":25, "quantity": 5000},{"operation":"sell", "unit-cost":15,"quantity": 10000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 0)
        self.assertEqual(result[2]['tax'], 0)


    def test_four_taxes(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 10000},{"operation":"buy","unit-cost":25, "quantity": 5000},{"operation":"sell", "unit-cost":15,"quantity": 10000},{"operation":"sell", "unit-cost":25, "quantity": 5000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 0)
        self.assertEqual(result[2]['tax'], 0)
        self.assertEqual(result[3]['tax'], 10000)


    def test_five_taxes(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 10000},{"operation":"sell","unit-cost":2, "quantity": 5000},{"operation":"sell", "unit-cost":20, "quantity":2000},{"operation":"sell", "unit-cost":20, "quantity": 2000},{"operation":"sell","unit-cost":25, "quantity": 1000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 0)
        self.assertEqual(result[2]['tax'], 0)
        self.assertEqual(result[3]['tax'], 3000)

