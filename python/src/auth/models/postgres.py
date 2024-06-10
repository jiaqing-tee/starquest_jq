import psycopg2
from config import env


POSTGRES_CONNECTION = None


def init():
    global POSTGRES_CONNECTION
    POSTGRES_CONNECTION = psycopg2.connect(
        host=env.POSTGRES_HOST,
        port=env.POSTGRES_PORT,
        database=env.POSTGRES_DB,
        user=env.POSTGRES_USER,
        password=env.POSTGRES_PASSWORD
    )

def get_user_password_hash(username):
    cur = POSTGRES_CONNECTION.cursor()
    sql_statement = f"SELECT password_hash FROM users WHERE email='{username}';"
    query_row_count = cur.execute(sql_statement)
    if query_row_count == 0:
        return None
    result = cur.fetchone()
    cur.close()
    return result[0]
