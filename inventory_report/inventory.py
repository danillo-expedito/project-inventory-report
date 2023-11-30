from typing import Optional, List
from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[List[Product]] = None):
        self._data = data or []

    @property
    def data(self):
        return self._data

    def add_data(self, data: List[Product]):
        self.data.extend(data)
