import os, sys, json
import pika.adapters.blocking_connection
import pika.spec
from models import rabbitmq
from utils import email
from utils.error_handlers import ErrorWrapper
from config import env


def consume_callback(channel: pika.adapters.blocking_connection.BlockingChannel, 
                     method: pika.spec.Basic.Deliver, 
                     properties: pika.spec.BasicProperties, 
                     body: bytes):
    try:
        message = json.loads(body)
        username, mp3_fid = message['username'], message['mp3_fid']
        email.send(username, mp3_fid)
    except Exception as err:
        channel.basic_nack(delivery_tag=method.delivery_tag)
        raise ErrorWrapper(f'Error in consuming callback', err)
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():
    # Initialize Models
    rabbitmq.init()
    # Consume mp3 queue: start sending email notification
    rabbitmq.consume(env.RABBITMQ_MP3_QUEUE, consume_callback)
    print('Waiting for messages, to exit press CTRL+C', file=sys.stderr)
    rabbitmq.RABBITMQ_CHANNEL.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted', file=sys.stderr)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
