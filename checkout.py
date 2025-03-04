<<<<<<< Updated upstream
=======
from collections import Counter
>>>>>>> Stashed changes
from product import Product

class Checkout:
    def __init__(self):
<<<<<<< Updated upstream
        self.items = []

    def add_item(self, product):
        self.items.append(product)
    
    def total_price(self):
        return sum(item.price for item in self.items)
=======
        self.cart = Counter()

    def scan(self, product: Product):
        self.cart[product.code] += 1

    def calculate_total(self):
        total = 0

        # Applying the special pricing rules
        for product_code, quantity in self.cart.items():
            if product_code == 'GR1':  # Buy-one-get-one-free for Green Tea
                total += (quantity // 2 + quantity % 2) * 3.11
            elif product_code == 'SR1':  # Discount for bulk purchase of Strawberries
                if quantity >= 3:
                    total += quantity * 4.50
                else:
                    total += quantity * 5.00
            elif product_code == 'CF1':  # Discount for Coffee if 3 or more are bought
                if quantity >= 3:
                    total += quantity * (11.23 * 2 / 3)
                else:
                    total += quantity * 11.23

        return round(total, 2)

# Test the Checkout system
if __name__ == '__main__':
    gr1 = Product('GR1', 'Green Tea', 3.11)
    sr1 = Product('SR1', 'Strawberries', 5.00)
    cf1 = Product('CF1', 'Coffee', 11.23)

    checkout = Checkout()
    checkout.scan(gr1)
    checkout.scan(gr1)  # Buy-one-get-one-free for Green Tea
    checkout.scan(sr1)
    checkout.scan(sr1)
    checkout.scan(gr1)  # Green Tea again
    checkout.scan(cf1)
    checkout.scan(cf1)
    checkout.scan(cf1)  # Discount on Coffee when 3 are bought

    print(f"Total: {checkout.calculate_total()}€")  # Expected Total: 30.57€
>>>>>>> Stashed changes
