from __future__ import unicode_literals
import imaplib


class MailManager(object):
    def __init__(self, smtp_server, username, password):
        self._imap = imaplib.IMAP4_SSL(smtp_server)
        self._imap.login(username, password)

    def list_folders(self):
        return self._imap.list()
