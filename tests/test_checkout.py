import unittest
from checkout import Checkout

class TestCheckout(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up the initial pricing rules and checkout instance.
        """
        self.pricing_rules = {
            'GR1': {'price': 3.11},
            'SR1': {'price': 5.00},
            'CF1': {'price': 11.23}
        }
        self.checkout = Checkout(self.pricing_rules)

    def test_buy_one_get_one_free(self) -> None:
        """
        Test Buy-One-Get-One-Free discount for Green Tea (GR1).
        """
        self.checkout.scan('GR1')
        self.checkout.scan('GR1')
        self.assertEqual(self.checkout.total(), 3.11)

    def test_bulk_discount_strawberries(self) -> None:
        """
        Test bulk discount for Strawberries (SR1) when buying 3 or more.
        """
        self.checkout.scan('SR1')
        self.checkout.scan('SR1')
        self.checkout.scan('GR1')
        self.checkout.scan('SR1')
        self.assertEqual(self.checkout.total(), 16.61)

    def test_coffee_discount(self) -> None:
        """
        Test Coffee discount when buying 3 or more (CF1).
        """
        self.checkout.scan('GR1')
        self.checkout.scan('CF1')
        self.checkout.scan('SR1')
        self.checkout.scan('CF1')
        self.checkout.scan('CF1')
        self.assertEqual(self.checkout.total(), 30.57)
    
    def test_edge_case_3_strawberries(self) -> None:
        """
        Test when exactly 3 Strawberries are scanned, should trigger bulk price.
        """
        self.checkout.scan('SR1')
        self.checkout.scan('SR1')
        self.checkout.scan('SR1')  # 3 should trigger bulk price
        self.assertEqual(self.checkout.total(), 13.50)  # 4.50 * 3

    def test_edge_case_3_coffees(self) -> None:
        """
        Test when exactly 3 Coffees are scanned, should trigger discount.
        """
        self.checkout.scan('CF1')
        self.checkout.scan('CF1')
        self.checkout.scan('CF1')  # 3 should trigger discount
        self.assertEqual(self.checkout.total(), round(3 * (2 / 3 * 11.23), 2))

    def test_empty_cart(self) -> None:
        """
        Test empty cart, should return total 0.
        """
        self.assertEqual(self.checkout.total(), 0)

    def test_single_product(self) -> None:
        """
        Test a cart with a single product (GR1).
        """
        self.checkout.scan('GR1')
        self.assertEqual(self.checkout.total(), 3.11)

    def test_different_order(self) -> None:
        """
        Test different order of products in the cart.
        """
        self.checkout.scan('CF1')
        self.checkout.scan('GR1')
        self.checkout.scan('SR1')
        self.checkout.scan('CF1')
        self.checkout.scan('CF1')  # 3 CF1 should still trigger discount
        self.assertEqual(self.checkout.total(), 30.57)

    def test_invalid_product(self) -> None:
        """
        Test invalid product code, should raise KeyError.
        """
        with self.assertRaises(KeyError):
            self.checkout.scan('INVALID')

if __name__ == '__main__':
    unittest.main(verbosity=2)
