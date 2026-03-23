import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "artifacts/model.pkl"  # ou models/

def predict(data: dict):
    model = joblib.load(MODEL_PATH)
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return int(prediction[0])