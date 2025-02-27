# Sentiment Analysis 

This is an end-to-end machine learning project that performs sentiment analysis on user-provided text. The application uses a pre-trained model from Hugging Face (`cardiffnlp/twitter-roberta-base-sentiment`) and is built with Flask to provide a simple web interface. Users can input text, and the app will classify the sentiment as **Positive**, **Neutral**, or **Negative**, displaying the result along with a confidence score.

## Features
- **Sentiment Analysis**: Classifies text into Positive, Neutral, or Negative sentiments.
- **Web Interface**: Built with Flask, featuring a clean and user-friendly UI.
- **Pre-trained Model**: Utilizes `cardiffnlp/twitter-roberta-base-sentiment` from Hugging Face, fine-tuned on Twitter data.
- **Confidence Scores**: Displays the model's confidence in its prediction.
            

## Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

## Setup Instructions
1. **Clone the Repository** (or create the project locally):
   git clone https://github.com/Nikhil383/sentiment-analysis.git
2. **Install Dependencies**
   pip install -r requirements.txt
3. **Run the application**
   py app.py
   
## Usage
1. Input Text: On the home page (/), enter some text in the provided   textarea (e.g., "I love this app!" or "This is terrible.").

2. Analyze: Click the "Analyze" button to submit the text.
3. View Results: The result page will display:
The original text.
The predicted sentiment (Positive, Neutral, or Negative).
The confidence score as a percentage.
4. Try Again: Click "Analyze another text" to return to the home page.



## Example Outputs
1. Input: "I love this app!"
Sentiment: Positive
Confidence: 98%
2. Input: "This is terrible."
Sentiment: Negative
Confidence: 95%


## Model Details
1. Model: cardiffnlp/twitter-roberta-base-sentiment
2. Source: Hugging Face Transformers
3. Architecture: RoBERTa (Robustly optimized BERT approach)
4. Training Data: Fine-tuned on Twitter data for three-class sentiment 
classification (Positive, Neutral, Negative).

##Results
1. Postive case
![Sample1](https://github.com/user-attachments/assets/cc9f198f-70c2-44c5-9193-7e30a1580195)
![Sample1(Result)](https://github.com/user-attachments/assets/0286a471-5071-4f6a-aa4b-775e0dd1265c)

2. Negative Case

![Sample2](https://github.com/user-attachments/assets/ddfe058b-9ed0-4b49-b522-ca6e16fa9c0f)
![Sample2(Result)](https://github.com/user-attachments/assets/2a9350bf-d0e6-46ed-8324-96efef17cd56)


## Customization
1. Change Model: Modify the sentiment_analyzer line in app.py to use a different Hugging Face model (e.g., distilbert-base-uncased-finetuned-sst-2-english for binary classification).
2. Enhance UI: Edit static/style.css or use a framework like Bootstrap for a more polished look.
3. Add Features: Implement error handling or color-coded sentiments (see "Future Improvements").


## Future Improvements
1. Add color coding for sentiments (e.g., green for Positive, red for Negative).
2. Deploy the app online using Heroku, Render, or another hosting service.
3. Include input validation and error handling for robustness.
4. Support multi-language sentiment analysis by switching to a multilingual model.


## Troubleshooting
1. ModuleNotFoundError: Ensure all dependencies (flask, transformers, torch) are installed.
2. Port Conflict: If 5000 is in use, change the port in app.py by adding app.run(debug=True, port=5001).
3. Model Download Issues: Ensure an active internet connection the first time you run the app, as the model is downloaded automatically.


## License
This project is open-source and available under the MIT License.

## Acknowledgments
1. Hugging Face for providing pre-trained models and the Transformers library.
2. Flask for the lightweight web framework.
