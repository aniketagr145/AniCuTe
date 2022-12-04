# -*- coding: utf-8 -*-
import telegram


class SecureTeaTelegram():
    """Initialize the telegram."""

    modulename = "Telegram"
    enabled = True

    def __init__(self, cred, debug):
        """Init Telegram params.
        """

        self.token = cred['token']
        self.user_id = cred['user_id']

    def notify(self, msg):
        message = str(msg) + "\n"

        bot = telegram.Bot(token=self.token)
        bot.send_message(chat_id=self.user_id, text=message)
        return
