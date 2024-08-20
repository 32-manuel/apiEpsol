from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para almacenar los datos recibidos
data_list = []

# Ruta para recibir datos mediante POST
@app.route('/add_data', methods=['POST'])
def add_data():
    # Obtener los datos JSON del cuerpo de la solicitud
    data = request.json
    # Agregar los datos a la lista
    data_list.append(data)
    # Devolver una respuesta
    return jsonify({"message": "Data received successfully", "data": data}), 201

# Ruta para mostrar los datos almacenados
@app.route('/show_data', methods=['GET'])
def show_data():
    return jsonify(data_list), 200

if __name__ == '__main__':
    app.run(debug=True)