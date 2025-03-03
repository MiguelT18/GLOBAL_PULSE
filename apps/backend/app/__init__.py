from flask import Flask
from app.extensions import cors
from app.routes.hotmart_routes import hotmart_bp


def create_app():
    """
    Crea y configura la instancia principal de la aplicación Flask.
    """
    app = Flask(__name__)

    # Inicializar extensiones
    cors.init_app(
        app, resources={r"/api/*": {"origins": "*"}}
    )  # Habilitar CORS para todas las rutas de la API

    # Registrar blueprint
    app.register_blueprint(hotmart_bp)

    return app
