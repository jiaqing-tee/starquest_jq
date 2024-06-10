from flask import request
from werkzeug.security import check_password_hash
from models import mysql, postgres
from utils import access
import utils.error_handlers as http_err
from config import env


APP_MODEL = mysql if env.APP_DB_USE_MYSQL else postgres


def login():
    auth_header = request.authorization
    if not auth_header:
        raise http_err.MissingAuthHeader()
    elif (auth_header.type != 'basic') or (not auth_header.username) or (not auth_header.password):
        raise http_err.MissingBasicAuthentication()
    password_hash = APP_MODEL.get_user_password_hash(auth_header.username)
    if password_hash is None:
        raise http_err.UserNotFound(auth_header.username)
    if not check_password_hash(password_hash, auth_header.password):
        raise http_err.IncorrectUserPassword()
    return access.get_access_token(env.JWT_SECRET, auth_header.username, True)

def validate():
    auth_header = request.authorization
    if not auth_header:
        raise http_err.MissingAuthHeader()
    elif auth_header.type != 'bearer':
        raise http_err.MissingBearerAuthentication()
    return access.get_payload(auth_header.token)
