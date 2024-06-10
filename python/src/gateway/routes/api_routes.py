from flask import Blueprint
from routes import auth_routes, file_routes


api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(auth_routes.auth_bp)
api_bp.register_blueprint(file_routes.file_bp)
