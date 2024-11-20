import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config_and_setup import GlobalVariables
from src.config_and_setup import route as health_check
from src.heart_prediction.route import route as model_prection_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

global_variables = GlobalVariables()
from src.database_setup.models import *

app.include_router(health_check)
app.include_router(model_prection_route, prefix = os.environ["API_VERSION"])