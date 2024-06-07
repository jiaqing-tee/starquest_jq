import os, tempfile
from moviepy.editor import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from utils.error_handlers import ErrorWrapper


def to_mp3(video: bytes) -> bytes:
    try:
        # Write video into temp file
        video_tf = tempfile.NamedTemporaryFile()
        video_tf.write(video)
        # Get audio file
        audio_tf_path = f'{tempfile.gettempdir()}/audio.mp3'
        audio_file_clip: AudioFileClip = VideoFileClip(video_tf.name).audio
        audio_file_clip.write_audiofile(audio_tf_path)
        with open(audio_tf_path, 'rb') as audio_tf:
            audio_file: bytes = audio_tf.read()
        # Remove files
        os.remove(audio_tf_path)
        video_tf.close()
        return audio_file
    except Exception as err:
        raise ErrorWrapper('Unable to convert video to mp3', err)
