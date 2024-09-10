import os
from fastapi import FastAPI
from pydantic import BaseModel
from src.config_and_setup import GlobalVariables
from src.heart_prediction.route import route as model_prection_route

app = FastAPI()
global_variables = GlobalVariables()

app.include_router(model_prection_route, prefix = os.environ["API_VERSION"])