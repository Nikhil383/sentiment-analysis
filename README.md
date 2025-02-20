# Sentiment Analysis Web App

This is an end-to-end machine learning project that performs sentiment analysis on user-provided text. The application uses a pre-trained model from Hugging Face (`cardiffnlp/twitter-roberta-base-sentiment`) and is built with Flask to provide a simple web interface. Users can input text, and the app will classify the sentiment as **Positive**, **Neutral**, or **Negative**, displaying the result along with a confidence score.

## Features
- **Sentiment Analysis**: Classifies text into Positive, Neutral, or Negative sentiments.
- **Web Interface**: Built with Flask, featuring a clean and user-friendly UI.
- **Pre-trained Model**: Utilizes `cardiffnlp/twitter-roberta-base-sentiment` from Hugging Face, fine-tuned on Twitter data.
- **Confidence Scores**: Displays the model's confidence in its prediction.

## Project Structure

sentiment_analysis_project/
├── app.py                # Flask application and sentiment analysis logic
├── templates/
│   ├── index.html       # Home page with input form
│   └── result.html      # Result page displaying sentiment
├── static/
│   └── style.css        # Basic CSS for styling
└── README.md            # Project documentation



## Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

## Setup Instructions
1. **Clone the Repository** (or create the project locally):
   git clone <repository-url>
   cd sentiment_analysis_project
2. **Clone the Repository** (or create the project locally):
   git clone <repository-url>
   cd sentiment_analysis_project
3. **Install Dependencies**
   pip install flask transformers torch
4. **Run the application**
   
## Usage
Input Text: On the home page (/), enter some text in the provided textarea (e.g., "I love this app!" or "This is terrible.").
Analyze: Click the "Analyze" button to submit the text.
View Results: The result page will display:
The original text.
The predicted sentiment (Positive, Neutral, or Negative).
The confidence score as a percentage.
Try Again: Click "Analyze another text" to return to the home page.



## Example Outputs
Input: "I love this app!"
Sentiment: Positive
Confidence: ~98%
Input: "This is terrible."
Sentiment: Negative
Confidence: 95%


## Model Details
Model: cardiffnlp/twitter-roberta-base-sentiment
Source: Hugging Face Transformers
Architecture: RoBERTa (Robustly optimized BERT approach)
Training Data: Fine-tuned on Twitter data for three-class sentiment classification (Positive, Neutral, Negative).


## Customization
Change Model: Modify the sentiment_analyzer line in app.py to use a different Hugging Face model (e.g., distilbert-base-uncased-finetuned-sst-2-english for binary classification).
Enhance UI: Edit static/style.css or use a framework like Bootstrap for a more polished look.
Add Features: Implement error handling or color-coded sentiments (see "Future Improvements").


## Future Improvements
Add color coding for sentiments (e.g., green for Positive, red for Negative).
Deploy the app online using Heroku, Render, or another hosting service.
Include input validation and error handling for robustness.
Support multi-language sentiment analysis by switching to a multilingual model.


## Troubleshooting
ModuleNotFoundError: Ensure all dependencies (flask, transformers, torch) are installed.
Port Conflict: If 5000 is in use, change the port in app.py by adding app.run(debug=True, port=5001).
Model Download Issues: Ensure an active internet connection the first time you run the app, as the model is downloaded automatically.



## License
This project is open-source and available under the MIT License.

## Acknowledgments
Hugging Face for providing pre-trained models and the Transformers library.
Flask for the lightweight web framework.