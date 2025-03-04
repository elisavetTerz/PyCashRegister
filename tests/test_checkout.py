import unittest
from checkout import Checkout
class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.pricing_rules = {
            'GR1': {'price': 3.11},
            'SR1': {'price': 5.00},
            'CF1': {'price': 11.23}
        }
        self.checkout = Checkout(self.pricing_rules)

    def test_buy_one_get_one_free(self):
        self.checkout.scan('GR1')
        self.checkout.scan('GR1')
        self.assertEqual(self.checkout.total(), 3.11)

    def test_bulk_discount_strawberries(self):
        self.checkout.scan('SR1')
        self.checkout.scan('SR1')
        self.checkout.scan('GR1')
        self.checkout.scan('SR1')
        self.assertEqual(self.checkout.total(), 16.61)

    def test_coffee_discount(self):
        self.checkout.scan('GR1')
        self.checkout.scan('CF1')
        self.checkout.scan('SR1')
        self.checkout.scan('CF1')
        self.checkout.scan('CF1')
        self.assertEqual(self.checkout.total(), 30.57)
    
    def test_empty_cart(self):
        self.assertEqual(self.checkout.total(), 0)
    
    def test_single_product(self):
        self.checkout.scan('GR1')
        self.assertEqual(self.checkout.total(), 3.11)
    
    def test_different_order(self):
        self.checkout.scan('CF1')
        self.checkout.scan('GR1')
        self.checkout.scan('SR1')
        self.checkout.scan('CF1')
        self.checkout.scan('CF1')
        self.assertEqual(self.checkout.total(), 30.57)

    # fail case 
    def test_invalid_product(self):
        with self.assertRaises(KeyError):
            self.checkout.scan('INVALID')
            self.checkout.total()

if __name__ == '__main__':
    unittest.main(verbosity=2)
