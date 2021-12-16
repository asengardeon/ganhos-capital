import json
import unittest

from source.capital.service.process_capital import ProcessCapital


class ServiceTestCase(unittest.TestCase):

    def test_one_buy_two_sell_operation_no_taxes_example(self):
        json_value = '[{	"operation": "buy",	"unit-cost": 10,	"quantity": 10000}, {	"operation": "sell",	"unit-cost": 20,	"quantity": 5000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 10000)


    def test_one_buy_two_sell_operation_no_taxes_case_1(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 100},{"operation":"sell", "unit-cost":15, "quantity": 50},{"operation":"sell", "unit-cost":15, "quantity": 50}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 0)
        self.assertEqual(result[2]['tax'], 0)


    def test_one_buy_two_sell_operation_with_taxes_case_2(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 10000},{"operation":"sell", "unit-cost":20, "quantity": 5000},{"operation":"sell", "unit-cost":5, "quantity":5000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 10000)
        self.assertEqual(result[2]['tax'], 0)


    def test_one_buy_two_sell_operation_with_taxes_case_3(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 10000},{"operation":"sell", "unit-cost":20, "quantity": 5000},{"operation":"sell", "unit-cost":5, "quantity":5000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 0)
        self.assertEqual(result[2]['tax'], 5000)


    def test_two_buy_one_sell_operation_no_taxes_case_4(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 10000},{"operation":"buy","unit-cost":25, "quantity": 5000},{"operation":"sell", "unit-cost":15,"quantity": 10000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 0)
        self.assertEqual(result[2]['tax'], 0)


    def test_two_buy_two_sell_operation_with_taxes_case_5(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 10000},{"operation":"buy","unit-cost":25, "quantity": 5000},{"operation":"sell", "unit-cost":15,"quantity": 10000},{"operation":"sell", "unit-cost":25, "quantity": 5000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 0)
        self.assertEqual(result[2]['tax'], 0)
        self.assertEqual(result[3]['tax'], 10000)


    def test_one_buy_four_sell_operation_with_taxes_case_6(self):
        json_value = '[{"operation":"buy", "unit-cost":10, "quantity": 10000},{"operation":"sell","unit-cost":2, "quantity": 5000},{"operation":"sell", "unit-cost":20, "quantity":2000},{"operation":"sell", "unit-cost":20, "quantity": 2000},{"operation":"sell","unit-cost":25, "quantity": 1000}]'
        process = ProcessCapital()
        result = json.loads(process.execute(json_value))
        self.assertEqual(result[0]['tax'], 0)
        self.assertEqual(result[1]['tax'], 0)
        self.assertEqual(result[2]['tax'], 0)
        self.assertEqual(result[3]['tax'], 3000)

