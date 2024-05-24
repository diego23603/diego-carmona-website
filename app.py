from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# Configuración de la conexión a MongoDB (modifica según tus credenciales)
client = MongoClient('mongodb://localhost:27017/')  # Cambia a tu URI de MongoDB si es diferente
db = client['MiBaseDeDatos']
collection = db['MiColeccion']

@app.route('/')
def index():
    return '¡Hola, Azure!'

@app.route('/items', methods=['GET'])
def get_items():
    items = list(collection.find({}, {'_id': 0}))
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    collection.insert_one(item)
    return jsonify(item), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
