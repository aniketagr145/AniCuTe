# -*- coding: utf-8 -*-
import requests

class TelegramNotifier():
    """Initialize the telegram."""

    modulename = "Telegram"
    enabled = True

    def __init__(self, cred):
        """Init Telegram params.
        """

        self.token = cred['token']
        self.user_id = cred['user_id']

    def send_message(self, msg):
        message = "ALERT\n" + str(msg)
        apiURL = 'https://api.telegram.org/bot{}/sendMessage'.format(self.token)
        response = requests.post(apiURL, json={'chat_id': self.user_id, 'text': message})

        return
