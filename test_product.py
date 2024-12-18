import pytest
import store
import products

def test_create_product():
    product = products.Product("MacBook Air M2", price=1450.00, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450.00
    assert product.quantity == 100
    assert product.is_active() == True


def test_invalid_details():
    with pytest.raises(ValueError):
        products.Product("", price=100, quantity=10)

    with pytest.raises(ValueError):
        products.Product("Invalid Product", price=-100, quantity=10)

    with pytest.raises(ValueError):
        products.Product("Invalid Product", price=100, quantity=-10)


def test_ran_out_stock():
    product = products.Product("MacBook Air M2", price=1450.00, quantity=1)
    product.buy(1)
    assert product.get_quantity() == 0
    assert product.is_active() == False


def test_product_purchase():
    product = products.Product("MacBook Air M2", price=1450.00, quantity=100)


    total_cost = product.buy(10)

    assert product.get_quantity() == 90
    assert total_cost == 1450.00 * 10


def test_product_purchase_invalid_quantity():
    product = products.Product("MacBook Air M2", price=1450.00, quantity=100)

    assert product.buy(200) == ValueError