from flask import jsonify
from app.services.hotmart_api import HotmartAPI


def get_products(quantity: int):
    """
    Controlador que obtiene productos del catálogo de Hotmart.

    Args:
        quantity (int, opcional): Número de productos a obtener.

    Returns:
        json: Respuesta con productos o mensaje de error.
    """
    hotmart_service = HotmartAPI()
    products = hotmart_service.get_catalogue(quantity)

    if products:
        return jsonify({"status": "success", "data": products}), 200
    else:
        return (
            jsonify({"status": "error", "message": "No se pudo obtener el catálogo"}),
            400,
        )
