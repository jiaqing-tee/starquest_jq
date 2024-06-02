from flask import request, send_file
from models import mongodb, rabbitmq
from utils import auth
from utils.error_handlers import NoPermission, MissingFidParams
from config import env


def upload():
    user_access = auth.validate_user()
    if not user_access['admin']:
        raise NoPermission(user_access["username"])
    uploaded_videos = []
    for file_name, file_storage in request.files.items():
        grid_file_id = mongodb.upload_file(env.GRIDFS_VIDEO_NAME, file_storage)
        message = {
            'username': user_access['username'],
            'video_name': file_storage.filename,
            'video_fid': grid_file_id,
            'mp3_fid': None,
        }
        try:
            rabbitmq.publish(env.RABBITMQ_VIDEO_QUEUE, message)
        except Exception as err:
            mongodb.delete_file(env.GRIDFS_VIDEO_NAME)
            raise err
        uploaded_videos.append({
            'video_name': file_storage.filename,
            'video_fid': grid_file_id,
        })
    return {
        'username': user_access['username'],
        'uploaded_videos': uploaded_videos,
    }


def download():
    user_access = auth.validate_user()
    if not user_access['admin']:
        raise NoPermission(user_access["username"])
    fid = request.args.get('fid')
    if not fid:
        raise MissingFidParams()
    gridout = mongodb.download_file(env.GRIDFS_MP3_NAME, fid)
    return send_file(gridout, download_name=f'{fid}.mp3')
