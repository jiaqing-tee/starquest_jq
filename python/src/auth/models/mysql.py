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


def get_user_password_hash(username):
    cur = MYSQL_SERVER.connection.cursor()
    sql_statement = 'SELECT password_hash FROM users WHERE email=%s;'
    query_row_count = cur.execute(sql_statement, (username, ))
    if query_row_count == 0:
        return None
    result = cur.fetchone()
    return result[0]
