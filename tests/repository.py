import unittest

from capital.repository.capital import CapitalRepository

from capital.adapter.json_adapter import JsonAdapter


class RepositoryCapitalTestcCase(unittest.TestCase):

    def setUp(self):
        self.repo = CapitalRepository()
        self.adapter = JsonAdapter()


    def tearDown(self):
        self.repo.add_list = []


    def test_add_data(self):
        json = '[{	"operation": "buy",	"unit-cost": 10,	"quantity": 10000}, {	"operation": "sell",	"unit-cost": 20,	"quantity": 5000}]'
        capital = self.adapter.json_to_unit_list(json)
        self.repo.add_list(capital)
        self.assertEqual(self.repo.get_data.count, 2)






