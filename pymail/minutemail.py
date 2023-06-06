import requests

BASE_URL = "https://10minutemail.com"
NEW_EMAIL = BASE_URL + "/session/address"
MESSAGE_AFTER = BASE_URL + "/messages/messagesAfter/"
MESSAGE_COUNT = BASE_URL + "/messages/messageCount"

class Mail(object):
    """
    Python wrapper for 10minutemail.com
    """

    def __init__(self):
        self.session = requests.session()
        self.message_count = 0
        self.messages = []

        # The website needs a user agent, otherwise we get a 403 error
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"}
        self.mail = self.session.get(NEW_EMAIL, headers=self.headers).json()['address']

    def get_mail(self):
        """
        :return: Mail of the current instance
        """
        return self.mail

    def get_message(self):
        """
        :return: list of messages stored in this instance
        """
        return self.messages

    def fetch_message(self):
        """
        Fetches for new messages which are not present in the instance
        :return: List of messages stored in the instance
        """
        res = self.session.get(MESSAGE_AFTER + str(self.message_count), headers=self.headers).json()
        self.message_count += len(res)
        self.messages += res
        return self.messages

    def new_message(self):
        """
        Check whether there are new messages or not
        :return: bool
        """
        return self.session.get(MESSAGE_COUNT, headers=self.headers).json()['messageCount'] != self.message_count
