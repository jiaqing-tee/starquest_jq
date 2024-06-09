from flask import current_app
from flask_mysqldb import MySQL
from utils.error_handlers import ErrorInitDb
from config import env


MYSQL_SERVER: MySQL = None


def init():
    global MYSQL_SERVER
    try:
        MYSQL_SERVER = MySQL(current_app)
        current_app.config['MYSQL_HOST'] = env.MYSQL_HOST
        current_app.config['MYSQL_PORT'] = env.MYSQL_PORT
        current_app.config['MYSQL_DB'] = env.MYSQL_DB
        current_app.config['MYSQL_USER'] = env.MYSQL_USER
        current_app.config['MYSQL_PASSWORD'] = env.MYSQL_PASSWORD
    except Exception as err:
        raise ErrorInitDb(f'Unable to initialize MySQL: {err}')


def get_user_password(username):
    cur = MYSQL_SERVER.connection.cursor()
    sql_statement = f'SELECT password FROM users WHERE email="{username}";'
    query_row_count = cur.execute(sql_statement)
    if query_row_count == 0:
        return None
    result = cur.fetchone()
    return result[0]
