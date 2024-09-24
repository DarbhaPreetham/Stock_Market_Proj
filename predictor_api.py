import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Load the trained model
with open('stock_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

# Root route
@app.route('/')
def index():
    return "Stock Predictor API is running. Use the /predict endpoint to get predictions."

# API endpoint to predict stock prices
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data['SMA_50'], data['SMA_200'], data['Price_Change'], data['Volatility']]
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

# Handle favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
