from typing import Optional, List, Dict
import requests
import time
from app.utils.hotmart_auth import get_hotmart_token
import json


class HotmartAPI:
    BASE_URL = "https://sandbox.hotmart.com/products/api/v1/products"
    _token = None
    _token_expiration = 0

    def __init__(self):
        """
        Inicializa la clase con el token de autenticación.
        """
        self.access_token = self.get_valid_token()
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}",
        }

    def get_valid_token(self) -> str:
        """
        Obtiene un token válido. Si el token en caché sigue siendo válido, lo usa.
        Si ha expirado, obtiene uno nuevo y actualiza la caché.

        Returns:
            str: Token de acceso válido.
        """
        current_time = time.time()

        if self._token and current_time < self._token_expiration:
            return self._token  # Reutilizar token si aún es válido

        # Solicitar un nuevo token porque el actual ha expirado o no existe
        token_data = get_hotmart_token()
        if token_data:
            self._token = token_data["access_token"]
            self._token_expiration = (
                current_time + token_data["expires_in"] - 60
            )  # Restamos 60s como buffer
            return self._token
        else:
            raise Exception("Error al obtener el token de Hotmart.")

    def get_catalogue(self, quantity: int) -> Optional[List[Dict]]:
        """
        Obtiene el catálogo de productos de Hotmart y devuelve los primeros 'quantity' productos.

        Args:
            quantity (int): Número de productos a obtener (máx. 50).

        Returns:
            list: Lista de productos o None en caso de error.
        """

        url = f"{self.BASE_URL}?max_results=50"

        try:
            response = requests.get(url, headers=self.headers)

            print(f"🔹 Código de estado: {response.status_code}")
            print(f"🔹 Respuesta cruda: {response.text}")

            if response.status_code == 200:
                if not response.text.strip():
                    print("⚠️ La API de Hotmart devolvió una respuesta vacía.")
                    return None

                try:
                    data = response.json()
                except json.JSONDecodeError:
                    print("❌ Error al decodificar JSON. Respuesta no es válida.")
                    return None

                if "items" in data:
                    products = data["items"]
                    return products[: min(quantity, len(products))]
                else:
                    print("⚠️ La respuesta de Hotmart no contiene 'items'.")
                return None
            else:
                print(
                    f"❌ Error en la solicitud: {response.status_code} - {response.text}"
                )
                return None
        except requests.RequestException as e:
            print(f"❌ Error en la solicitud: {e}")
            return None
