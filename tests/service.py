import unittest

from capital.service.process_capital import ProcessCapital


class ServiceTestCase(unittest.TestCase):
    def test_execute(self):
        json = '[{	"operation": "buy",	"unit-cost": 10,	"quantity": 10000}, {	"operation": "sell",	"unit-cost": 20,	"quantity": 5000}]'
        process = ProcessCapital()
        process.execute(json)
