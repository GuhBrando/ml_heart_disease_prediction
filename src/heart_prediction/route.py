def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from fastapi import APIRouter, HTTPException
import joblib
import numpy as np
from datetime import datetime, timedelta
import pytz

from .models import insert_values_into_table
from .exceptions import TypeConverterError
from .schema import model_payload

route = APIRouter()

@route.post("/model-prediction")
async def model_prediction(payload: model_payload):
	calibrated_model = joblib.load(open(r"./models/modeloRandomForestCalibrado.pkl", "rb"))
	scaler = joblib.load(open(r"./models/scalerCalibrado.pkl", "rb"))

	try:
		name = payload.name
		surname = payload.surname
		email = payload.email
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
		aerobic_recommendation = int(payload.aerobic_recommendation)
		high_cholesterol = int(payload.high_cholesterol)
		asthma = int(payload.asthma)
		ethnicity = int(payload.ethnicity)
		sex = int(payload.sex)
		age = int(payload.age)
		height = int(payload.height)
		weight = int(payload.weight)
		smoker_status = int(payload.smoker_status)
		is_heavy_drinker = int(payload.is_heavy_drinker)
	except ValueError:
		raise HTTPException(status_code=400, detail="Erro ao converter valores para int")


	columns = ['saude','temMedicoPrivado', 'dataUltimoCheckup', 'exercicioUltimoMes', 
			'pressaoAlta', 'remedioColesterol', 'teveAVC', 'teveDepressao', 
			'teveDoencaRenal', 'diabetico', 'areaOndeVive', 'saudeMental', 
			'atividadesFisicas', 'recomendacaoAerobica', 'colesterolAlto', 'asma', 
			'etnia', 'genero', 'idade','altura',
			'peso', 'fumante', 'alcoolatra']
	new_input = pd.DataFrame([[health, have_private_doctor, last_checkup, last_exercise,
							high_blood_pressure, use_cholesterol_medicine, had_a_stroke, had_depression, kidney_disease, 
							diabetes, urban_rural_status, mental_health, physical_activity, 
							aerobic_recommendation, high_cholesterol, asthma, ethnicity, 
							sex, age, height, weight,
							smoker_status, is_heavy_drinker]], columns=columns)
	new_input_scaled = pd.DataFrame(scaler.transform(new_input), columns=new_input.columns)

	brazil_timezone = pytz.timezone("America/Sao_Paulo") 
	local_timezone = datetime.now(brazil_timezone) + timedelta(days=1)
	current_date_time = local_timezone.strftime("%Y-%m-%d")

	probabilities = calibrated_model.predict_proba(new_input_scaled)[0]
	predicted_class = np.argmax(probabilities)

	confidence = probabilities[predicted_class] * 100

	insert_values_into_table(name = name,
							 surname = surname, 
							 sex_id = sex,  
							 age_id = age,  
							 ethnicity_id = ethnicity,  
							 height = height,  
							 weight = weight,  
							 urban_rural_status_id = urban_rural_status,  
							 health_id = health,  
							 have_private_doctor_id = have_private_doctor,  
							 last_checkup_id = last_checkup,  
							 last_exercise_id = last_exercise,  
							 high_blood_pressure_id = high_blood_pressure,  
							 use_cholesterol_medicine_id = use_cholesterol_medicine,  
							 had_a_stroke_id = had_a_stroke, 
							 kidney_disease_id = kidney_disease,  
							 diabetes_id = diabetes,  
							 mental_health_id = mental_health,  
							 physical_activity_id = physical_activity,  
							 had_depression_id = had_depression,  
							 aerobic_recommendation_id = aerobic_recommendation,  
							 high_cholesterol_id = high_cholesterol,  
							 asthma_id = asthma,  
							 smoker_status_id = smoker_status,  
							 is_heavy_drinker_id = is_heavy_drinker,
							 model_prediction_result = predicted_class,
							 model_confidence_result = round(confidence, 2),
							 email = email,
							 odate = str(current_date_time)
							)

	resultado = "Você possui um risco significativo de desenvolver uma doença cardíaca" if predicted_class == 1 else "Você não possui um risco significativo de desenvolver uma doença cardiovascular"

	return {"input": str(payload),
			"output": f"Previsão = {resultado}, com uma confiança de {confidence:.2f}%"}