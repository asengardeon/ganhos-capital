import json
from typing import List

from source.capital.adapter.json_adapter import JsonAdapter
from source.capital.business.calculus import Calculus
from source.capital.business.unit_capital import UnitCapital
from source.capital.repository.capital import CapitalRepository


class ProcessCapital:

    def __init__(self):
        self.capital_repository = CapitalRepository()

    def __persist_entrace(self, data: List[UnitCapital]) -> None:
        self.capital_repository.add_list(data)

    def execute(self, capital_json: str):
        json_adapter = JsonAdapter()
        capital = json_adapter.json_to_unit_list(capital_json)
        self.__persist_entrace(capital)
        calculus = Calculus()
        loss = self.capital_repository.get_loss()
        taxes, loss = calculus.calculate_tax(capital, loss)
        self.capital_repository.save_loss(loss)
        taxes_output = json_adapter.tax_list_to_json(taxes)
        return taxes_output



