from typing import Dict, List


class Product:
    """
    Represents a product in the store.

    Attributes:
        code (str): Unique product code.
        name (str): Product name.
        price (float): Unit price of the product.
    """

    def __init__(self, code: str, name: str, price: float) -> None:
        self.code = code
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        """Returns a detailed string representation for debugging."""
        return f"Product(code='{self.code}', name='{self.name}', price={self.price})"

    def __str__(self) -> str:
        """Returns a user-friendly string representation."""
        return f"{self.name} (${self.price:.2f})"


class Checkout:
    """
    Handles the checkout process, including scanning items and applying pricing rules.

    Attributes:
        pricing_rules (Dict[str, Dict[str, float]]): A dictionary mapping product codes to pricing rules.
    """

    def __init__(self, pricing_rules: Dict[str, Dict[str, float]]) -> None:
        self.pricing_rules = pricing_rules
        self.cart: List[str] = []

    def scan(self, product_code: str) -> None:
        """
        Adds a product to the cart.

        Args:
            product_code (str): The unique product code.
        
        Raises:
            KeyError: If the product code is not found in pricing rules.
        """
        if product_code not in self.pricing_rules:
            raise KeyError(f"Product {product_code} not found in pricing rules.")
        self.cart.append(product_code)

    def total(self) -> float:
        """
        Calculates the total price of items in the cart, applying discounts.

        Returns:
            float: The total price after applying discounts.
        """
        item_counts: Dict[str, int] = {code: self.cart.count(code) for code in set(self.cart)}
        total_price: float = 0.0

        for code, count in item_counts.items():
            base_price: float = self.pricing_rules[code]['price']

            # Apply Buy-One-Get-One-Free for Green Tea (GR1)
            if code == 'GR1':
                total_price += (count // 2 + count % 2) * base_price

            # Apply bulk discount for Strawberries (SR1)
            elif code == 'SR1' and count >= 3:
                total_price += count * 4.50
            else:
                total_price += count * base_price

            # Apply Coffee Discount if buying 3 or more (CF1)
            if code == 'CF1' and count >= 3:
                total_price += count * (2 / 3 * base_price)
            elif code == 'CF1':
                total_price += count * base_price

        return round(total_price, 2)
