# Mi Proyecto

Este proyecto extrae y muestra las rutas almacenadas en una base de datos MongoDB.

## Configuración

Configura tu base de datos en el archivo `config/settings.py`.

## Cómo ejecutar

1. Instalar dependencias:
    ```
    pip install -r requirements.txt
    ```

2. Ejecutar el script:
    ```
    python src/main.py
    ```

## Cómo ejecutar los tests

1. Instalar `unittest` si no está instalado:
    ```
    pip install unittest
    ```

2. Ejecutar los tests:
    ```
    python -m unittest discover -s tests
    ```
