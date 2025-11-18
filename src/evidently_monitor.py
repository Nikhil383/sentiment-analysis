import pandas as pd
from model import SentimentModel
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

def generate_texts(n=200):
    pos = ["I love this product!" for _ in range(n//2)]
    neg = ["I hate this." for _ in range(n//2)]
    return pos + neg

def main():
    model = SentimentModel()

    ref_texts = generate_texts(200)
    cur_texts = ref_texts.copy()

    # Simulate drift
    for i in range(20):
        cur_texts[i] += " extra words to simulate drift"

    preds_ref, probs_ref = model.predict(ref_texts)
    preds_cur, probs_cur = model.predict(cur_texts)

    df_ref = pd.DataFrame({
        "text": ref_texts,
        "predicted_label": preds_ref,
        "predicted_prob": probs_ref,
        "text_length": [len(t) for t in ref_texts]
    })

    df_cur = pd.DataFrame({
        "text": cur_texts,
        "predicted_label": preds_cur,
        "predicted_prob": probs_cur,
        "text_length": [len(t) for t in cur_texts]
    })

    dashboard = Dashboard(tabs=[DataDriftTab()])
    dashboard.calculate(df_ref, df_cur)
    dashboard.save("evidently_report.html")
    print("Saved evidently_report.html")

if __name__ == "__main__":
    main()
