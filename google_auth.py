import google.auth
import google.auth.transport.requests


def get_auth_token():
    creds, project = google.auth.default()
    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)
    return creds.token
