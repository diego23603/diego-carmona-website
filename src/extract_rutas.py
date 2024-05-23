import pymongo

def connect_to_mongodb():
    # URI de conexión
    uri = "mongodb+srv://dcarru9:AEUFqcbKYXzHPqHs@cluster0.qnzmtv6.mongodb.net/?retryWrites=true&w=majority"

    # Conexión a la base de datos
    client = pymongo.MongoClient(uri)

    return client

def filter_routes_by_origin_or_destination(origin_or_destination, collection):
    # Filtrar rutas por origen o destino
    filtered_routes = collection.find({"$or": [{"origen": origin_or_destination}, {"destino": origin_or_destination}]})
    for route in filtered_routes:
        print(route)

def calculate_route_statistics(collection):
    # Calcular estadísticas de las rutas
    total_distance = 0
    num_routes = 0
    max_distance = 0
    min_distance = float('inf')

    routes = collection.find()
    for route in routes:
        total_distance += route["distancia"]
        num_routes += 1
        max_distance = max(max_distance, route["distancia"])
        min_distance = min(min_distance, route["distancia"])

    average_distance = total_distance / num_routes

    print("Estadísticas de las rutas:")
    print(f"Número total de rutas: {num_routes}")
    print(f"Distancia promedio: {average_distance}")
    print(f"Ruta más larga: {max_distance}")
    print(f"Ruta más corta: {min_distance}")

def update_route(route_id, new_data, collection):
    # Actualizar información de una ruta
    collection.update_one({"_id": route_id}, {"$set": new_data})

def delete_route(route_id, collection):
    # Eliminar una ruta
    collection.delete_one({"_id": route_id})

def add_new_route(new_route_data, collection):
    # Agregar una nueva ruta
    collection.insert_one(new_route_data)

def sort_routes_by_distance(collection):
    # Ordenar rutas por distancia
    sorted_routes = collection.find().sort("distancia", pymongo.ASCENDING)
    for route in sorted_routes:
        print(route)

def search_routes_by_text(keyword, collection):
    # Buscar rutas por texto en origen, destino o descripción
    search_result = collection.find({"$or": [{"origen": {"$regex": keyword, "$options": "i"}},
                                             {"destino": {"$regex": keyword, "$options": "i"}},
                                             {"descripcion": {"$regex": keyword, "$options": "i"}}]})
    for route in search_result:
        print(route)

def extract_rutas():
    try:
        # Conexión a la base de datos
        client = connect_to_mongodb()

        # Seleccionar la base de datos y la colección
        db = client.mydatabase  # Reemplaza "mydatabase" con el nombre de tu base de datos
        collection = db.rutas   # Reemplaza "rutas" con el nombre de tu colección

        # Filtrar rutas por origen o destino
        filter_routes_by_origin_or_destination("Ciudad A", collection)

        # Calcular estadísticas de las rutas
        # calculate_route_statistics(collection)

        # Actualizar información de una ruta
        # update_route(ObjectId('664f9e0d3fd7d041b32c0933'), {"destino": "Nueva Ciudad"}, collection)

        # Eliminar una ruta
        # delete_route(ObjectId('664f9e0d3fd7d041b32c0933'), collection)

        # Agregar una nueva ruta
        # add_new_route({"ruta": "Nueva Ruta", "origen": "Ciudad X", "destino": "Ciudad Y", "distancia": 300}, collection)

        # Ordenar rutas por distancia
        # sort_routes_by_distance(collection)

        # Buscar rutas por texto
        # search_routes_by_text("Ciudad", collection)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    extract_rutas()
