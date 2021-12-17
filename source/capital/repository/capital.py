from typing import List
from singleton_decorator import singleton

from capital.business.unit_capital import UnitCapital


@singleton
class CapitalRepository():
    capital_data: List[UnitCapital]
    loss: float

    def add_list(self, list: List[UnitCapital]):
        self.capital_data = list
        self.loss = 0.0


    def get_data(self)-> List[UnitCapital]:
        return self.capital_data

    def get_loss(self):
        return self.loss

    def save_loss(self, loss: float):
        self.loss = loss

    def __init__(self):
        self.capital_data = []