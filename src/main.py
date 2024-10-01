import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.config_and_setup import GlobalVariables
from src.config_and_setup import route as health_check
from src.heart_prediction.route import route as model_prection_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permite qualquer método (GET, POST, etc.)
    allow_headers=["*"],  # Permite qualquer cabeçalho
)

global_variables = GlobalVariables()

app.include_router(health_check)
app.include_router(model_prection_route, prefix = os.environ["API_VERSION"])

# def create_exception_handler(
#     status_code: int, initial_detail: str
# ) -> Callable[[Request, ModelPredictionError], JSONResponse]:
#     detail = {"message": initial_detail}  # Using a dictionary to hold the detail

#     async def exception_handler(_: Request, exc: ModelPredictionError) -> JSONResponse:
#         if exc.message:
#             detail["message"] = exc.message

#         if exc.name:
#             detail["message"] = f"{detail['message']} [{exc.name}]"

#         logger.error(exc)
#         return JSONResponse(
#             status_code=status_code, content={"detail": detail["message"]}
#         )

#     return exception_handler
