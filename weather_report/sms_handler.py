from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
import os

# Loading the environment variables
load_dotenv(".env")


class Sender:
    def __init__(self):
        self.auth_token = os.getenv('AUTH_TOKEN')
        self.account_sid = os.getenv('ACCOUNT_SID')
        self.from_number = os.getenv('SMS_FROM')
        self.to_number = os.getenv('SMS_TO')

    def send_sms(self, articles):
        """Send an SMS to the phone number with Twilio library"""
        # If operate from pythonanywhere need ot add this lines
        # proxy_client = TwilioHttpClient()
        # proxy_client.session.proxies = {'https: os.environ['https_proxy']'}
        # client = Client(self.account_sid, self.auth_token, http_client=proxy_client)
        client = Client(self.account_sid, self.auth_token)
        for article in articles:
            print(article)
            client.messages.create(
                body=article,
                from_=self.from_number,
                to=self.to_number
            )
