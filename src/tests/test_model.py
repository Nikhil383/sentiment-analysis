from model import SentimentModel

def test_predict():
    model = SentimentModel()
    preds, probs = model.predict(["I love it", "I hate this"], batch_size=2)
    assert len(preds) == 2
    assert len(probs) == 2
