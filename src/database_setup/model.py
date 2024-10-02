import psycopg2


conn = psycopg2.connect(user = "postgres",
                        password = "VONmefjimlVoPExDyYwgvhFdSJJyRNOs",
                        host = "autorack.proxy.rlwy.net",
                        port = "45508")
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datacamp_courses table
cur.execute("""
            DROP SCHEMA tcc CASCADE;
            """)
# Make the changes to the database persistent
conn.commit()

cur.execute("""CREATE TABLE model_prediction_table(
            course_id SERIAL PRIMARY KEY,
            UUID UUID (50);
            course_name VARCHAR (50) UNIQUE NOT NULL,
            course_instructor VARCHAR (100) NOT NULL,
            topic VARCHAR (20) NOT NULL);
            """)
# Make the changes to the database persistent
conn.commit()
# Close cursor and communication with the database
cur.close()
conn.close()