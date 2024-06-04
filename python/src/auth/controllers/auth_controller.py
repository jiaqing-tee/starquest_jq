from flask import request
from models import mysql
from utils import access
import utils.error_handlers as http_err
from config import env


def login():
    auth_header = request.authorization
    if not auth_header:
        raise http_err.MissingAuthHeader()
    elif (auth_header.type != 'basic') or (not auth_header.username) or (not auth_header.password):
        raise http_err.MissingBasicAuthentication()
    user_password = mysql.get_user_password(auth_header.username)
    if user_password is None:
        raise http_err.UserNotFound(auth_header.username)
    if auth_header.password != user_password:
        raise http_err.IncorrectUserPassword()
    return access.get_access_token(env.JWT_SECRET, auth_header.username, True)

def validate():
    auth_header = request.authorization
    if not auth_header:
        raise http_err.MissingAuthHeader()
    elif auth_header.type != 'bearer':
        raise http_err.MissingBearerAuthentication()
    return access.get_payload(auth_header.token)
