from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

ASSISTANT_ID = "asst_AQSHLWG4y7WjkvGqT2U6FRKD"

def consultar_asistente(prompt):
    response = openai.AssistantCompletion.create(
        assistant=ASSISTANT_ID,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

@app.route("/consultar_asistente", methods=["POST"])
def consultar_asistente_endpoint():
    data = request.json
    prompt = data.get("prompt")
    if prompt:
        respuesta = consultar_asistente(prompt)
        return jsonify({"respuesta": respuesta})
    else:
        return jsonify({"error": "No se encontró el campo 'prompt' en la solicitud."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

