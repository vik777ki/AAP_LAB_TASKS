# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

# test_product_unittest.py
import unittest
from product import Product

class TestProduct(unittest.TestCase):
    
    def setUp(self):
        # Ta metoda odpala się przed każdym pojedynczym testem
        self.product = Product("Klawiatura mechaniczna", 350.50, 10)

    def test_init_valid_values(self):
        self.assertEqual(self.product.name, "Klawiatura mechaniczna")
        self.assertEqual(self.product.price, 350.50)
        self.assertEqual(self.product.quantity, 10)

    def test_init_negative_price_raises_error(self):
        with self.assertRaises(ValueError):
            Product("Myszka", -50.0, 5)

    def test_init_negative_quantity_raises_error(self):
        with self.assertRaises(ValueError):
            Product("Monitor", 1200.0, -1)

    def test_add_stock_valid(self):
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises_error(self):
        with self.assertRaises(ValueError):
            self.product.add_stock(-2)

    def test_remove_stock_valid(self):
        self.product.remove_stock(3)
        self.assertEqual(self.product.quantity, 7)

    def test_remove_stock_negative_raises_error(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(-5)

    def test_remove_stock_too_much_raises_error(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(20)

    def test_is_available_true(self):
        self.assertTrue(self.product.is_available())

    def test_is_available_false(self):
        self.product.remove_stock(10)
        self.assertFalse(self.product.is_available())

    def test_total_value(self):
        expected_value = 350.50 * 10
        self.assertEqual(self.product.total_value(), expected_value)

if __name__ == '__main__':
    unittest.main()