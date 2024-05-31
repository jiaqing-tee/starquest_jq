from flask import Flask, request
from flask_mysqldb import MySQL
from util import jwt
from config import env


app = Flask(__name__)

mysql = MySQL(app)
app.config['MYSQL_HOST'] = env.MYSQL_HOST
app.config['MYSQL_PORT'] = env.MYSQL_PORT
app.config['MYSQL_DB'] = env.MYSQL_DB
app.config['MYSQL_USER'] = env.MYSQL_USER
app.config['MYSQL_PASSWORD'] = env.MYSQL_PASSWORD


@app.route('/login', methods=['POST'])
def login():
    auth_header = request.authorization
    if (not auth_header) or (not auth_header.username) or not (auth_header.password):
        return ('Unauthorized: No authorization header provided', 401)
    # Check db for username and password
    cur = mysql.connection.cursor()
    sql_statement = f'SELECT password FROM user WHERE email="{auth_header.username}"'
    query_row_count = cur.execute(sql_statement)
    if query_row_count == 0:
        return (f'Unauthorized: User "{auth_header.username}" not found', 401)
    (password) = cur.fetchone()
    if auth_header.password != password:
        return ('Unauthorized: The username or password is incorrect', 401)
    return jwt.encode(env.JWT_SECRET, auth_header.username, True)

@app.route('/validate', methods=['POST'])
def validate():
    auth_header = request.headers['Authorization']
    if (not auth_header) or (type(auth_header) is not str):
        return ('Unauthorized: No authorization header provided', 401)
    elif auth_header[:7] != 'Bearer ':
        return ('Unauthorized: Bearer authentication not provided in authorization header', 401)
    try:
        return jwt.decode(auth_header)
    except:
        return ('Unauthorized: Invalid access token provided', 401)

if __name__ == '__main__':
    app.run(host=env.FLASK_HOST, port=env.FLASK_PORT, debug=env.FLASK_DEBUG)
