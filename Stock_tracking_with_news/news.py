import requests
from dotenv import load_dotenv
import os

# Loading the environment variables
load_dotenv(".env")


class News:
    def __init__(self):
        self.api_key = os.getenv('NEWS_API')
        self.web_url = 'https://newsapi.org/v2/everything?'
        self.params = {}
        self.question = ""
        self.date = ""

    def set_params(self, question, date):
        self.question = question
        self.date = date
        self.params = {
            'web_url': self.web_url,
            'q': self.question,
            'date': self.date,
            'apikey': self.api_key,
        }

    def get_news(self):
        """Get the news on selected subject in selected days"""
        response = requests.get(self.web_url, params=self.params).json()
        return response['articles']
