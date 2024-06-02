from flask import Flask
from models import mongodb, rabbitmq
from routes import auth_routes, file_routes
from config import env


app = Flask(__name__)

with app.app_context():
    # Models
    mongodb.init()
    rabbitmq.init()
    # Routes
    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(file_routes.file_bp)


if __name__ == '__main__':
    app.run(host=env.FLASK_HOST, port=env.FLASK_PORT, debug=env.FLASK_DEBUG)
