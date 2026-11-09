
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Homepage
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        cgpa = float(data['cgpa'])
        iq = int(data['iq'])

        input_features = np.array([[cgpa, iq]])

        prediction = model.predict(input_features)[0]

        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
