import os

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class GlobalVariables():
    def __init__(self):
        os.environ["API_VERSION"] = "/api/1.0"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permite qualquer método (GET, POST, etc.)
    allow_headers=["*"],  # Permite qualquer cabeçalho
)

route = APIRouter()

@route.get("/")
async def model_prediction():
    return {"status": "TCC - Projeto voltado para prever doencas cardiovasculares utilizando machine learning"}

@route.get("/health")
async def model_prediction():
    return {"status": "alive"}