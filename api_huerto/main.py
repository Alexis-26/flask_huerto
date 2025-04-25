from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)
# MONGO_URI = os.getenv("MONGO_URI")
# DB_NAME = os.getenv("DB_NAME")


# Conexión a MongoDB (ajusta según tu config)
client = MongoClient("mongodb+srv://alexis:Chokart$2978@cluster0.dx3fa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["sensores_db"]
coleccion = db["lecturas"]

@app.route('/datos', methods=['POST'])
def recibir_datos():
    data = request.get_json()
    print("Datos recibidos:", data)

    # Aquí iría la lógica para guardarlos en tu base de datos
    if data:
        data['timestamp'] = datetime.now()
        coleccion.insert_one(data)
        return jsonify({"mensaje": "Datos guardados en MongoDB"}), 200
    else:
        return jsonify({"error": "No se recibieron datos válidos"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
