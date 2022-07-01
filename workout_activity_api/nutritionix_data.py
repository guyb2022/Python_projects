import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Loading the environment variables
load_dotenv(".env")
# Setting security level to basic
basic = HTTPBasicAuth(os.getenv('NUT_USER'), os.getenv('NUT_USER'))


class Nutritionix:
    """Nutritionsix calls"""
    def __init__(self, ):
        """Init all class vars"""
        self.url_web = 'https://trackapi.nutritionix.com/v2/natural/exercise'
        self.x_app_id = os.getenv('NUT_API_ID')
        self.x_app_key = os.getenv('NUT_API_KEY')
        self.x_remote_user_id = "0"
        self.query = ""
        self.gender = ""
        self.weight = ""
        self.height = ""
        self.age = ""
        self.params = {}
        self.header = {
            "x-app-id": self.x_app_id,
            "x-app-key": self.x_app_key,
            "x-remote-user-id": self.x_remote_user_id,
        }

    def set_data(self, query, gender, weight, height, age):
        """Init the request params"""
        self.query = query
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age
        self.params = {
            "query": self.query,
            "gender": self.gender,
            "weight_kg": self.weight,
            "height_cm": self.height,
            "age": self.age
        }

    def post_request(self):
        """Request POST new entry"""
        response = requests.post(url=self.url_web, json=self.params, headers=self.header, auth=basic)
        data = response.json()
        return data
        # return requests.post(url=self.url_web, json=self.params, headers=self.header).json()