from typing import List

from source.capital.business.unit_capital import UnitCapital, OperationEnum


class Calculus:


    def __calculate_poderated_average(self, buy_list: List[UnitCapital], sell_item: UnitCapital)->float:
        total_buy = 0.0
        total_items = 0
        for capital in buy_list:
            quantity = capital.quantity
            unit_cost = capital.unit_cost
            total_buy += quantity * unit_cost
            total_items += quantity
        return 0 if total_items == 0 else total_buy / total_items


    def __calculate_taxes(self, item: UnitCapital, buy_list: List[UnitCapital]):
        poderated_average = self.__calculate_poderated_average(buy_list, item)
        sell_value = item.unit_cost * item.quantity
        sold_value = (sell_value - (poderated_average * item.quantity))
        tax_value = 0
        if sold_value >= 20000:
            tax_value = sold_value * 0.2
        return tax_value



    def calculate_tax(self, data: List[UnitCapital])->str:
        buy_list = []
        taxes = []
        for item in data:
            if item.operation == OperationEnum.BUY:
                buy_list.append(item)
                taxes.append(0)
            else:
                taxes.append(self.__calculate_taxes(item, buy_list))
        return taxes