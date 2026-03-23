from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict():
    response = client.post("/predict", json={
        "idade": 30,
        "renda": 4000,
        "score": 600
    })

    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_invalid_data():
    response = client.post("/predict", json={
        "idade": "abc",  # inválido
        "renda": 4000,
        "score": 600
    })

    assert response.status_code == 422

def test_predict_edge_case():
    response = client.post("/predict", json={
        "idade": 0,
        "renda": 0,
        "score": 0
    })

    assert response.status_code == 200

def test_predict_high_score():
    response = client.post("/predict", json={
        "idade": 50,
        "renda": 10000,
        "score": 900
    })

    assert response.status_code == 200
    assert response.json()["prediction"] in [0, 1]