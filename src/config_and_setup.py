import json
import os

from fastapi import APIRouter, FastAPI
import logging

import joblib

logger = logging.getLogger("my_app")

class ModelPredictionError(Exception):
    
    def __init__(self, message: str = "Service is unavailable", name: str = "ModelPredictionError") -> None:
        self.name = name
        self.message = message

        super().__init__(self.message, self.name)

app = FastAPI()
try:
    with open("src/postgres_setup.json", "r") as read_file:
        postgres_infos = json.load(read_file)
    os.environ["postgres_user"] = postgres_infos["username"]
    os.environ["postgres_pass"] = postgres_infos["password"]
except:
    print("ERROR")
    pass

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