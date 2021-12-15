import unittest

from source.capital.business.sell_capital import SellCapital
from source.capital.business.unit_capital import OperationEnum
from unit_list_factory import UnitListBuilder


class SellCapitalTestcCase(unittest.TestCase):

    def test_remove_sold_equals(self):
        capital_data = UnitListBuilder().with_new_unit(OperationEnum.BUY, 10, 10000).build()
        sell_capital = SellCapital()
        capital_data = sell_capital.remove_sold_capital(capital_data, 10000)
        self.assertEqual(len(capital_data), 0)


    def test_remove_sold_minus(self):
        capital_data = UnitListBuilder().with_new_unit(OperationEnum.BUY, 10, 10000).build()
        sell_capital = SellCapital()
        capital_data = sell_capital.remove_sold_capital(capital_data, 5000)
        self.assertEqual(len(capital_data), 1)
        item = capital_data[0]
        self.assertEqual(item.quantity, 5000)


    def test_remove_sold_two_buys(self):
        capital_data = UnitListBuilder().with_new_unit(OperationEnum.BUY, 10, 10000).with_new_unit(OperationEnum.BUY, 10, 10000).build()
        sell_capital = SellCapital()
        capital_data = sell_capital.remove_sold_capital(capital_data, 15000)
        self.assertEqual(len(capital_data), 1)
        item = capital_data[0]
        self.assertEqual(item.quantity, 5000)
s