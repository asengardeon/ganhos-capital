from typing import List

from capital.business.unit_capital import UnitCapital, OperationEnum


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


    def __calculate_taxes(self, item: UnitCapital, buy_list: List[UnitCapital], loss: float):
        poderated_average = self.__calculate_poderated_average(buy_list, item)
        sell_value = item.unit_cost * item.quantity
        sold_value = (sell_value - (poderated_average * item.quantity))
        tax_value = 0
        sold_value_with_loss = sold_value + loss
        if sold_value_with_loss <= 0:
            loss = sold_value_with_loss
        else:
            loss = 0
        if loss == 0 and sell_value > 20000 and sold_value_with_loss > 0:
            tax_value = sold_value_with_loss * 0.2
        return (tax_value, loss)



    def calculate_tax(self, data: List[UnitCapital], loss: float)->List[float]:
        buy_list = []
        taxes = []
        for item in data:
            if item.operation == OperationEnum.BUY:
                buy_list.append(item)
                taxes.append(0)
            else:
                tax, loss = self.__calculate_taxes(item, buy_list, loss)
                taxes.append(tax)
        return (taxes, loss)