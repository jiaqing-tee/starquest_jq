from flask import Flask
from models import mysql
from routes import auth_routes
from config import env


app = Flask(__name__)

with app.app_context():
    # Models
    mysql.init()
    # Routes
    app.register_blueprint(auth_routes.auth_bp)


if __name__ == '__main__':
    app.run(host=env.FLASK_HOST, port=env.FLASK_PORT, debug=env.FLASK_DEBUG)
