"""
api.py
~~~~~~

This module defines a simple REST API for a Machine Learning (ML) model.
"""

from os import environ

from joblib import load
from flask import abort, Flask, jsonify, make_response, request
from pandas import DataFrame


service_name = environ['SERVICE_NAME']
version = environ['API_VERSION']
model = load('model.joblib')
app = Flask(__name__)


@app.route(f'/{service_name}/v{version}/predict', methods=['POST'])
def predict():
    """TODO"""
    try:
        features = DataFrame(request.json)
        prediction = model.predict(features).tolist()
        return make_response(jsonify({'prediction': prediction}))
    except ValueError:
        raise RuntimeError('Features are not in the correct format.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
