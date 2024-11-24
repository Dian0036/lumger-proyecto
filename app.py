from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Configuración de conexión a PostgreSQL
def get_db_connection():
    connection = psycopg2.connect(
        dbname="lumger_db",
        user="postgres",
        password="Djyira0.36",  # Cambia por tu contraseña
        host="localhost",
        port="5432"
    )
    return connection

# Ruta base para verificar que el servidor funciona
@app.route("/")
def home():
    return "Hola, Lumger está funcionando correctamente!"

# Ruta para obtener todas las ideas
@app.route('/ideas', methods=['GET'])
def get_ideas():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM ideas')
        ideas = cursor.fetchall()
        cursor.close()
        connection.close()
        result = [
            {"id": idea[0], "title": idea[1], "description": idea[2], "created_at": idea[3]}
            for idea in ideas
        ]
        return jsonify(result)
    except Exception as error:
        return jsonify({"error": str(error)})

# Ruta para agregar una idea
@app.route('/ideas', methods=['POST'])
def add_idea():
    try:
        data = request.json
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO ideas (title, description) VALUES (%s, %s) RETURNING id',
            (data['title'], data['description'])
        )
        idea_id = cursor.fetchone()[0]
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Idea creada con éxito", "id": idea_id})
    except Exception as error:
        return jsonify({"error": str(error)})

# Ruta para obtener una idea por ID
@app.route('/ideas/<int:idea_id>', methods=['GET'])
def get_idea_by_id(idea_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM ideas WHERE id = %s', (idea_id,))
        idea = cursor.fetchone()
        cursor.close()
        connection.close()
        if idea:
            result = {
                "id": idea[0],
                "title": idea[1],
                "description": idea[2],
                "created_at": idea[3]
            }
            return jsonify(result)
        else:
            return jsonify({"error": "Idea no encontrada"}), 404
    except Exception as error:
        return jsonify({"error": str(error)})

if __name__ == "__main__":
    app.run(debug=True, port=5002)
    from flask import Flask, request, jsonify
import os
from connect_postgres import init_db, insert_idea, get_ideas

app = Flask(__name__)
init_db()

@app.route("/ideas", methods=["GET"])
def get_all_ideas():
    ideas = get_ideas()
    return jsonify(ideas), 200

@app.route("/ideas", methods=["POST"])
def add_idea():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    insert_idea(title, description)
    return jsonify({"message": "Idea added"}), 201

if __name__ == "__main__":
    app.run(debug=True)