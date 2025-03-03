from product import Product

class Checkout:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
    
    def total_price(self):
        return sum(item.price for item in self.items)