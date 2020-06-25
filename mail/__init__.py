import imaplib
from mail.config import Config

emailConfig = Config()
_imap_adress = str(emailConfig.IMAP_ADRESS)
_imap_port = int(emailConfig.IMAP_PORT)

m = imaplib.IMAP4_SSL(_imap_adress, _imap_port)
