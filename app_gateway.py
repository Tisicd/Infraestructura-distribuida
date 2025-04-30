from flask import Flask, jsonify
import requests

app = Flask(__name__)

SERVICES = {
    "service_a": "http://servicio-a:5001",
    "service_b": "http://servicio-b:5002",
}

@app.route("/<service_name>/hello")
def gateway(service_name):
    if service_name not in SERVICES:
        return jsonify({"error": "Servicio no encontrado"}), 404
    
    response = requests.get(f"{SERVICES[service_name]}/hello")
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)