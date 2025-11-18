from transformers import pipeline

def evaluate():
    pipe = pipeline(
        "sentiment-analysis",
        model="models/hf_model",
        tokenizer="models/hf_model"
    )
    print(pipe("This is amazing!"))

if __name__ == "__main__":
    evaluate()
