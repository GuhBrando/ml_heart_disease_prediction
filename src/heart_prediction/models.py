
import os
import psycopg2
import uuid

def insert_values_into_table(name_id,
                            weight,
                            height,
                            health_id,
                            have_private_doctor_id,
                            last_chekup_id,
                            last_exercise_id,
                            high_blood_pressure_id,
                            use_cholesterol_medicine_id,
                            had_a_stroke_id,
                            had_depression_id,
                            kidney_disease_id,
                            diabetes_id,
                            urban_rural_status_id,
                            mental_health_id,
                            physical_activity_id,
                            aerobic_recommendation_id,
                            high_cholesterol_id,
                            asthma_id,
                            ethnicity_id,
                            sex_id,
                            age_id,
                            smoker_status_id,
                            is_heavy_drinker_id,
                            odate):
    conn = psycopg2.connect(user = "postgres", 
                        password = os.environ["postgres_pass"], 
                        host = "autorack.proxy.rlwy.net", 
                        port = "45508", 
                        database = "railway")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()
    cur.execute(f"""INSERT INTO s_model_prediction_results VALUES(
                    '{uuid.uuid4()}',
                    {name_id},
                    {weight},
                    {height},
                    {health_id},
                    {have_private_doctor_id},
                    {last_chekup_id},
                    {last_exercise_id},
                    {high_blood_pressure_id},
                    {use_cholesterol_medicine_id},
                    {had_a_stroke_id},
                    {had_depression_id},
                    {kidney_disease_id},
                    {diabetes_id},
                    {urban_rural_status_id},
                    {mental_health_id},
                    {physical_activity_id},
                    {aerobic_recommendation_id},
                    {high_cholesterol_id},
                    {asthma_id},
                    {ethnicity_id},
                    {sex_id},
                    {age_id},
                    {smoker_status_id},
                    {is_heavy_drinker_id},
                    '{odate}'
                    );
                    """)

    cur.close()
    conn.close()

insert_values_into_table(name_id = 0, 
                         sex_id = 1,  
                         age_id = 1,  
                         ethnicity_id = 1,  
                         height = 192,  
                         weight = 124,  
                         urban_rural_status_id = 1,  
                         health_id = 4,  
                         have_private_doctor_id = 1,  
                         last_chekup_id = 1,  
                         last_exercise_id = 1,  
                         high_blood_pressure_id = 1,  
                         use_cholesterol_medicine_id = 2,  
                         had_a_stroke_id = 2, 
                         kidney_disease_id = 2,  
                         diabetes_id = 3,  
                         mental_health_id = 1,  
                         physical_activity_id = 2,  
                         had_depression_id = 7,  
                         aerobic_recommendation_id = 2,  
                         high_cholesterol_id = 2,  
                         asthma_id = 1,  
                         smoker_status_id = 4,  
                         is_heavy_drinker_id = 2, 
                         odate = "2024-08-10")