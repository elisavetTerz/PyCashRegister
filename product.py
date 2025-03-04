class Product:
<<<<<<< Updated upstream
    def __init__(self, name, price):
        self.name = name
        self.price = price
=======
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(code={self.code}, name={self.name}, price={self.price})"

# Test Data: Defining products
GR1 = Product('GR1', 'Green Tea', 3.11)
SR1 = Product('SR1', 'Strawberries', 5.00)
CF1 = Product('CF1', 'Coffee', 11.23)

>>>>>>> Stashed changes
