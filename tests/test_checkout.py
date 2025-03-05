import unittest
from checkout import Product, Checkout

class TestCheckout(unittest.TestCase):
    def setUp(self):
        # Define product prices and rules as Product objects
        self.pricing_rules = {
            'GR1': Product('GR1', 'Green Tea', 3.11),
            'SR1': Product('SR1', 'Strawberries', 5.00),
            'CF1': Product('CF1', 'Coffee', 11.23),
        }

        # Create an instance of Checkout with pricing rules
        self.checkout = Checkout(self.pricing_rules)

    def test_scan_gr1_gr1(self):
        """Test scanning two Green Tea (GR1) items with buy-one-get-one-free."""
        self.checkout.scan('GR1')
        self.checkout.scan('GR1')
        self.assertEqual(self.checkout.total(), 3.11)

    def test_scan_sr1_sr1_gr1_sr1(self):
        """Test scanning Strawberries (SR1) with bulk price and Green Tea (GR1)."""
        self.checkout.scan('SR1')
        self.checkout.scan('SR1')
        self.checkout.scan('GR1')
        self.checkout.scan('SR1')
        self.assertEqual(self.checkout.total(), 16.61)

    def test_scan_gr1_cf1_sr1_cf1_cf1(self):
        """Test scanning Green Tea (GR1), Coffee (CF1) with discount for 3 coffees, and Strawberries (SR1)."""
        self.checkout.scan('GR1')
        self.checkout.scan('CF1')
        self.checkout.scan('SR1')
        self.checkout.scan('CF1')
        self.checkout.scan('CF1')
        self.assertEqual(self.checkout.total(), 30.57)

    def test_scan_sr1_with_bulk_discount(self):
        """Test scanning 3 Strawberries (SR1) to apply the bulk discount."""
        self.checkout.scan('SR1')
        self.checkout.scan('SR1')
        self.checkout.scan('SR1')
        self.assertEqual(self.checkout.total(), 13.50)  # 3 * 4.50€

    def test_scan_cf1_with_discount(self):
        """Test scanning 3 Coffees (CF1) to apply the discount of 2/3 off the price."""
        self.checkout.scan('CF1')
        self.checkout.scan('CF1')
        self.checkout.scan('CF1')
        self.assertEqual(self.checkout.total(), 22.46)  # 3 * (2/3 of 11.23)

    def test_invalid_product_code(self):
        """Test scanning an invalid product code raises KeyError."""
        with self.assertRaises(KeyError):
            self.checkout.scan('INVALID')

if __name__ == '__main__':
    unittest.main()