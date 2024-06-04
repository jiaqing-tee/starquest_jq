import json, requests
from flask import request
from utils.error_handlers import MissingAuthHeader, MissingBearerAuthentication, ErrorWrapper
from config import env


def validate_user():
    auth_header = request.authorization
    if not auth_header:
        raise MissingAuthHeader()
    elif auth_header.type != 'bearer':
        raise MissingBearerAuthentication()
    headers = {
        'Authorization': f'Bearer {request.authorization.token}'
    }
    response = requests.post(
        f'{env.AUTH_SVC_ADDRESS}/auth/validate',
        headers=headers,
    )
    if response.status_code != 200:
        raise ErrorWrapper(response.status_code, response.text)
    return json.loads(response.text)
