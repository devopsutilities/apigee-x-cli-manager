import requests
import constants


def get_instance_name(auth_token: str, organization: str):
    headers = {
        "authorization": f"Bearer {auth_token}",
        "content-type": "application/json"
    }
    url = f"{constants.BASE_URL}/{organization}/instances"
    response = requests.get(url=url, headers=headers)
    instance_name = response.json().get("instances")[0].get("name")
    print(f"instance name found: {instance_name}")
    return instance_name
