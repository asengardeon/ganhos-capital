from typing import List

from source.capital.business.unit_capital import UnitCapital


class SellCapital:

    def remove_sold_capital(self, data: List[UnitCapital], quantity: int) -> List[UnitCapital]:
        remove_more = True
        internal_quantity = quantity
        while remove_more and len(data) > 0:
            item = data.pop(0)
            if item.quantity == internal_quantity:
                remove_more = False
            elif item.quantity > internal_quantity:
                item.quantity -= internal_quantity
                data.insert(0, item)
                remove_more = False
            else:
                internal_quantity -= item.quantity
        return data

