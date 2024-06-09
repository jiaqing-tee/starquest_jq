import os


# Flask
FLASK_HOST = os.environ.get('FLASK_HOST')
FLASK_PORT = int(os.environ.get('FLASK_PORT'))
FLASK_DEBUG = os.environ.get('FLASK_DEBUG').lower() == 'true'
# MySQL
MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_PORT = os.environ.get('MYSQL_PORT')
MYSQL_PORT = int(MYSQL_PORT) if MYSQL_PORT is not None else MYSQL_PORT
MYSQL_DB = os.environ.get('MYSQL_DB')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
# Postgres
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_PORT = int(POSTGRES_PORT) if (POSTGRES_PORT is not None) and (str.isdigit(POSTGRES_PORT)) else POSTGRES_PORT
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
# JWT
JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')


APP_DB_USE_MYSQL = MYSQL_DB is not None
APP_DB_USE_POSTGRES = POSTGRES_DB is not None
