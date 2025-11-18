from app.model_utils import load_model, predict_text

def test_prediction():
    pipe = load_model(None)
    res = predict_text(pipe, "I love this!")
    assert isinstance(res, list)
    assert "label" in res[0]
    assert "score" in res[0]
