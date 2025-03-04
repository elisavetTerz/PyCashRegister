class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.cart = {}

    def scan(self, product_code):
        if product_code in self.cart:
            self.cart[product_code] += 1
        else:
            self.cart[product_code] = 1

    def total(self):
        total_price = 0
        for product_code, quantity in self.cart.items():
            price = self.apply_pricing_rules(product_code, quantity)
            total_price += price
        return round(total_price, 2)

    def apply_pricing_rules(self, product_code, quantity):
        price_per_unit = self.pricing_rules[product_code]['price']
        
        if product_code == 'GR1':  # Buy-One-Get-One-Free
            return (quantity // 2 + quantity % 2) * price_per_unit
        
        elif product_code == 'SR1' and quantity >= 3:  # Bulk discount
            return quantity * 4.50
        
        elif product_code == 'CF1' and quantity >= 3:  # Coffee discount
            return quantity * (2/3 * price_per_unit)
        
        return quantity * price_per_unit
