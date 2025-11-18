# src/app.py
from flask import Flask, request, jsonify, render_template
from model import SentimentModel
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# load model on startup (from HF Hub)
try:
    MODEL_DEVICE = os.environ.get("MODEL_DEVICE")  # optional override: 'cpu' or 'cuda'
    model = SentimentModel(device=MODEL_DEVICE)
    MODEL_LOADED = True
except Exception as e:
    print("Error loading model:", e)
    model = None
    MODEL_LOADED = False

@app.route("/")
def index():
    """Serve web UI."""
    return render_template("index.html", model_loaded=MODEL_LOADED)

@app.route("/health")
def health():
    return jsonify({"status": "ok", "model_loaded": MODEL_LOADED})

@app.route("/predict", methods=["POST"])
def predict():
    if not MODEL_LOADED:
        return jsonify({"error": "Model not loaded. Ensure container has network access."}), 503

    payload = request.get_json()
    if not payload or "texts" not in payload:
        return jsonify({"error": "JSON must contain 'texts' (list of strings)."}), 400

    texts = payload["texts"]
    if not isinstance(texts, list):
        return jsonify({"error": "'texts' must be a list of strings."}), 400

    preds, pos_probs = model.predict(texts)
    labels = ["negative" if p == 0 else "neutral" if p == 1 else "positive" for p in preds]

    return jsonify({"labels": labels, "prob_positive": pos_probs})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
