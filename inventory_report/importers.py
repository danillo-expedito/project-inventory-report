from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        raise NotImplementedError


class JsonImporter(Importer):
    def __init__(self, path: str):
        super().__init__(path)
        self.products: List[Product] = []

    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file:
            data = json.load(file)
            for product in data:
                self.products.append(Product(**product))

        return self.products


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

if __name__ == "__main__":
    json_importer = JsonImporter("inventory_report/data/inventory.json")
    products = json_importer.import_data()
    print(products)
