FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app_gateway.py .
CMD ["python", "app_gateway.py"]