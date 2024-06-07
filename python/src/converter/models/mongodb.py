from pymongo import MongoClient
from gridfs import GridFS, GridOut
from bson.objectid import ObjectId
from utils.error_handlers import ErrorWrapper
from config import env


MONGODB_VIDEO_DB = None
MONGODB_MP3_DB = None
GRIDFS_VIDEOS = None
GRIDFS_MP3S = None
GRIDFS: dict[str: GridFS] = {}


def init():
    global MONGODB_VIDEO_DB, MONGODB_MP3_DB, GRIDFS_VIDEOS, GRIDFS_MP3S
    try:
        mongo_client = MongoClient(env.MONGODB_HOST, env.MONGODB_PORT)
        MONGODB_VIDEO_DB = mongo_client.get_database(env.MONGODB_VIDEO_DB)
        MONGODB_MP3_DB = mongo_client.get_database(env.MONGODB_MP3_DB)
    except Exception as err:
        raise ErrorWrapper('Unable to initialize MongoDB', err)
    try:
        GRIDFS_VIDEOS = GridFS(MONGODB_VIDEO_DB)
        GRIDFS_MP3S = GridFS(MONGODB_MP3_DB)
        GRIDFS[env.GRIDFS_VIDEO_NAME] = GRIDFS_VIDEOS
        GRIDFS[env.GRIDFS_MP3_NAME] = GRIDFS_MP3S
    except Exception as err:
        raise ErrorWrapper('Unable to initialize GridFS', err)


def get_file(gridfs_name: str, objectid: str) -> bytes:
    try:
        out: GridOut = GRIDFS[gridfs_name].get(ObjectId(objectid))
        file: bytes = out.read()
        return file
    except Exception as err:
        raise ErrorWrapper(f'Unable to get {objectid} file from {gridfs_name} GridFS', err)


def put_file(gridfs_name: str, file: bytes) -> str:
    try:
        fid: ObjectId = GRIDFS[gridfs_name].put(file)
        return str(fid)
    except Exception as err:
        raise ErrorWrapper(f'Unable to put file in {gridfs_name} GridFS', err)


def delete_file(gridfs_name: str, objectid: str):
    try:
        GRIDFS[gridfs_name].delete(ObjectId(objectid))
    except Exception as err:
        raise ErrorWrapper(f'Unable to delete {objectid} file in {gridfs_name} GridFS', err)
