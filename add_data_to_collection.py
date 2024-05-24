import pymongo

def add_data_to_collection():
    # URI de conexión
    uri = "mongodb+srv://dcarru9:AEUFqcbKYXzHPqHs@cluster0.qnzmtv6.mongodb.net/?retryWrites=true&w=majority"

    # Conexión a la base de datos
    client = pymongo.MongoClient(uri)

    # Seleccionar la base de datos y la colección
    db = client.mydatabase  # Reemplaza "mydatabase" con el nombre de tu base de datos
    collection = db.rutas   # Reemplaza "rutas" con el nombre de tu colección

    # Datos a insertar (documento de ejemplo)
    data = {
        "ruta": "Ruta 1",
        "origen": "Ciudad A",
        "destino": "Ciudad B",
        "distancia": 100
    }

    # Insertar un solo documento
    result = collection.insert_one(data)
    print("Documento insertado con el ID:", result.inserted_id)

    # Datos para insertar múltiples documentos (lista de ejemplos)
    more_data = [
        {"ruta": "Ruta 2", "origen": "Ciudad B", "destino": "Ciudad C", "distancia": 150},
        {"ruta": "Ruta 3", "origen": "Ciudad C", "destino": "Ciudad D", "distancia": 200}
    ]

    # Insertar varios documentos
    result = collection.insert_many(more_data)
    print("Documentos insertados con los IDs:", result.inserted_ids)

if __name__ == "__main__":
    add_data_to_collection()
