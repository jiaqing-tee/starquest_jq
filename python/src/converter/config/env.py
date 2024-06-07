import os


# MongoDB
MONGODB_HOST = os.environ.get('MONGODB_HOST')
MONGODB_PORT = int(os.environ.get('MONGODB_PORT'))
MONGODB_VIDEO_DB = os.environ.get('MONGODB_VIDEO_DB')
MONGODB_MP3_DB = os.environ.get('MONGODB_MP3_DB')
GRIDFS_VIDEO_NAME = os.environ.get('GRIDFS_VIDEO_NAME')
GRIDFS_MP3_NAME = os.environ.get('GRIDFS_MP3_NAME')
# RabbitMQ
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_VIDEO_QUEUE = os.environ.get('RABBITMQ_VIDEO_QUEUE')
RABBITMQ_MP3_QUEUE = os.environ.get('RABBITMQ_MP3_QUEUE')
