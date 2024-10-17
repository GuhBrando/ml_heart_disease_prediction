
import os
import psycopg2
import uuid

def insert_values_into_table(name,
                             surname,
                             weight,
                             height,
                             health_id,
                             have_private_doctor_id,
                             last_checkup_id,
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
                             model_prediction_result,
                             model_confidence_result,
                             email,
                             odate):
    conn = psycopg2.connect(user = "postgres", 
                        password = os.environ["postgres_pass"], 
                        host = "autorack.proxy.rlwy.net", 
                        port = "45508", 
                        database = "railway")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()

    cur.execute(f"SELECT id FROM s_patient_name WHERE name = '{name}' AND surname = '{surname}' AND email = '{email}'")
    row_id = cur.fetchall()[0][0]
    if len(row_id) > 0:
        row_id = row_id
        cur.execute(f"""UPDATE s_patient_name 
                    SET height = {height},
                    weight = {weight},
                    sex = {sex_id}
                    WHERE id = {row_id};
                    """
                    )
    else:
        cur.execute(f"SELECT MAX(id) FROM s_patient_name")
        max_id = cur.fetchall()[0][0]
        row_id = int(max_id) + 1 if max_id != None else 0
        cur.execute(f"""INSERT INTO s_patient_name VALUES (
                    {row_id},
                    '{name}',
                    '{surname}',
                    '{email}',
                    {height},
                    {weight},
                    {sex_id}
                    )
            """
            )
    cur.execute(f"""INSERT INTO s_model_prediction_results VALUES(
                    '{uuid.uuid4()}',
                    {row_id},
                    {weight},
                    {height},
                    {health_id},
                    {have_private_doctor_id},
                    {last_checkup_id},
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
                    {model_prediction_result},
                    {model_confidence_result},
                    '{odate}'
                    );
                    """)

    cur.close()
    conn.close()