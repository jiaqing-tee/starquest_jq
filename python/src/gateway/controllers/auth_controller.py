import requests
from flask import request
from utils.error_handlers import MissingAuthHeader, MissingBasicAuthentication
from config import env


def login():
    auth_header = request.authorization
    if not auth_header:
        raise MissingAuthHeader()
    elif (auth_header.type != 'basic') or (not auth_header.username) or not (auth_header.password):
        raise MissingBasicAuthentication()
    response = requests.post(
        f'{env.AUTH_SVC_ADDRESS}/login', 
        auth=(auth_header.username, auth_header.password)
    )
    return (response.content, response.status_code)
