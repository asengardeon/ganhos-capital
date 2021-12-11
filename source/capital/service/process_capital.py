from capital.adapter.json_adapter import JsonAdapter
from capital.repository.capital import CapitalRepository


class ProcessCapital:

    def execute(self, capital_json: str):
        json_adapter = JsonAdapter()
        capital = json_adapter.json_to_unit_list(capital_json)
        capital_repository = CapitalRepository()
        capital_repository.add_list(capital)

