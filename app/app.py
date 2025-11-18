from flask import Flask, request, jsonify, render_template
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import logging
import os
from model_utils import load_model, predict_text

app = Flask(__name__, template_folder="templates")

# Prometheus counter
REQUEST_COUNT = Counter("requests_total", "Total HTTP requests", ["endpoint"])

# Logger config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Hugging Face model cache
HF_PIPELINE = None
MODEL_LOADED = False


# ------------------------------
# Lazy Model Loader (Flask 3.x SAFE)
# ------------------------------
@app.before_request
def load_model_once():
    global HF_PIPELINE, MODEL_LOADED

    if MODEL_LOADED:
        return  # already loaded

    model_path = os.environ.get("MODEL_PATH")   # e.g. models/hf_model
    device = int(os.environ.get("TORCH_DEVICE", "-1"))

    try:
        HF_PIPELINE = load_model(model_path, device=device)
        logger.info("Loaded Hugging Face model from %s", model_path or "HF Hub")
    except Exception as e:
        logger.exception("Error loading model: %s", e)
        HF_PIPELINE = None

    MODEL_LOADED = True


# ------------------------------
# UI ROUTES
# ------------------------------

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/ui-predict", methods=["POST"])
def ui_predict():
    text = request.form.get("text")

    if not text:
        return "No text provided", 400

    result = predict_text(HF_PIPELINE, text)[0]

    return render_template(
        "result.html",
        text=text,
        label=result["label"],
        score=round(result["score"], 4),
    )


# ------------------------------
# JSON API
# ------------------------------

@app.route("/predict", methods=["POST"])
def predict():
    REQUEST_COUNT.labels(endpoint="/predict").inc()

    data = request.get_json(silent=True)
    if not data or "text" not in data:
        return jsonify({"error": "Provide 'text' field"}), 400

    try:
        result = predict_text(HF_PIPELINE, data["text"])
        return jsonify({"predictions": result})
    except Exception as e:
        logger.exception("Prediction error: %s", e)
        return jsonify({"error": "Prediction failed", "details": str(e)}), 500


# ------------------------------
# Metrics
# ------------------------------

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


# ------------------------------
# Custom 404
# ------------------------------

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not Found", "path": request.path}), 404


# ------------------------------
# Local development entrypoint
# ------------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )
