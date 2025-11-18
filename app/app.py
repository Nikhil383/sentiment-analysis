from flask import Flask, request, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import logging
import os
from model_utils import load_model, predict_text

app = Flask(__name__)

REQUEST_COUNT = Counter("requests_total", "Total HTTP requests", ["endpoint"])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

HF_PIPELINE = None

@app.before_first_request
def load():
    global HF_PIPELINE
    model_path = os.environ.get("MODEL_PATH")
    device = int(os.environ.get("TORCH_DEVICE", "-1"))

    HF_PIPELINE = load_model(model_path, device=device)
    logger.info("Model loaded from %s", model_path)

@app.route("/predict", methods=["POST"])
def predict():
    REQUEST_COUNT.labels(endpoint="/predict").inc()
    payload = request.get_json()

    if "text" not in payload:
        return jsonify({"error": "Provide 'text'"}), 400

    result = predict_text(HF_PIPELINE, payload["text"])
    return jsonify({"predictions": result})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(debug=True)
