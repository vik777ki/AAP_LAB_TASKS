# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product

@pytest.fixture
def product():
    return Product("Myszka", 150.0, 10)

def test_init_ok(product):
    assert product.name == "Myszka"
    assert product.price == 150.0
    assert product.quantity == 10

def test_init_bad_price():
    with pytest.raises(ValueError):
        Product("Test", -10.0, 5)

def test_init_bad_qty():
    with pytest.raises(ValueError):
        Product("Test", 10.0, -5)

@pytest.mark.parametrize("amount, expected_qty", [
    (5, 15),
    (0, 10),
    (20, 30)
])
def test_add_stock_ok(product, amount, expected_qty):
    product.add_stock(amount)
    assert product.quantity == expected_qty

def test_add_stock_negative(product):
    with pytest.raises(ValueError):
        product.add_stock(-5)

def test_remove_stock_ok(product):
    product.remove_stock(2)
    assert product.quantity == 8

def test_remove_stock_negative(product):
    with pytest.raises(ValueError):
        product.remove_stock(-2)

def test_remove_stock_too_much(product):
    with pytest.raises(ValueError):
        product.remove_stock(20)

def test_is_available(product):
    assert product.is_available() is True
    product.remove_stock(10)
    assert product.is_available() is False

def test_total_value(product):
    assert product.total_value() == 1500.0