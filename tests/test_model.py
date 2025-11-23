# tests/test_model.py
from app.model_utils import load_model, predict_text

def test_prediction_labels():
    pipe = load_model(None)
    res = predict_text(pipe, "I love this!")
    assert isinstance(res, list)
    assert res[0]["label"] in {"NEGATIVE", "NEUTRAL", "POSITIVE"}
    assert "score" in res[0]
