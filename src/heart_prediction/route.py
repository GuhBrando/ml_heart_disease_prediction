from fastapi import APIRouter
import joblib
import numpy as np

from .schema import model_payload

route = APIRouter()

@route.post("/model-prediction")
async def model_prediction(payload: model_payload):
    modelo = joblib.load(open(r"./models/ModeloRandomForest.pkl", "rb"))

    new_input = np.array([[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 5, 99, 2, 1, 1, 1, 4, 2, 1, 3, 1, 2, 12, 160, 78.02, 4, 1]])
    prediction = modelo.predict(new_input)

    return {"previsao": "Previsão do modelo é: " + str(prediction)}