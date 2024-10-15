from flask import Flask, jsonify


app = Flask(__name__)


recommended_products = [
    {"id": 1, "name": "Face Cream", "price": 15.99, "category": "Skincare"},
    {"id": 2, "name": "Lipstick", "price": 9.99, "category": "Makeup"},
    {"id": 3, "name": "Perfume", "price": 29.99, "category": "Fragrance"}
]

@app.route('/recommended-products', methods=['GET'])
def get_recommended_products():
    return jsonify({"recommended_products": recommended_products})

if __name__ == '__main__':
    app.run(debug=True)
