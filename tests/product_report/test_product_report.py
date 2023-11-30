from inventory_report.product import Product
import pytest


@pytest.fixture
def test_product() -> Product:
    return Product(
        "1",
        "Coca Cola",
        "Coca Cola Company",
        "2023-08-01",
        "2024-12-01",
        "123456",
        "Keep in dry and cool place"
    )


def test_product_report(test_product) -> None:
    assert str(test_product) == (
        "The product 1 - Coca Cola with serial number 123456 "
        "manufactured on 2023-08-01 by the company Coca Cola Company "
        "valid until 2024-12-01 must be stored according to the following "
        "instructions: Keep in dry and cool place."
    )
