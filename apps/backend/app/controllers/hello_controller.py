from flask import jsonify


def greetings():
    return jsonify({"message": "Hola Mundo"})
