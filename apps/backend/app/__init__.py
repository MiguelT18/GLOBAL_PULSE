from flask import Flask
from app.config import Config
from app.routes.hello_router import greet_bp
from app.extensions import cors


def create_app():
    """
    Crea y configura la instancia principal de la aplicación Flask.
    """
    app = Flask(__name__)
    app.config.from_object(Config)  # Cargar la configuración desde la clase Config

    # Inicializar extensiones
    cors.init_app(
        app, resources={r"/api/*": {"origins": "*"}}
    )  # Habilitar CORS para todas las rutas de la API

    # Registrar blueprint
    app.register_blueprint(greet_bp)

    return app
