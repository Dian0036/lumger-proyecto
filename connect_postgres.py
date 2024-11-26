import psycopg2

try:
    # Conecta a tu base de datos PostgreSQL
    connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Djyira0.36",
        host="localhost",
        port="5432",
    )
    print("¡Conexión exitosa a PostgreSQL!")
except Exception as error:
    print("Error al conectar a PostgreSQL:", error)
finally:
    if "connection" in locals() and connection:
        connection.close()
        print("Conexión cerrada.")
        import psycopg2
import psycopg2
from psycopg2.extras import RealDictCursor
import os

DATABASE_URL = os.getenv("DATABASE_URL")  # Asegúrate de que esté configurado correctamente.

def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ideas (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def get_ideas():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    cur = conn.cursor()
    cur.execute("SELECT * FROM ideas;")
    ideas = cur.fetchall()
    cur.close()
    conn.close()
    return ideas

def insert_idea(title, description):
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("INSERT INTO ideas (title, description) VALUES (%s, %s);", (title, description))
    conn.commit()
    cur.close()
    conn.close()