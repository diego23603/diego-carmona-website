from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connect_to_mongodb():
    # URI de conexión
    uri = "mongodb+srv://dcarru9:AEUFqcbKYXzHPqHs@cluster0.qnzmtv6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Crear un nuevo cliente y conectarse al servidor
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Enviar un ping para confirmar una conexión exitosa
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    connect_to_mongodb()
