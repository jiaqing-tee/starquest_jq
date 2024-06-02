import json, pika
import pika.spec
from utils.error_handlers import ErrorInitRabbitmq, PublishError
from config import env


RABBITMQ_CONNECTION = None
RABBITMQ_CHANNEL = None


def init():
    global RABBITMQ_CONNECTION, RABBITMQ_CHANNEL
    try:
        RABBITMQ_CONNECTION = pika.BlockingConnection(pika.ConnectionParameters(env.RABBITMQ_HOST))
    except Exception as err:
        raise ErrorInitRabbitmq(f'Unable to initialize RabbitMQ connection: {err}')
    try:
        RABBITMQ_CHANNEL = RABBITMQ_CONNECTION.channel()
    except Exception as err:
        raise ErrorInitRabbitmq(f'Unable to initialize RabbitMQ channel: {err}')


def publish(routing_key: str, message: dict):
    try:
        body = json.dumps(message)
        properties = pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
        RABBITMQ_CHANNEL.basic_publish(
            exchange='',
            routing_key=routing_key,
            body=body,
            properties=properties,
        )
    except Exception as err:
        raise PublishError(routing_key, body, err)
