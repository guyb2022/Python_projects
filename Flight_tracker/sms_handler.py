from twilio.rest import Client
from dotenv import load_dotenv
import os

# Loading the environment variables
load_dotenv(".env")


class Sender:
    """SMS sender class"""
    def __init__(self):
        """Init sms sender class params"""
        self.auth_token = os.getenv('AUTH_TOKEN')
        self.account_sid = os.getenv('ACCOUNT_SID')
        self.from_number = os.getenv('SMS_FROM')
        self.to_number = os.getenv('SMS_TO')

    def send_sms(self, articles):
        """Send an SMS to the phone number with Twilio library"""
        client = Client(self.account_sid, self.auth_token)
        for article in articles:
            client.messages.create(
                body=article,
                from_=self.from_number,
                to=self.to_number
            )
