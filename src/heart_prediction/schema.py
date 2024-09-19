from pydantic import BaseModel


class model_payload(BaseModel):
    name: str
    surname: str
    health: str
    have_private_medic: str
    last_checkup: str
    last_exercise: str
    high_blood_presure: str
    use_cholesterol_medicine: str
    had_a_stroke: str
    kidney_disease: str
    diabetes: str
    urban_rural_status: str
    mental_health: str
    physical_activity: str
    had_depression: str
    aerobic_recomendation: str
    high_cholesterol: str
    asthma: str
    ethnicity: str
    sex: str
    age: str
    weight: str
    height: str
    race: str
    region: str
    medic: str
    consult: str