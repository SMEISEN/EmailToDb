import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config(object):

    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASS = os.getenv('EMAIL_PASS')
    EMAIL_DIRECTORY = f'"{os.getenv("EMAIL_DIRECTORY")}"'

    IMAP_ADRESS = str(os.getenv('IMAP_ADRESS'))
    IMAP_PORT = int(os.getenv('IMAP_PORT'))
