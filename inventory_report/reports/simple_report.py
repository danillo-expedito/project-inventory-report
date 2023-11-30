from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report


class SimpleReport(Report):
    def __init__(self):
        self.inventories = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        oldest = None
        expiration = None
        company = None

        for inventory in self.inventories:
            if not oldest or oldest > inventory.get_earliest_date():
                oldest = inventory.get_earliest_date()
            if not expiration or expiration < inventory.get_latest_date():
                expiration = inventory.get_latest_date()
            if not company or company < inventory.get_company():
                company = inventory.get_company()

        return (
            f"Oldest manufacturing date: {oldest}\n"
            f"Closest expiration date: {expiration}\n"
            f"Company with the largest inventory: {company}"
        )
