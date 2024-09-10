from fastapi import APIRouter

from .schema import model_payload

route = APIRouter()

@route.post("/model-prediction")
async def model_prediction(payload: model_payload):
    return "Alive"