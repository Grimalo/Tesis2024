from flask import Flask, request, jsonify
import openai
import os

# Inicializa la aplicación Flask
app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

ASSISTANT_ID = "asst_AQSHLWG4y7WjkvGqT2U6FRKD"

def consultar_asistente(prompt):
    # Crea un thread con el Assistant específico
    thread = openai.Thread.create(assistant=ASSISTANT_ID)

    # Añade el mensaje del usuario al thread
    openai.Thread.add_message(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    response = openai.Thread.run(thread_id=thread.id)
    return response['choices'][0]['message']['content']

@app.route("/consultar_asistente", methods=["POST"])
def consultar_asistente_endpoint():
    data = request.json
    prompt = data.get("prompt")
    if prompt:
        respuesta = consultar_asistente(prompt)
        return jsonify({"respuesta": respuesta})
    else:
        return jsonify({"error": "No se encontró el campo 'prompt' en la solicitud."}), 400

# Punto de entrada para iniciar la aplicación
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
