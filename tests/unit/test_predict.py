from unittest.mock import patch
import pytest

@patch("src.models.predict.joblib.load")
def test_predict_mock(mock_model):
    
    class FakeModel:
        def predict(self, X):
            return [1]

    mock_model.return_value = FakeModel()

    from src.models.predict import predict

    result = predict({
        "idade": 30,
        "renda": 4000,
        "score": 600
    })

    assert result == 1

@patch("src.models.predict.joblib.load")
def test_model_failure(mock_model):
    mock_model.side_effect = Exception("Erro ao carregar modelo")

    from src.models.predict import predict

    with pytest.raises(Exception):
        predict({
            "idade": 30,
            "renda": 4000,
            "score": 600
        })