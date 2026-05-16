# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


import unittest

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Cena nie może być ujemna")
        if quantity < 0:
            raise ValueError("Ilość nie może być ujemna")
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Nie można dodać ujemnej ilości")
        self.quantity += amount

    def remove_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Nie można usunąć ujemnej ilości")
        if amount > self.quantity:
            raise ValueError("Za mało na magazynie")
        self.quantity -= amount

    def is_available(self) -> bool:
        return self.quantity > 0

    def total_value(self) -> float:
        return self.price * self.quantity


class TestProduct(unittest.TestCase):
    
    def setUp(self):
        self.product = Product("Myszka", 150.0, 10)

    def test_init_ok(self):
        self.assertEqual(self.product.name, "Myszka")
        self.assertEqual(self.product.price, 150.0)
        self.assertEqual(self.product.quantity, 10)

    def test_init_bad_price(self):
        with self.assertRaises(ValueError):
            Product("Test", -10.0, 5)

    def test_init_bad_qty(self):
        with self.assertRaises(ValueError):
            Product("Test", 10.0, -5)

    def test_add_stock_ok(self):
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative(self):
        with self.assertRaises(ValueError):
            self.product.add_stock(-5)

    def test_remove_stock_ok(self):
        self.product.remove_stock(2)
        self.assertEqual(self.product.quantity, 8)

    def test_remove_stock_negative(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(-2)

    def test_remove_stock_too_much(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(20)

    def test_is_available(self):
        self.assertTrue(self.product.is_available())
        self.product.remove_stock(10)
        self.assertFalse(self.product.is_available())

    def test_total_value(self):
        self.assertEqual(self.product.total_value(), 1500.0)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)