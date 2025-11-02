from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the sentiment analysis pipeline with the correct model
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

# Map raw labels to user-friendly sentiment
LABEL_MAP = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form.get("text", "")
    if not text.strip():
        return render_template("result.html", text=text, sentiment="No input provided", score=0)
    result = sentiment_analyzer(text)
    raw_label = result[0]["label"]
    sentiment = LABEL_MAP.get(raw_label, raw_label)  # fallback to raw if not found
    score = result[0]["score"]
    return render_template("result.html", text=text, sentiment=sentiment, score=score)

if __name__ == "__main__":
    app.run(debug=True)