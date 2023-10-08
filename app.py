from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Sample initial data
stocks = []

# Function to generate random stock data
def generate_random_stock():
    names = ["Apple Inc.", "Google LLC", "Microsoft Corporation", "Amazon.com Inc.", "Facebook Inc."]
    symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]
    prices = [random.uniform(100, 500) for _ in range(5)]
    
    random_stock = {
        'name': random.choice(names),
        'ticker_symbol': random.choice(symbols),
        'current_price': round(random.choice(prices), 2)
    }
    
    return random_stock

# Add 10 random stocks to the initial data
for _ in range(10):
    stocks.append(generate_random_stock())

# Render the 'stocks.html' template for the root URL
@app.route('/')
def stocks_default():
    return render_template('stocks.html', stocks=stocks)

# Modify the '/add_stock' route to handle form data
@app.route('/add_stock', methods=['POST'])
def add_stock():
    name = request.form.get('name')
    ticker_symbol = request.form.get('ticker_symbol')
    current_price = request.form.get('current_price')

    if name and ticker_symbol and current_price:
        stock = {
            'name': name,
            'ticker_symbol': ticker_symbol,
            'current_price': current_price
        }
        stocks.append(stock)
        return jsonify({'message': 'Stock added successfully'}), 201
    else:
        return jsonify({'error': 'Invalid data format'}), 400

@app.route('/get_stocks', methods=['GET'])
def get_stocks():
    return jsonify({'stocks': stocks})

if __name__ == '__main__':
    app.run(debug=True)
