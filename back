from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada (diccionario)
usuarios_db = {
    1: {"nombre": "Juan", "edad": 30},
    2: {"nombre": "Ana", "edad": 25},
    3: {"nombre": "Carlos", "edad": 28},
}

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    """Devuelve todos los usuarios."""
    return jsonify(usuarios_db), 200

@app.route('/usuario/<int:id>', methods=['GET'])
def obtener_usuario(id):
    """Devuelve los detalles de un usuario específico."""
    usuario = usuarios_db.get(id)
    if usuario:
        return jsonify(usuario), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/usuario', methods=['POST'])
def agregar_usuario():
    """Agrega un nuevo usuario."""
    nuevo_usuario = request.json
    id_nuevo_usuario = max(usuarios_db.keys()) + 1  # Generar un nuevo ID
    usuarios_db[id_nuevo_usuario] = nuevo_usuario
    return jsonify({"mensaje": "Usuario agregado", "id": id_nuevo_usuario}), 201

@app.route('/usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    """Actualiza la información de un usuario."""
    usuario = usuarios_db.get(id)
    if usuario:
        datos_actualizados = request.json
        usuario.update(datos_actualizados)
        return jsonify({"mensaje": "Usuario actualizado", "usuario": usuario}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    """Elimina un usuario."""
    if id in usuarios_db:
        del usuarios_db[id]
        return jsonify({"mensaje": "Usuario eliminado"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
