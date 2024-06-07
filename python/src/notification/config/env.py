import os


# RabbitMQ
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_MP3_QUEUE = os.environ.get('RABBITMQ_MP3_QUEUE')
# Email
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_SUBJECT = os.environ.get('EMAIL_SUBJECT')
# File
FILE_DOWNLOAD_URL = os.environ.get('FILE_DOWNLOAD_URL')
