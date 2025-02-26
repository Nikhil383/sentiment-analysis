from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the Hugging Face sentiment analysis pipeline with the RoBERTa model
sentiment_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        # Get the text input from the form
        user_input = request.form['text']
        
        # Perform sentiment analysis
        result = sentiment_analyzer(user_input)[0]
        label = result['label']  # LABEL_0, LABEL_1, or LABEL_2
        score = result['score']  # Confidence score
        
        # Map the label to a user-friendly sentiment
        if label == "LABEL_0":
            sentiment = "Negative"
        elif label == "LABEL_1":
            sentiment = "Neutral"
        else:  # LABEL_2
            sentiment = "Positive"
        
        # Render the result page with the sentiment and score
        return render_template('result.html', text=user_input, sentiment=sentiment, score=score)

if __name__ == '__main__':
    app.run(debug=True)
