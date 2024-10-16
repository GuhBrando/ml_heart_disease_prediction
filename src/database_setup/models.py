#from src.config_and_setup import *
import os
import psycopg2


conn = psycopg2.connect(user = "postgres",
                        password = os.environ["postgres_pass"],
                        host = "autorack.proxy.rlwy.net",
                        port = "45508",
                        database = "railway")
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

# cur.execute("DROP TABLE s_patient_name CASCADE")

cur.execute("""CREATE TABLE IF NOT EXISTS s_patient_name(
                ID BIGSERIAL PRIMARY KEY,
                name VARCHAR (100),
                surname VARCHAR (300),
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
                had_stroke VARCHAR (100)
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
                aerobic_recomentation VARCHAR (100)
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

cur.execute("""CREATE TABLE IF NOT EXISTS s_high_cholesterol(
                ID SMALLINT PRIMARY KEY,
                high_cholesterol VARCHAR (100)
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
                UUID uuid PRIMARY KEY,
                name_id BIGINT REFERENCES s_patient_name (ID),
                weight INTEGER,
                height SMALLINT,
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
                odate DATE
            );
            """)

# EXEMPLO

# -- Criar a tabela clientes
# CREATE TABLE clientes (
#     id SERIAL PRIMARY KEY,
#     nome VARCHAR(100)
# );

# -- Criar a tabela pedidos
# CREATE TABLE pedidos (
#     id SERIAL PRIMARY KEY,
#     cliente_id INT,
#     data DATE,
#     FOREIGN KEY (cliente_id) REFERENCES clientes(id)
# );

# -- Criar a tabela relatorio_pedidos com JOIN
# CREATE TABLE relatorio_pedidos AS
# SELECT 
#     c.id AS cliente_id,
#     c.nome AS cliente_nome,
#     p.id AS pedido_id,
#     p.data AS pedido_data
# FROM clientes c
# JOIN pedidos p ON c.id = p.cliente_id;

# -- Adicionar novos campos
# ALTER TABLE relatorio_pedidos
# ADD COLUMN status VARCHAR(50);

# -- Definir chaves estrangeiras
# ALTER TABLE relatorio_pedidos
# ADD CONSTRAINT fk_cliente
# FOREIGN KEY (cliente_id) REFERENCES clientes(id),
# ADD CONSTRAINT fk_pedido
# FOREIGN KEY (pedido_id) REFERENCES pedidos(id);


conn.commit()

cur.close()
conn.close()