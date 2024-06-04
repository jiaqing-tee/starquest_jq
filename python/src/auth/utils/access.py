import jwt
import datetime as dt
from utils.error_handlers import ErrorWrapper, InvalidUserToken
from config import env


def get_access_token(secret: str, username: str, is_admin: bool):
    try:
        payload = {
            'username': username,
            'admin': is_admin,
            'exp': dt.datetime.now(dt.timezone.utc) + dt.timedelta(days=1),
            'iat': dt.datetime.now(dt.timezone.utc),
        }
        access_token = jwt.encode(payload, secret, algorithm=env.JWT_ALGORITHM)
        return access_token
    except Exception as err:
        raise ErrorWrapper(f'Unable to generate access token for {username}: {err}')


def get_payload(bearer_token: str):
    try:
        payload = jwt.decode(bearer_token, env.JWT_SECRET, algorithms=[env.JWT_ALGORITHM])
        return payload
    except Exception as err:
        raise InvalidUserToken(err)
