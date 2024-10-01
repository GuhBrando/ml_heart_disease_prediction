import os

from fastapi import APIRouter, FastAPI

app = FastAPI()

class GlobalVariables():
    def __init__(self):
        os.environ["API_VERSION"] = "/api/1.0"

route = APIRouter()

@route.get("/")
async def model_prediction():
    return {"status": "TCC - Projeto voltado para prever doencas cardiovasculares utilizando machine learning"}

@route.get("/health")
async def model_prediction():
    return {"status": "alive"}