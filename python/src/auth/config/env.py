import os

# Flask
FLASK_HOST = os.environ.get('FLASK_HOST')
FLASK_PORT = int(os.environ.get('FLASK_PORT'))
FLASK_DEBUG = os.environ.get('FLASK_DEBUG').lower() == 'true'
# MySQL
MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_PORT = int(os.environ.get('MYSQL_PORT'))
MYSQL_DB = os.environ.get('MYSQL_DB')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
# JWT
JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')
