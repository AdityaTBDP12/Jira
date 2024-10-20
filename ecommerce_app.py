# Jira/ecommerce_app.py

from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Sample product data
products = [
    {"id": 1, "name": "Product 1", "price": 29.99},
    {"id": 2, "name": "Product 2", "price": 39.99},
    {"id": 3, "name": "Product 3", "price": 49.99},
]

# Home route
@app.route('/')
def home():
    return render_template('home.html', products=products)

# Product route
@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template('product.html', product=product)

# Add to cart
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    return redirect(url_for('cart'))

# Cart route
@app.route('/cart')
def cart():
    cart_items = [p for p in products if p['id'] in session.get('cart', [])]
    return render_template('cart.html', cart_items=cart_items)

# Checkout route
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
