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
    'GR1': Product('GR1', 'Green Tea', 3.11),
    'SR1': Product('SR1', 'Strawberries', 5.00),
    'CF1': Product('CF1', 'Coffee', 11.23)
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
    data = request.json
    product_code = data.get('productCode')

    if not product_code:
        return jsonify({'error': 'Product code is required'}), 400

    try:
        checkout.scan(product_code)
        return jsonify({
            'cart': [{'code': p.code, 'name': p.name, 'price': p.price} for p in checkout.cart],
            'total': checkout.total()  # Return the total along with the updated cart
        })
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

@app.route('/remove-from-cart', methods=['POST'])
def remove_from_cart():
    data = request.json
    product_code = data.get('productCode')

    if not product_code:
        return jsonify({'error': 'Product code is required'}), 400

    try:
        # Remove the item from the cart by scanning it out
        checkout.remove(product_code)
        return jsonify({
            'cart': [{'code': p.code, 'name': p.name, 'price': p.price} for p in checkout.cart],
            'total': checkout.total()  # Return updated cart and total
        })
    except KeyError:
        return jsonify({'error': 'Product not found in cart'}), 400

@app.route('/clear-cart', methods=['POST'])
def clear_cart():
    """
    Clears the cart.
    
    Returns:
        JSON: Empty cart and total amount.
    """
    checkout.cart = []  # Clear the cart
    return jsonify({'cart': checkout.cart, 'total': checkout.total()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
