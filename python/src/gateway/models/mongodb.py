import sys
from gridfs import GridFS
from flask import current_app
from flask_pymongo import PyMongo
from werkzeug.datastructures import FileStorage
from bson.objectid import ObjectId
from utils.error_handlers import ErrorInitDb, UploadError, DownloadError
from config import env


MONGODB_VIDEO = None
MONGODB_MP3 = None
GRIDFS_VIDEOS = None
GRIDFS_MP3S = None
GRIDFS: dict[str: GridFS] = {}


def init():
    global MONGODB_VIDEO, MONGODB_MP3, GRIDFS_VIDEOS, GRIDFS_MP3S
    try:
        MONGODB_VIDEO = PyMongo(current_app, uri=env.MONGODB_VIDEO_URI)
        MONGODB_MP3 = PyMongo(current_app, uri=env.MONGODB_MP3_URI)
    except Exception as err:
        raise ErrorInitDb(f'Unable to initialize MongoDB: {err}')
    try:
        GRIDFS_VIDEOS = GridFS(MONGODB_VIDEO.db)
        GRIDFS_MP3S = GridFS(MONGODB_MP3.db)
        GRIDFS[env.GRIDFS_VIDEO_NAME] = GRIDFS_VIDEOS
        GRIDFS[env.GRIDFS_MP3_NAME] = GRIDFS_MP3S
    except Exception as err:
        raise ErrorInitDb(f'Unable to initialize GridFS: {err}')


def upload_file(gridfs_name: str, file_storage: FileStorage):
    try:
        grid_file_id = GRIDFS[gridfs_name].put(file_storage)
        return str(grid_file_id)
    except Exception as err:
        raise UploadError(gridfs_name, err)


def download_file(gridfs_name: str, fid: str):
    try:
        gridout = GRIDFS[gridfs_name].get(ObjectId(fid))
        return gridout
    except Exception as err:
        raise DownloadError(gridfs_name, fid, err)


def delete_file(gridfs_name: str):
    try:
        GRIDFS[gridfs_name].delete()
    except Exception as err:
        print(f'Error deleting file from {gridfs_name} GridFS: {err}', file=sys.stderr)
