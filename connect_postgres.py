import psycopg2
from psycopg2.extras import RealDictCursor
import os

# Obtiene la URL de la base de datos desde el archivo .env
DATABASE_URL = os.getenv("DATABASE_URL")  # No pongas la URL directa aquí.

# Imprime la URL para verificar que se está cargando correctamente.
print(f"DATABASE_URL: {DATABASE_URL}")

# Asegúrate de que DATABASE_URL esté configurada
if not DATABASE_URL:
    raise ValueError("La variable de entorno DATABASE_URL no está configurada.")

# Inicializa la base de datos y crea la tabla si no existe
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

# Obtiene todas las ideas de la base de datos
def get_ideas():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    cur = conn.cursor()
    cur.execute("SELECT * FROM ideas;")
    ideas = cur.fetchall()
    cur.close()
    conn.close()
    return ideas

# Inserta una nueva idea en la base de datos
def insert_idea(title, description):
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("INSERT INTO ideas (title, description) VALUES (%s, %s);", (title, description))
    conn.commit()
    cur.close()
    conn.close()