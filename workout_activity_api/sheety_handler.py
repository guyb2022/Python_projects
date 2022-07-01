import requests
from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth

# Loading the environment variables
load_dotenv(".env")
# Setting security level to basic
basic = HTTPBasicAuth(os.getenv('SHT_USER'), os.getenv('SHT_PASS'))


class Sheety:
    def __init__(self):
        self.api_key = os.getenv("SHT_API")
        self.url_web = f'https://api.sheety.co/{self.api_key}/myWorkoutsGuy/workouts'
        self.date = ""
        self.time = ""
        self.exercise = ""
        self.duration = ""
        self.calories = ""
        self.params = {}

    def set_data(self, date, time, exercise, duration, calories):
        self.date = date
        self.time = time
        self.exercise = exercise
        self.duration = duration
        self.calories = calories
        self.params = {
            'workout': {
                'date': self.date,
                'time': self.time,
                'exercise': self.exercise,
                'duration': self.duration,
                'calories': self.calories,
            }
        }

    def post_request(self):
        return requests.post(url=self.url_web, json=self.params, auth=basic)
