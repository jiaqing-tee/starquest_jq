import os, sys, json
import pika.adapters.blocking_connection
import pika.spec
from models import mongodb, rabbitmq
from utils import convert
from utils.error_handlers import ErrorWrapper
from config import env


def consume_callback(channel: pika.adapters.blocking_connection.BlockingChannel, 
                     method: pika.spec.Basic.Deliver, 
                     properties: pika.spec.BasicProperties, 
                     body: bytes):
    try:
        # Get video file
        message = json.loads(body)
        video_fid = message['video_fid']
        print(f'Begin converting for {video_fid} video.', file=sys.stderr)
        video_file = mongodb.get_file(env.GRIDFS_VIDEO_NAME, video_fid)
        # Get audio file
        audio_file = convert.to_mp3(video_file)
        # Upload audio file
        mp3_fid = mongodb.put_file(env.GRIDFS_MP3_NAME, audio_file)
        message['mp3_fid'] = mp3_fid
        # Add to mp3 queue
        try:
            rabbitmq.publish(env.RABBITMQ_MP3_QUEUE, message)
        except Exception as err:
            mongodb.delete_file(env.GRIDFS_MP3_NAME, mp3_fid)
            raise err
    except Exception as err:
        channel.basic_nack(delivery_tag=method.delivery_tag)
        raise ErrorWrapper(f'Error in consuming callback', err)
    # Acknowledge video queue
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print(f'\nFinished converting for {video_fid} video, created {mp3_fid} audio.', file=sys.stderr)


def main():
    # Initialize Models
    mongodb.init()
    rabbitmq.init()
    # Consume video queue: start converting videos into audios
    rabbitmq.consume(env.RABBITMQ_VIDEO_QUEUE, consume_callback)
    print("Waiting for messages, to exit press CTRL+C", file=sys.stderr)
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
