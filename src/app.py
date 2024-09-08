from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    tax: float = 10.5
    
@app.post("/items/")
async def create_item(item: Item):
    return item