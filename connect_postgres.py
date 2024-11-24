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

DATABASE_URL = os.getenv("DATABASE_URL")


def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ideas (
            id SERIAL PRIMARY KEY,
            title TEXT,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )
    conn.commit()
    conn.close()


def insert_idea(title, description):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ideas (title, description) VALUES (%s, %s)", (title, description)
    )
    conn.commit()
    conn.close()


def get_ideas():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ideas")
    ideas = cursor.fetchall()
    conn.close()
    return ideas
