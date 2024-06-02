import os

# Flask
FLASK_HOST = os.environ.get('FLASK_HOST')
FLASK_PORT = int(os.environ.get('FLASK_PORT'))
FLASK_DEBUG = os.environ.get('FLASK_DEBUG').lower() == 'true'
# Auth Service
AUTH_SVC_ADDRESS = os.environ.get('AUTH_SVC_ADDRESS')
# MongoDB
MONGODB_VIDEO_URI = os.environ.get('MONGODB_VIDEO_URI')
MONGODB_MP3_URI = os.environ.get('MONGODB_MP3_URI')
GRIDFS_VIDEO_NAME = os.environ.get('GRIDFS_VIDEO_NAME')
GRIDFS_MP3_NAME = os.environ.get('GRIDFS_MP3_NAME')
# RabbitMQ
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_VIDEO_QUEUE = os.environ.get('RABBITMQ_VIDEO_QUEUE')
RABBITMQ_MP3_QUEUE = os.environ.get('RABBITMQ_MP3_QUEUE')
