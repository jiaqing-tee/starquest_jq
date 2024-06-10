from flask import Flask
from models import mongodb, rabbitmq
from routes import api_routes
from config import env


app = Flask(__name__)

with app.app_context():
    # Models
    mongodb.init()
    rabbitmq.init()
    # Routes
    app.register_blueprint(api_routes.api_bp)


if __name__ == '__main__':
    app.run(host=env.FLASK_HOST, port=env.FLASK_PORT, debug=env.FLASK_DEBUG)
