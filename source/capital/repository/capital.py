from typing import List
from capital.capital.unit_capital import UnitCapital
from singleton_decorator import singleton

@singleton
class CapitalRepository():
    capital_data: List[UnitCapital]

    def add_list(self, list: List[UnitCapital]):
        self.capital_data = list


    def get_data(self)-> List[UnitCapital]:
        return self.capital_data


    def __init__(self):
        self.capital_data = []