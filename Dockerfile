# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt y lo instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el contenido del proyecto
COPY . .

# Comando para ejecutar tu aplicación
CMD ["python", "src/main.py"]
