import jwt
import datetime as dt
from config import env


def encode(secret: str, username: str, is_admin: bool):
    payload = {
        'username': username,
        'admin': is_admin,
        'exp': dt.datetime.now(dt.timezone.utc) + dt.timedelta(days=1),
        'iat': dt.datetime.now(dt.timezone.utc),
    }
    return jwt.encode(payload, secret, algorithm=env.JWT_ALGORITHM)

def decode(auth_header):
    bearer_token = auth_header[7:]
    return jwt.decode(bearer_token, env.JWT_SECRET, algorithms=[env.JWT_ALGORITHM])
