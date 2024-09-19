from pydantic import BaseModel


class model_payload(BaseModel):
    name: str
    nickname: str
    sex: str
    age: str
    weight: str
    height: str
    race: str
    region: str
    medic: str
    consult: str