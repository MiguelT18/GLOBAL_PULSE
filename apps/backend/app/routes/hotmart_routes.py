from flask import Blueprint, request
from app.controllers.hotmart_controller import get_products

hotmart_bp = Blueprint("hotmart", __name__, url_prefix="/hotmart")


@hotmart_bp.route("/products", methods=["GET"])
def fetch_products():
    """
    Ruta para obtener productos de Hotmart.
    Parámetros Query:
        - quantity (int, opcional): Número de productos a devolver.
    Returns:
        JSON con la lista de productos o error.
    """
    quantity = request.args.get("quantity", default=5, type=int)
    return get_products(quantity)
