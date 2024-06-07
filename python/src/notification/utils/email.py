import sys, smtplib
from email.message import EmailMessage
from utils.error_handlers import ErrorWrapper
from config import env


def send(receiver_address: str, mp3_fid: str):
    try:
        email_message = EmailMessage()
        email_message.set_content(f'Your mp3 file {mp3_fid} is now ready for download. Please visit {env.FILE_DOWNLOAD_URL}{mp3_fid} to download your file.')
        email_message['From'] = env.EMAIL_USERNAME
        email_message['To'] = receiver_address
        email_message['Subject'] = env.EMAIL_SUBJECT

        session = smtplib.SMTP(env.EMAIL_HOST, env.EMAIL_PORT)
        session.starttls()
        session.login(env.EMAIL_USERNAME, env.EMAIL_PASSWORD)
        session.send_message(email_message, env.EMAIL_USERNAME, receiver_address)
        session.quit()
        print(f'Notification email has been sent to {receiver_address} to notify {mp3_fid} audio file is ready.', file=sys.stderr)
    except Exception as err:
        raise ErrorWrapper(f'Unable to send email to {receiver_address} to notify {mp3_fid} audio file is ready', err)
