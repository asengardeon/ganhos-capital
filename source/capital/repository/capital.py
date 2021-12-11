from typing import List
from capital.capital.unit_capital import UnitCapital

class CapitalRepository():
    capital_data: List[UnitCapital]

    def add_list(self, list: List[UnitCapital]):
        self.capital_data = list