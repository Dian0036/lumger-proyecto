from flask import Flask, request, jsonify
import os
from connect_postgres import init_db, insert_idea, get_ideas

# Inicializa la aplicación Flask
app = Flask(__name__)

# Inicializa la base de datos al inicio
init_db()


# Ruta para obtener todas las ideas
@app.route("/ideas", methods=["GET"])
def get_all_ideas():
    try:
        ideas = get_ideas()
        return jsonify(ideas), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500


# Ruta para agregar una nueva idea
@app.route("/ideas", methods=["POST"])
def add_idea():
    try:
        data = request.get_json()
        title = data.get("title")
        description = data.get("description")
        insert_idea(title, description)
        return jsonify({"message": "Idea added successfully"}), 201
    except Exception as error:
        return jsonify({"error": str(error)}), 500


# Ruta base para verificar que el servidor funciona
@app.route("/")
def home():
    return "Hola, Lumger está funcionando correctamente!"


if __name__ == "__main__":
    app.run(debug=True, port=5002)
