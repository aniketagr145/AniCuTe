# -*- coding: utf-8 -*-
import telegram


class TelegramNotifier():
    """Initialize the telegram."""

    modulename = "Telegram"
    enabled = True

    def __init__(self, cred):
        """Init Telegram params.
        """

        self.token = cred['token']
        self.user_id = cred['user_id']

    def notify(self, msg):
        message = "ALERT\n" + str(msg)

        bot = telegram.Bot(token=self.token)
        bot.send_message(chat_id=self.user_id, text=message)
        return
