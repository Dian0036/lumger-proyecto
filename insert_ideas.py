import psycopg2

# Conexión a la base de datos
try:
    connection = psycopg2.connect(
        dbname="lumger_db",   
        user="postgres",      
        password="Djyira0.36", 
        host="localhost",     
        port="5432"           
    )
    cursor = connection.cursor()

    # Inserción de datos
    insert_query = """
    INSERT INTO ideas (title, description)
    VALUES (%s, %s)
    RETURNING id;
    """
    values = ("Nueva Idea", "Esta es la descripción de la idea.")
    cursor.execute(insert_query, values)

    # Obtener el ID del registro insertado
    idea_id = cursor.fetchone()[0]
    connection.commit()
    print(f"Idea insertada con ID: {idea_id}")

except Exception as error:
    print("Error al insertar en la base de datos:", error)

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("Conexión cerrada.")
