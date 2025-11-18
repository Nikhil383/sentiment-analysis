from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
from typing import List, Tuple

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"

class SentimentModel:
    def __init__(self, model_name: str = MODEL_NAME, device: str = None):
        self.model_name = model_name
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")

        print(f"Loading model from Hugging Face Hub: {self.model_name}")

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.model.to(self.device)

    def predict(self, texts: List[str], batch_size: int = 8) -> Tuple[List[int], List[float]]:
        all_preds = []
        all_pos_probs = []

        self.model.eval()
        with torch.no_grad():
            for i in range(0, len(texts), batch_size):
                batch = texts[i:i + batch_size]
                inputs = self.tokenizer(batch, padding=True, truncation=True, return_tensors="pt")
                inputs = {k: v.to(self.device) for k, v in inputs.items()}

                outputs = self.model(**inputs)
                probs = F.softmax(outputs.logits, dim=-1)

                preds = torch.argmax(probs, dim=1).tolist()
                pos_probs = probs[:, 2].tolist()

                all_preds.extend(preds)
                all_pos_probs.extend(pos_probs)

        return all_preds, all_pos_probs
