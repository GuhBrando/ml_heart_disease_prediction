import os

from fastapi import APIRouter

class GlobalVariables():
    def __init__(self):
        os.environ["API_VERSION"] = "/api/1.0"

route = APIRouter()

@route.get("/health")
async def model_prediction():
    return {"status": "alive"}