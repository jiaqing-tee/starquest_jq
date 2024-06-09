from flask import Flask
from models import mysql, postgres
from routes import auth_routes
from config import env


app = Flask(__name__)

with app.app_context():
    # Models
    if env.APP_DB_USE_MYSQL:
        mysql.init()
    if env.APP_DB_USE_POSTGRES:
        postgres.init()
    # Routes
    app.register_blueprint(auth_routes.auth_bp)


if __name__ == '__main__':
    app.run(host=env.FLASK_HOST, port=env.FLASK_PORT, debug=env.FLASK_DEBUG)
