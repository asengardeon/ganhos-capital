from enum import IntEnum


class OperationEnum(IntEnum):
    SELL = 1
    BUY = 2


class UnitCapital:

    operation: OperationEnum
    unit_cost: float
    quantity: int

    def __init__(self, operation: OperationEnum, unit_cost: float, quantity: int):
        self.operation = operation
        self.unit_cost = unit_cost
        self.quantity = quantity

