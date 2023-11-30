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


def test_create_product(test_product) -> None:
    assert test_product.id == "1"
    assert test_product.product_name == "Coca Cola"
    assert test_product.company_name == "Coca Cola Company"
    assert test_product.manufacturing_date == "2023-08-01"
    assert test_product.expiration_date == "2024-12-01"
    assert test_product.serial_number == "123456"
    assert test_product.storage_instructions == "Keep in dry and cool place"
