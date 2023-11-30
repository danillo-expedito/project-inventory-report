from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def __init__(self):
        super().__init__()
        self.inventories = []

    def generate(self) -> str:
        return (
            f"{super().generate()}\n"
            f"Stocked products by company:\n"
            f"{self._get_stocked_products_by_company()}"
        )

    def _get_stocked_products_by_company(self) -> str:
        companies_counter = Counter(
            product.company_name
            for inventory in self.inventories
            for product in inventory.data
        )

        results = [
            f"- {company}: {amount}\n"
            for company, amount in companies_counter.items()
        ]

        return "".join(results)
