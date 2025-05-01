# Usamos una imagen base de Python
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos necesarios al contenedor
COPY server.py /app
COPY requirements.txt /app

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto en el que el servidor Flask escuchará
EXPOSE 5000

# Comando para ejecutar el servidor Flask
CMD ["python", "server.py"]
