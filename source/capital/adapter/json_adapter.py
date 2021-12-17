import json
from typing import List

from singleton_decorator import singleton

from capital.business.unit_capital import UnitCapital, OperationEnum


@singleton
class JsonAdapter:

    def __json_operation_to_operation_enum__(self, operation: str)->OperationEnum:
        if operation.lower() == "sell":
            return OperationEnum.SELL
        result = OperationEnum.BUY
        return result


    def json_to_unit_list(self, json_value: str)->List[UnitCapital]:
        data = json.loads(json_value)
        result = []
        for item in data:
            operation = item['operation']
            unit_cost = item['unit-cost']
            quantity = item['quantity']
            converted_operation = self.__json_operation_to_operation_enum__(operation)
            new_capital = UnitCapital(converted_operation, float(unit_cost), int(quantity))
            result.append(new_capital)
        return result

    def tax_list_to_json(self, data: List[float]):
        result = []
        for item in data:
            result.append({"tax": item})
        return json.dumps(result)



