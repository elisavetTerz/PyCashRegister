from flask import Flask, jsonify, request
from flask_cors import CORS
from checkout import Product, Checkout

app = Flask(__name__)
CORS(app)

# Define available products
products = [
    Product('GR1', 'Green Tea', 3.11),
    Product('SR1', 'Strawberries', 5.00),
    Product('CF1', 'Coffee', 11.23)
]

# Define pricing rules
pricing_rules = {
    'GR1': {'price': 3.11},
    'SR1': {'price': 5.00},
    'CF1': {'price': 11.23}
}

# Initialize checkout system
checkout = Checkout(pricing_rules)


@app.route('/products', methods=['GET'])
def get_products():
    """
    Returns the list of available products.

    Returns:
        JSON: A list of products with code, name, and price.
    """
    return jsonify([{'code': p.code, 'name': p.name, 'price': p.price} for p in products])


@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    """
    Adds a product to the checkout cart.

    Returns:
        JSON: The updated cart list.
    """
    data = request.json
    product_code = data.get('productCode')

    if not product_code:
        return jsonify({'error': 'Product code is required'}), 400

    try:
        checkout.scan(product_code)
        return jsonify({'cart': checkout.cart})
    except KeyError:
        return jsonify({'error': 'Invalid product code'}), 400


@app.route('/checkout', methods=['POST'])
def checkout_total():
    """
    Calculates the total price of the cart.

    Returns:
        JSON: The total amount.
    """
    total = checkout.total()
    return jsonify({'total': total})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
