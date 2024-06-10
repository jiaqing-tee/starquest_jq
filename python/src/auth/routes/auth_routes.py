from flask import Blueprint
from controllers import auth_controller


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
auth_bp.route('/login', methods=['POST'])(auth_controller.login)
auth_bp.route('/validate', methods=['POST'])(auth_controller.validate)
