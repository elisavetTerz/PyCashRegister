import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product('GR1', 'Green Tea', 3.11)
        self.assertEqual(product.code, 'GR1')
        self.assertEqual(product.name, 'Green Tea')
        self.assertEqual(product.price, 3.11)

    def test_product_repr(self):
        product = Product('CF1', 'Coffee', 11.23)
        self.assertEqual(repr(product), "Product(code='CF1', name='Coffee', price=11.23)")

    def test_different_product_creation(self):
        product = Product('SR1', 'Strawberries', 5.00)
        self.assertEqual(product.code, 'SR1')
        self.assertEqual(product.name, 'Strawberries')
        self.assertEqual(product.price, 5.00)


if __name__ == '__main__':
    unittest.main()