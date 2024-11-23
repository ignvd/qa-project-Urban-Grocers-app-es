import requests
from configuration import BASE_URL, ROUTES
from data import user_body

def create_user():
    # Se envía el cuerpo de la solicitud para crear un usuario
    response = requests.post(BASE_URL + ROUTES["create_user"], json=user_body)
    return response.json()["authToken"]

def create_kit(kit_body, auth_token):
    # Se asegura que los headers incluyan el token correcto
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(BASE_URL + ROUTES["create_kit"], json=kit_body, headers=headers)
    return response
