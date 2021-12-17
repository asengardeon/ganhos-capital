from typing import List

from capital.business.unit_capital import OperationEnum, UnitCapital


class UnitListBuilder:

    def __init__(self):
        self.instance = []

    def with_new_unit(self, operation: OperationEnum, unit_cost: float, quantity: int):
        self.instance.append(UnitCapital(operation, unit_cost, quantity))
        return self

    def build(self)-> List[UnitCapital]:
        return self.instance