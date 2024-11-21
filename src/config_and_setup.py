import json
import os
import logging
from fastapi import APIRouter, FastAPI

class ModelPredictionError(Exception):
    
    def __init__(self, message: str = "Service is unavailable", name: str = "ModelPredictionError") -> None:
        self.name = name
        self.message = message

        super().__init__(self.message, self.name)

class GlobalVariables():
    def __init__(self):
        os.environ["API_VERSION"] = "/api/1.0"

logger = logging.getLogger("my_app")
        
try:
    with open("src/postgres_setup.json", "r") as read_file:
        postgres_infos = json.load(read_file)
    os.environ["postgres_user"] = postgres_infos["username"]
    os.environ["postgres_pass"] = postgres_infos["password"]
except:
    print("ERROR")
    pass

app = FastAPI()
route = APIRouter()

@route.get("/")
def model_prediction():
    return {"status": "TCC - Projeto voltado para prever doencas cardiovasculares utilizando machine learning"}

@route.get("/health")
def model_prediction():
    return {"status": "alive"}