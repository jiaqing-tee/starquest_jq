import json, pika
import pika.spec
from typing import Callable
from utils.error_handlers import ErrorWrapper
from config import env


RABBITMQ_CONNECTION = None
RABBITMQ_CHANNEL = None


def init():
    global RABBITMQ_CONNECTION, RABBITMQ_CHANNEL
    try:
        parameters = pika.ConnectionParameters(env.RABBITMQ_HOST)
        RABBITMQ_CONNECTION = pika.BlockingConnection(parameters)
    except Exception as err:
        raise ErrorWrapper('Unable to initialize RabbitMQ connection', err)
    try:
        RABBITMQ_CHANNEL = RABBITMQ_CONNECTION.channel()
    except Exception as err:
        raise ErrorWrapper('Unable to initialize RabbitMQ channel', err)


def consume(queue_name: str, callback: Callable):
    try:
        RABBITMQ_CHANNEL.basic_consume(queue=queue_name, on_message_callback=callback)
    except Exception as err:
        raise ErrorWrapper(f'Unable to consume from {queue_name} queue', err)


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
        raise ErrorWrapper(f'Unable to publish to {routing_key} channel with {body}', err)
