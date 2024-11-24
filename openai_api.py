import openai
import os

# Configuración de la clave API
openai.api_key = os.getenv("OPENAI_API_KEY")

def generar_idea(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error al generar idea: {e}"
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()