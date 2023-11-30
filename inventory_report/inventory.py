from typing import Optional, List
from inventory_report.product import Product
from datetime import datetime
from collections import Counter


class Inventory:
    def __init__(self, data: Optional[List[Product]] = None):
        self._data = data or []

    @property
    def data(self):
        return self._data

    def add_data(self, data: List[Product]):
        self.data.extend(data)

    def get_earliest_date(self) -> str:
        if not self.data:
            return "No manufacturing dates available"

        earliest_date = min(
            [product.manufacturing_date for product in self.data]
        )

        return earliest_date

    def get_latest_date(self) -> str:
        current_date = datetime.today()

        valid_dates = [
            product.expiration_date
            for product in self.data
            if (
                datetime.strptime(product.expiration_date, "%Y-%m-%d")
                > current_date
            )
        ]

        if not valid_dates:
            return "No valid expiration dates available"

        latest_date = min(valid_dates)
        return latest_date

    def get_company(self) -> str:
        if not self.data:
            return "No companies available"

        company_with_more_products = Counter(
            [product.company_name for product in self.data]
        )

        return company_with_more_products.most_common(1)[0][0]
