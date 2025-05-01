import requests

# URL del servidor centralizado
BASE_URL = "http://127.0.0.1:5000"

def obtener_usuarios():
    response = requests.get(f"{BASE_URL}/usuarios")
    if response.status_code == 200:
        usuarios = response.json()
        print("Usuarios:", usuarios)
    else:
        print("Error al obtener usuarios")

def obtener_usuario(id):
    response = requests.get(f"{BASE_URL}/usuario/{id}")
    if response.status_code == 200:
        usuario = response.json()
        print("Usuario:", usuario)
    else:
        print("Error al obtener usuario")

def agregar_usuario(nuevo_usuario):
    response = requests.post(f"{BASE_URL}/usuario", json=nuevo_usuario)
    if response.status_code == 201:
        print("Usuario agregado con éxito")
    else:
        print("Error al agregar usuario")

def actualizar_usuario(id, datos_actualizados):
    response = requests.put(f"{BASE_URL}/usuario/{id}", json=datos_actualizados)
    if response.status_code == 200:
        print("Usuario actualizado con éxito")
    else:
        print("Error al actualizar usuario")

def eliminar_usuario(id):
    response = requests.delete(f"{BASE_URL}/usuario/{id}")
    if response.status_code == 200:
        print("Usuario eliminado con éxito")
    else:
        print("Error al eliminar usuario")

# Ejemplos de uso
if __name__ == "__main__":
    # Obtener todos los usuarios
    obtener_usuarios()
    
    # Obtener un usuario específico
    obtener_usuario(1)
    
    # Agregar un nuevo usuario
    nuevo_usuario = {"nombre": "María", "edad": 22}
    agregar_usuario(nuevo_usuario)
    
    # Actualizar un usuario
    datos_actualizados = {"nombre": "Juanito", "edad": 31}
    actualizar_usuario(1, datos_actualizados)
    
    # Eliminar un usuario
    eliminar_usuario(3)
