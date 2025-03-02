from flask import Blueprint, jsonify
from app.controllers.hello_controller import greetings

greet_bp = Blueprint("greet_bp", __name__)


@greet_bp.route("/", methods=["GET"])
def main():
    return greetings()
