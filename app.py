import requests
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = "asst_AQSHLWG4y7WjkvGqT2U6FRKD"  

@app.route('/consultar_inventario', methods=['POST'])
def consultar_inventario():
    user_query = request.json.get("consulta")

    url = f"https://api.openai.com/v1/assistants/{ASSISTANT_ID}/query"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "OpenAI-Beta": "assistants=v2"
    }
    data = {
        "query": user_query
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        respuesta = response.json().get("respuesta")
        return jsonify({"respuesta": respuesta})
    else:
        return jsonify({"error": "Error al consultar el asistente"}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

