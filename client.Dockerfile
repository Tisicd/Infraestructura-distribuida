# Usamos una imagen base de Python
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos necesarios al contenedor
COPY cliente.py /app
COPY requirements.txt /app

# Instalamos las dependencias necesarias (requests)
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar el cliente
CMD ["python", "cliente.py"]
