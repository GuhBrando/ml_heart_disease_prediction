from fastapi import APIRouter
from src.heart_prediction.service import ModelPrediction
from src.heart_prediction.schema import model_payload

route = APIRouter()
model = ModelPrediction()
@route.post("/model-prediction", status_code=200)
def model_prediction(payload: model_payload):

	result = model.predict(payload.model_dump())
	return {result}