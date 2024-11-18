from fastapi import APIRouter

from src.heart_prediction.service import ModelPrediction
from src.heart_prediction.schema import model_payload

route = APIRouter()
model = ModelPrediction()
@route.post("/model-prediction")
def model_prediction(payload: model_payload):

	model.predict(payload.model_dump())
	#return {"input": str(payload),
	#		"output": f"Previsão = {resultado}, com uma confiança de {confidence:.2f}%"}