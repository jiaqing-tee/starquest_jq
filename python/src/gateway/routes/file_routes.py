from flask import Blueprint
from controllers import file_controller


file_bp = Blueprint('file', __name__, url_prefix='/file')
file_bp.route('/upload', methods=['POST'])(file_controller.upload)
file_bp.route('/download', methods=['GET'])(file_controller.download)
