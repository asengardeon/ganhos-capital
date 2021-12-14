from typing import List

from capital.adapter.json_adapter import JsonAdapter
from capital.capital.unit_capital import UnitCapital, OperationEnum
from capital.repository.capital import CapitalRepository

class ProcessCapital:

    def __calculate_poderated_average(self, buy_list: List[UnitCapital], sell_item: UnitCapital)->float:
        total_buy = 0.0
        total_items = 0
        for capital in buy_list:
            quantity = capital.quantity
            unit_cost = capital.unit_cost
            total_buy += quantity * unit_cost
            total_items += quantity
        return 0 if total_items == 0 else total_buy / total_items


    def __calculate_tax(self)->str:
        capital_repository = CapitalRepository()
        data = capital_repository.get_data().copy()
        buy_list = []
        taxes = []
        for item in data:
            if item.operation == OperationEnum.BUY:
                buy_list.append(item)
            else:
                poderated_average = self.__calculate_poderated_average(buy_list, item)
                sell_value = item.unit_cost * item.quantity
                taxes.append(poderated_average * item.quantity - sell_value)
        return taxes


    def __persist_entrace(self, data: List[UnitCapital]) -> None:
        capital_repository = CapitalRepository()
        capital_repository.add_list(data)


    def execute(self, capital_json: str):
        json_adapter = JsonAdapter()
        capital = json_adapter.json_to_unit_list(capital_json)
        self.__persist_entrace(capital)
        taxes = self.__calculate_tax()
        print(taxes)


