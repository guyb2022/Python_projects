import requests
from dotenv import load_dotenv
import os

# Loading the environment variables
load_dotenv(".env")


class Weather:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.url_web = 'https://api.openweathermap.org/data/2.5/onecall'
        self.longitude = ''
        self.latitude = ''
        self.params = {}

    def set_params(self, latitude, longitude, exclude):
        self.latitude = latitude
        self.longitude = longitude
        self.params = {
            'lat': self.latitude,
            'lon': self.longitude,
            'appid': self.api_key,
            'exclude': exclude,
        }

    def get_weather_forcast(self):
        weather_response = requests.get(url=self.url_web, params=self.params)
        weather_response.raise_for_status()
        data = weather_response.json()
        return data
