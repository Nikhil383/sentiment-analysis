from pathlib import Path
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import os

HF_MODEL_NAME = os.environ.get(
    "HF_MODEL_NAME", "cardiffnlp/twitter-roberta-base-sentiment-latest"
)

def save_hf_model_locally(model_name=HF_MODEL_NAME, save_dir=Path("models/hf_model")):
    save_dir.mkdir(parents=True, exist_ok=True)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer.save_pretrained(save_dir)
    model.save_pretrained(save_dir)
    return save_dir

def load_model(path=None, device=-1):
    if path:
        p = Path(path)
        if p.exists():
            return pipeline(
                "sentiment-analysis", model=str(p), tokenizer=str(p), device=device
            )
    return pipeline("sentiment-analysis", model=HF_MODEL_NAME, device=device)

def predict_text(pipe, texts):
    if isinstance(texts, str):
        texts = [texts]
    outputs = pipe(texts)
    return [
        {"text": t, "label": o["label"], "score": float(o["score"])}
        for t, o in zip(texts, outputs)
    ]
