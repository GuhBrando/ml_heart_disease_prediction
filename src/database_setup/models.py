#from ..config_and_setup import *
import json
import os
import psycopg2

conn = psycopg2.connect(user = "postgres",
                        password = os.environ["postgres_pass"],
                        host = "autorack.proxy.rlwy.net",
                        port = "45508",
                        database = "railway")
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS s_patient_name(
                ID BIGSERIAL PRIMARY KEY,
                name VARCHAR (100),
                surname VARCHAR (300),
                email VARCHAR (300),
                height SMALLINT,
                weight INTEGER,
                sex SMALLINT REFERENCES s_sex (ID)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_health(
                ID SMALLINT PRIMARY KEY,
                health VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_private_doctor(
                ID SMALLINT PRIMARY KEY,
                have_private_doctor VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_last_checkup(
                ID SMALLINT PRIMARY KEY,
                last_checkup VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_high_blood_pressure(
                ID SMALLINT PRIMARY KEY,
                high_blood_pressure VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_use_cholesterol_meds(
                ID SMALLINT PRIMARY KEY,
                use_cholesterol_med VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_had_stroke(
                ID SMALLINT PRIMARY KEY,
                had_stroke VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_had_depression(
                ID SMALLINT PRIMARY KEY,
                had_depression VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_kidney_disease(
                ID SMALLINT PRIMARY KEY,
                kidney_disease VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_diabetes(
                ID SMALLINT PRIMARY KEY,
                diabetes VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_urban_rural_status(
                ID SMALLINT PRIMARY KEY,
                urban_rural_status VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_physical_activity(
                ID SMALLINT PRIMARY KEY,
                physical_activity VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_aerobic_recommendation(
                ID SMALLINT PRIMARY KEY,
                aerobic_recommendation VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_high_cholesterol(
                ID SMALLINT PRIMARY KEY,
                high_cholesterol VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_asthma(
                ID SMALLINT PRIMARY KEY,
                asthma VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_ethnicity(
                ID SMALLINT PRIMARY KEY,
                ethnicity VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_sex(
                ID SMALLINT PRIMARY KEY,
                sex VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_age(
                ID SMALLINT PRIMARY KEY,
                age VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_mental_health(
                ID SMALLINT PRIMARY KEY,
                mental_health VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_smoker_status(
                ID SMALLINT PRIMARY KEY,
                smoker_status VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_heavy_drinker(
                ID SMALLINT PRIMARY KEY,
                heavy_drinker VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_last_exercise(
                ID SMALLINT PRIMARY KEY,
                last_exercise VARCHAR (100)
            );
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS s_model_prediction_results(
                UUID uuid,
                name_id BIGINT REFERENCES s_patient_name (ID),
                weight INTEGER NOT NULL,
                height SMALLINT NOT NULL,
                health_id SMALLINT REFERENCES s_health (ID),
                have_private_doctor_id SMALLINT REFERENCES s_private_doctor (ID),
                last_checkup_id SMALLINT REFERENCES s_last_checkup (ID),
                last_exercise_id SMALLINT REFERENCES s_last_exercise (ID),
                high_blood_pressure_id SMALLINT REFERENCES s_high_blood_pressure (ID),
                use_cholesterol_meds_id SMALLINT REFERENCES s_use_cholesterol_meds (ID),
                had_stroke_id SMALLINT REFERENCES s_had_stroke (ID),
                had_depression_id SMALLINT REFERENCES s_had_depression (ID),
                kidney_disease_id SMALLINT REFERENCES s_kidney_disease (ID),
                diabetes_id SMALLINT REFERENCES s_diabetes (ID),
                urban_rural_status_id SMALLINT REFERENCES s_urban_rural_status (ID),
                mental_health_id SMALLINT REFERENCES s_mental_health (ID),
                physical_activity_id SMALLINT REFERENCES s_physical_activity (ID),
                aerobic_recommendation_id SMALLINT REFERENCES s_aerobic_recommendation (ID),
                high_cholesterol_id SMALLINT REFERENCES s_high_cholesterol (ID),
                asthma_id SMALLINT REFERENCES s_asthma (ID),
                ethnicity_id SMALLINT REFERENCES s_ethnicity (ID),
                sex_id SMALLINT REFERENCES s_sex (ID),
                age_id SMALLINT REFERENCES s_age (ID),
                smoker_status_id SMALLINT REFERENCES s_smoker_status (ID),
                is_heavy_drinker_id SMALLINT REFERENCES s_heavy_drinker (ID),
                model_prediction_result SMALLINT NOT NULL,
                model_confidence_result REAL NOT NULL,
                odate DATE NOT NULL,
                PRIMARY KEY (UUID, odate)
            ) PARTITION BY RANGE (odate);
            """)

cur.execute("""create or replace view g_model_true_information AS
                SELECT 
                    s_patient_name.name AS name,
                    s_patient_name.surname AS surname,
                    s_model_prediction_results.weight AS weight,
                    s_model_prediction_results.height AS height,
                    s_health.health AS health,
                    s_private_doctor.have_private_doctor AS have_private_doctor,
                    s_last_checkup.last_checkup AS last_checkup,
                    s_last_exercise.last_exercise AS last_exercise,
                    s_high_blood_pressure.high_blood_pressure AS high_blood_pressure,
                    s_use_cholesterol_meds.use_cholesterol_med AS use_cholesterol_med,
                    s_had_stroke.had_stroke AS had_stroke,
                    s_had_depression.had_depression AS had_depression,
                    s_kidney_disease.kidney_disease AS kidney_disease,
                    s_diabetes.diabetes AS diabetes,
                    s_urban_rural_status.urban_rural_status AS urban_rural_status,
                    s_mental_health.mental_health AS mental_health,
                    s_physical_activity.physical_activity AS physical_activity,
                    s_aerobic_recommendation.aerobic_recommendation AS aerobic_recommendation,
                    s_high_cholesterol.high_cholesterol AS high_cholesterol,
                    s_asthma.asthma AS asthma,
                    s_ethnicity.ethnicity AS ethnicity,
                    s_sex.sex AS sex,
                    s_age.age AS age,
                    s_smoker_status.smoker_status AS smoker_status,
                    s_heavy_drinker.heavy_drinker AS heavy_drinker,
                    model_prediction_result,
                    model_confidence_result,
                    odate
                FROM s_model_prediction_results
                JOIN s_patient_name ON s_model_prediction_results.name_id = s_patient_name.id
                JOIN s_age ON s_model_prediction_results.age_id = s_age.id
                JOIN s_health ON s_model_prediction_results.health_id = s_health.id
                JOIN s_private_doctor ON s_model_prediction_results.have_private_doctor_id = s_private_doctor.id
                JOIN s_last_checkup ON s_model_prediction_results.last_checkup_id =  s_last_checkup.id
                JOIN s_last_exercise ON s_model_prediction_results.last_exercise_id =  s_last_exercise.id
                JOIN s_high_blood_pressure ON s_model_prediction_results.high_blood_pressure_id =  s_high_blood_pressure.id
                JOIN s_use_cholesterol_meds ON s_model_prediction_results.use_cholesterol_meds_id =  s_use_cholesterol_meds.id
                JOIN s_had_stroke ON s_model_prediction_results.had_stroke_id =  s_had_stroke.id
                JOIN s_had_depression ON s_model_prediction_results.had_depression_id =  s_had_depression.id
                JOIN s_kidney_disease ON s_model_prediction_results.kidney_disease_id =  s_kidney_disease.id
                JOIN s_diabetes ON s_model_prediction_results.diabetes_id =  s_diabetes.id
                JOIN s_urban_rural_status ON s_model_prediction_results.urban_rural_status_id =  s_urban_rural_status.id
                JOIN s_mental_health ON s_model_prediction_results.mental_health_id =  s_mental_health.id
                JOIN s_physical_activity ON s_model_prediction_results.physical_activity_id =  s_physical_activity.id
                JOIN s_aerobic_recommendation ON s_model_prediction_results.aerobic_recommendation_id =  s_aerobic_recommendation.id
                JOIN s_high_cholesterol ON s_model_prediction_results.high_cholesterol_id =  s_high_cholesterol.id
                JOIN s_asthma ON s_model_prediction_results.asthma_id =  s_asthma.id
                JOIN s_ethnicity ON s_model_prediction_results.ethnicity_id =  s_ethnicity.id
                JOIN s_sex ON s_model_prediction_results.sex_id =  s_sex.id
                JOIN s_smoker_status ON s_model_prediction_results.smoker_status_id =  s_smoker_status.id
                JOIN s_heavy_drinker ON s_model_prediction_results.is_heavy_drinker_id =  s_heavy_drinker.id
            ;""")


cur.execute("""CREATE TABLE IF NOT EXISTS s_model_prediction_results_10_2024 PARTITION OF s_model_prediction_results
                FOR VALUES FROM ('2024-10-01') TO ('2024-10-31');""")

cur.execute("""CREATE TABLE IF NOT EXISTS s_model_prediction_results_11_2024 PARTITION OF s_model_prediction_results
                FOR VALUES FROM ('2024-11-01') TO ('2024-11-30');""")

cur.execute("""CREATE TABLE IF NOT EXISTS s_model_prediction_results_12_2024 PARTITION OF s_model_prediction_results
                FOR VALUES FROM ('2024-12-01') TO ('2024-12-31');""")

conn.commit()

cur.close()
conn.close()