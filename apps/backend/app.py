from flask import Flask, jsonify, request
from flask_cors import CORS

# Crear la aplicación Flask
app = Flask(__name__)
CORS(app)


# Ruta de prueba (GET)
@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {"mensaje": "¡Servidor Flask en Docker funcionando con Python 3.13!"}
    )


# Ejecutar la app en modo producción con Gunicorn
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
