from flask import Flask, request, jsonify
import random

app = Flask(__name__)

SEED = 37
random.seed(SEED)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

REG_NUMBER = "FA23-BDS-037"


@app.route('/predict', methods=['GET'])
def predict():
    try:
        x1 = float(request.args.get('x1'))
        x2 = float(request.args.get('x2'))
        x3 = float(request.args.get('x3'))
    except (TypeError, ValueError):
        return jsonify({"error": "x1, x2, x3 are required and must be numeric"}), 400

    prediction = a1 * x1 + a2 * x2 + a3 * x3 + b

    return jsonify({
        "registration number": REG_NUMBER,
        "prediction": round(prediction, 2)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


