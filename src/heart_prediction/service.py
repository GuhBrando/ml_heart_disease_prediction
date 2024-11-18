def warn(*args, **kwargs):
    pass
import os
import warnings
warnings.warn = warn

import pandas as pd
from fastapi import HTTPException
import joblib
import numpy as np
from datetime import datetime, timedelta
import pytz

from .models import insert_values_into_table

class ModelPrediction:
    def __init__(self):
        self.calibrated_model = joblib.load(open(r"./models/modeloRandomForestCalibrado.pkl", "rb"))
        self.scaler = joblib.load(open(r"./models/scalerCalibrado.pkl", "rb"))
        self.columns = ['saude','temMedicoPrivado', 'dataUltimoCheckup', 'exercicioUltimoMes', 
                        'pressaoAlta', 'remedioColesterol', 'teveAVC', 'teveDepressao', 
                        'teveDoencaRenal', 'diabetico', 'areaOndeVive', 'saudeMental', 
                        'atividadesFisicas', 'recomendacaoAerobica', 'colesterolAlto', 'asma', 
                        'etnia', 'genero', 'idade','altura',
                        'peso', 'fumante', 'alcoolatra']

    def _define_and_validate_payload(self, 
                                    name: str, 
                                    surname: str, 
                                    email: str, 
                                    health: str, 
                                    have_private_doctor: str, 
                                    last_checkup: str, 
                                    last_exercise: str, 
                                    high_blood_pressure: str, 
                                    use_cholesterol_medicine: str, 
                                    had_a_stroke: str,
                                    had_depression: str,
                                    kidney_disease: str,
                                    diabetes: str,
                                    urban_rural_status: str,
                                    mental_health: str,
                                    physical_activity: str,
                                    aerobic_recommendation: str,
                                    high_cholesterol: str,
                                    asthma: str,
                                    ethnicity: str,
                                    sex: str,
                                    age: str,
                                    height: str,
                                    weight: str,
                                    smoker_status: str,
                                    is_heavy_drinker: str
                                ) -> None:
            try:
                self.name = name
                self.surname = surname
                self.email = email
                self.health = int(health)
                self.have_private_doctor = int(have_private_doctor)
                self.last_checkup = int(last_checkup)
                self.last_exercise = int(last_exercise)
                self.high_blood_pressure = int(high_blood_pressure)
                self.use_cholesterol_medicine = int(use_cholesterol_medicine)
                self.had_a_stroke = int(had_a_stroke)
                self.had_depression = int(had_depression)
                self.kidney_disease = int(kidney_disease)
                self.diabetes = int(diabetes)
                self.urban_rural_status = int(urban_rural_status)
                self.mental_health = int(mental_health)
                self.physical_activity = int(physical_activity)
                self.aerobic_recommendation = int(aerobic_recommendation)
                self.high_cholesterol = int(high_cholesterol)
                self.asthma = int(asthma)
                self.ethnicity = int(ethnicity)
                self.sex = int(sex)
                self.age = int(age)
                self.height = int(height)
                self.weight = int(weight)
                self.smoker_status = int(smoker_status)
                self.is_heavy_drinker = int(is_heavy_drinker)
            except ValueError:
                raise HTTPException(status_code=400, detail="Erro ao converter valores para int")

    def predict(self, payload):
        self._define_and_validate_payload(**payload)

        new_input = pd.DataFrame([[self.health, self.have_private_doctor, self.last_checkup, self.last_exercise,
                                self.high_blood_pressure, self.use_cholesterol_medicine, 
                                self.had_a_stroke, self.had_depression, self.kidney_disease, 
                                self.diabetes, self.urban_rural_status, self.mental_health, 
                                self.physical_activity, self.aerobic_recommendation, 
                                self.high_cholesterol, self.asthma, self.ethnicity, 
                                self.sex, self.age, self.height, self.weight,self.smoker_status, 
                                self.is_heavy_drinker]], columns=self.columns)
        new_input_scaled = pd.DataFrame(self.scaler.transform(new_input), columns=new_input.columns)

        brazil_timezone = pytz.timezone("America/Sao_Paulo") 
        local_timezone = datetime.now(brazil_timezone) + timedelta(days=1)
        current_date_time = local_timezone.strftime("%Y-%m-%d")

        probabilities = self.calibrated_model.predict_proba(new_input_scaled)[0]
        predicted_class = np.argmax(probabilities)

        confidence = probabilities[predicted_class] * 100
        insert_values_into_table(name = self.name,
                                surname = self.surname, 
                                sex_id = self.sex,  
                                age_id = self.age,  
                                ethnicity_id = self.ethnicity,  
                                height = self.height,  
                                weight = self.weight,  
                                urban_rural_status_id = self.urban_rural_status,  
                                health_id = self.health,  
                                have_private_doctor_id = self.have_private_doctor,  
                                last_checkup_id = self.last_checkup,  
                                last_exercise_id = self.last_exercise,  
                                high_blood_pressure_id = self.high_blood_pressure,  
                                use_cholesterol_medicine_id = self.use_cholesterol_medicine,  
                                had_a_stroke_id = self.had_a_stroke, 
                                kidney_disease_id = self.kidney_disease,  
                                diabetes_id = self.diabetes,  
                                mental_health_id = self.mental_health,  
                                physical_activity_id = self.physical_activity,  
                                had_depression_id = self.had_depression,  
                                aerobic_recommendation_id = self.aerobic_recommendation,  
                                high_cholesterol_id = self.high_cholesterol,  
                                asthma_id = self.asthma,  
                                smoker_status_id = self.smoker_status,  
                                is_heavy_drinker_id = self.is_heavy_drinker,
                                model_prediction_result = predicted_class,
                                model_confidence_result = round(confidence, 2),
                                email = self.email,
                                odate = str(current_date_time)
                                )

        resultado = "Você possui um risco significativo de desenvolver uma doença cardiovascular" if predicted_class == 1 else "Você não possui um risco significativo de desenvolver uma doença cardiovascular"
