from fastapi import FastAPI
from pydantic import BaseModel

from src.models.predict import predict

app = FastAPI()

class InputData(BaseModel):
    idade: int
    renda: float
    score: int

@app.get("/")
def home():
    return {"message": "API ML funcionando 🚀"}

@app.post("/predict")
def get_prediction(data: InputData):
    result = predict(data.dict())
    return {"prediction": result}