import requests
from configuration import BASE_URL, ROUTES

def create_user():
    response = requests.post(BASE_URL + ROUTES["create_user"])
    return response.json()["authToken"]

def create_kit(kit_body, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(BASE_URL + ROUTES["create_kit"], json=kit_body, headers=headers)
    return response
