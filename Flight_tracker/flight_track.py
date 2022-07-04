import requests
from dotenv import load_dotenv
import os

# Loading the environment variables
load_dotenv(".env")


class FlightTrack:
    """Class for the FLight API"""
    def __init__(self):
        """Init all FLight params"""
        self.api_key = os.getenv('FLY_API')
        self.password = os.getenv('FLY_PASS')
        self.web_url = 'https://tequila-api.kiwi.com/v2/search?'
        self.fly_from = ''
        self.fly_to = ''
        self.dateFrom = ''
        self.dateTo = ''
        self.header = {
            'apikey': self.api_key
        }
        self.params = {}

    def get_flights(self, fly_from, fly_to, datefrom, dateto):
        """Get all flight from x to y in specific dates range"""
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.dateFrom = datefrom
        self.dateTo = dateto

        self.params = {
            'fly_from': self.fly_from,
            'fly_to':  self.fly_to,
            'date_from': self.dateFrom,
            'date_to': self.dateTo,
        }
        return requests.get(url=self.web_url, params=self.params, headers=self.header).json()




