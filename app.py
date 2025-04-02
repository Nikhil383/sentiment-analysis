import streamlit as st
from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Streamlit UI
st.title("Sentiment Analysis App")
st.write("Enter text below to analyze sentiment using a Hugging Face model.")

# User input
user_input = st.text_area("Enter text:")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        result = sentiment_pipeline(user_input)
        sentiment = result[0]['label']
        confidence = result[0]['score']
        
        st.subheader("Sentiment Result")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Confidence Score:** {confidence:.2f}")
    else:
        st.warning("Please enter text for analysis.")