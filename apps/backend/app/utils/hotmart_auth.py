from typing import Optional, Dict
from dotenv import load_dotenv
import requests
import os
import base64

# Cargar variables de entorno
load_dotenv()

# Hotmart credentials
CLIENT_ID = os.getenv("HOTMART_CLIENT_ID")
CLIENT_SECRET = os.getenv("HOTMART_CLIENT_SECRET")
BASIC_AUTH = os.getenv("HOTMART_BASIC_AUTH")

# Hotmart URL authentication
HOTMART_AUTH_URL = os.getenv("HOTMART_AUTH_URL")


def get_hotmart_token() -> Optional[Dict]:
    """Obtiene un nuevo token de acceso de Hotmart"""

    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET
    basic_auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    url = HOTMART_AUTH_URL
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {basic_auth}",
    }

    params = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    try:
        response = requests.post(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)
