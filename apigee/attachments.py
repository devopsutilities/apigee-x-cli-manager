import requests
import constants


def get_attachment(auth_token: str, organization: str, instance: str, attachment: str):
    headers = {
        "authorization": f"Bearer {auth_token}",
        "content-type": "application/json"
    }
    url = f"{constants.BASE_URL}/{organization}/instances/{instance}/attachments/{attachment}"
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_attachment_list(auth_token: str, organization: str, instance: str):
    headers = {
        "authorization": f"Bearer {auth_token}",
        "content-type": "application/json"
    }
    url = f"{constants.BASE_URL}/{organization}/instances/{instance}/attachments/"
    response = requests.get(url=url, headers=headers)
    return response.json()


def create_attachment(auth_token: str, organization: str, instance: str, env: str):
    headers = {
        "authorization": f"Bearer {auth_token}",
        "content-type": "application/json"
    }
    url = f"{constants.BASE_URL}/{organization}/instances/{instance}/attachments"
    body = {"environment": env}
    response = requests.post(url=url, headers=headers, json=body)
    return response.json()


def delete_attachment(auth_token: str, organization: str, instance: str, attachment: str):
    headers = {
        "authorization": f"Bearer {auth_token}",
        "content-type": "application/json"
    }
    url = f"{constants.BASE_URL}/{organization}/instances/{instance}/attachments/{attachment}"
    response = requests.delete(url=url, headers=headers)
    return response.json()
