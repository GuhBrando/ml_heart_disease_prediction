import os

from fastapi import APIRouter, FastAPI
import logging

logger = logging.getLogger("my_app")

class ModelPredictionError(Exception):
    
    def __init__(self, message: str = "Service is unavailable", name: str = "ModelPredictionError") -> None:
        self.name = name
        self.message = message

        super().__init__(self.message, self.name)

app = FastAPI()

class GlobalVariables():
    def __init__(self):
        os.environ["API_VERSION"] = "/api/1.0"

route = APIRouter()

@route.get("/")
def model_prediction():
    return {"status": "TCC - Projeto voltado para prever doencas cardiovasculares utilizando machine learning"}

@route.get("/health")
def model_prediction():
    return {"status": "alive"}