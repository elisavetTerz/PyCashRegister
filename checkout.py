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
    def __init__(self, pricing_rules: Dict[str, Product]) -> None:
        self.pricing_rules = pricing_rules
        self.cart: List[Product] = []

    def scan(self, product_code: str) -> None:
        if product_code not in self.pricing_rules:
            raise KeyError(f"Product {product_code} not found in pricing rules.")
        self.cart.append(self.pricing_rules[product_code])

    def total(self) -> float:
        item_counts: Dict[str, int] = {product.code: self.cart.count(product) for product in set(self.cart)}
        total_price: float = 0.0

        for code, count in item_counts.items():
            product = self.pricing_rules[code]
            base_price: float = product.price

            # Apply Buy-One-Get-One-Free for Green Tea (GR1)
            if code == 'GR1':
                # Half the price for every pair of Green Teas, plus the remainder at full price
                total_price += (count // 2 + count % 2) * base_price

            # Apply bulk discount for Strawberries (SR1)
            elif code == 'SR1' and count >= 3:
                total_price += count * 4.50  # Bulk price for Strawberries

            # Apply Coffee Discount if buying 3 or more (CF1)
            elif code == 'CF1' and count >= 3:
                total_price += count * base_price * (2/3)
            # Default pricing for items without discounts
            else:
                total_price += count * base_price

        return round(total_price, 2)
    
    def remove(self, product_code):
        """Remove a product from the cart by its code."""
        for product in self.cart:
            if product.code == product_code:
                self.cart.remove(product)
                return
        raise KeyError("Product not found in cart")