import pandas as pd
from fastapi import APIRouter
import joblib
import numpy as np

from .schema import model_payload

route = APIRouter()

@route.post("/model-prediction")
async def model_prediction(payload: model_payload):
    calibrated_model = joblib.load(open(r"./models/modeloRandomForestCalibrado.pkl", "rb"))
    scaler = joblib.load(open(r"./models/scalerCalibrado.pkl", "rb"))

    health = int(payload.health)
    have_private_doctor = int(payload.have_private_doctor)
    last_checkup = int(payload.last_checkup)
    last_exercise = int(payload.last_exercise)
    high_blood_pressure = int(payload.high_blood_pressure)
    use_cholesterol_medicine = int(payload.use_cholesterol_medicine)
    had_a_stroke = int(payload.had_a_stroke)
    had_depression = int(payload.had_depression)
    kidney_disease = int(payload.kidney_disease)
    diabetes = int(payload.diabetes)
    urban_rural_status = int(payload.urban_rural_status)
    mental_health = int(payload.mental_health)
    physical_activity = int(payload.physical_activity)
    aerobic_recomendation = int(payload.aerobic_recomendation)
    high_cholesterol = int(payload.high_cholesterol)
    asthma = int(payload.asthma)
    ethnicity = int(payload.ethnicity)
    sex = int(payload.sex)
    age = int(payload.age)
    height = int(payload.height)
    weight = int(payload.weight)
    smoker_status = int(payload.smoker_status)
    is_heavy_drinker = int(payload.is_heavy_drinker)


    columns = ['saude','temMedicoPrivado', 'dataUltimoCheckup', 'exercicioUltimoMes', 
           'pressaoAlta', 'remedioColesterol', 'teveAVC', 'teveDepressao', 
           'teveDoencaRenal', 'diabetico', 'areaOndeVive', 'saudeMental', 
           'atividadesFisicas', 'recomendacaoAerobica', 'colesterolAlto', 'asma', 
           'etnia', 'genero', 'idade','altura',
           'peso', 'fumante', 'alcoolatra']
    new_input = pd.DataFrame([[health, have_private_doctor, last_checkup, last_exercise,
                           high_blood_pressure, use_cholesterol_medicine, had_a_stroke, had_depression, kidney_disease, 
                           diabetes, urban_rural_status, mental_health, physical_activity, 
                           aerobic_recomendation, high_cholesterol, asthma, ethnicity, 
                           sex, age, height, weight,
                           smoker_status, is_heavy_drinker]], columns=columns)
    new_input_scaled = pd.DataFrame(scaler.transform(new_input), columns=new_input.columns)

    probabilities = calibrated_model.predict_proba(new_input_scaled)[0]
    predicted_class = np.argmax(probabilities)

    confidence = probabilities[predicted_class] * 100

    resultado = "Você possui um risco significativo de desenvolver uma doença cardíaca" if predicted_class == 1 else "Você não possui um risco significativo de desenvolver uma doença cardiovascular"

    return {"input": str(payload),
            "output": f"Previsão = {resultado}, com uma confiança de {confidence:.2f}%"}