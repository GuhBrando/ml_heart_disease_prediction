from pydantic import BaseModel


class model_payload(BaseModel):
    name: str
    price: float
    tax: float = 10.5