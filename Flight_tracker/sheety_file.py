import requests
from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth
import pandas as pd

# Loading the environment variables
load_dotenv(".env")
# Setting security level to basic
basic = HTTPBasicAuth(os.getenv('SHT_USER'), os.getenv('SHT_PASS'))


class Sheety:
    """Sheety CLass"""
    def __init__(self):
        """Init Sheety class params"""
        self.api_key = os.getenv("SHT_API")
        self.url_web = f'https://api.sheety.co/{self.api_key}/flightsBooking/prices'
        self.auth = os.getenv('SHT_AUTH')
        self.city = ""
        self.iata_code = ""
        self.lowest_price = ""
        self.row_id = ""
        self.bargain_price = 0
        self.params = {}

    def set_data(self, city, iata_code, lowest_price, bargain_price=0):
        """Set data to be post or put"""
        self.city = city
        self.iata_code = iata_code
        self.lowest_price = lowest_price
        self.bargain_price = bargain_price
        self.params = {
            'price': {
                "city": self.city,
                "iataCode": self.iata_code,
                "lowestPrice": self.lowest_price,
                "bargainPrice": self.bargain_price
            }
        }

    def get_request(self):
        """Get data from sheet"""
        data = requests.get(url=self.url_web, auth=basic).json()
        print(data)
        df = pd.DataFrame()
        for dict_item in data['prices']:
            d = {'id': dict_item['id'], 'city': dict_item['city'], 'iata_code': dict_item['iataCode'],
                 'lowestPrice': dict_item['lowestPrice'], 'bargainPrice': dict_item['bargainPrice']}
            df2 = pd.DataFrame([d])
            df = pd.concat([df, df2], ignore_index=True)
        return df

    def post_request(self, city, iata_code, lowest_price, bargain_price):
        """Post data to sheet"""
        self.set_data(city, iata_code, lowest_price, bargain_price)
        response = requests.post(url=self.url_web, json=self.params, auth=basic)
        print("response.status_code =", response.status_code)
        print("response.text= ", response.text)

    def put_request(self, row_id, new_value):
        """Put data on sheet"""
        self.row_id = row_id
        self.set_data(new_value[0], new_value[1], new_value[2], new_value[3])
        self.params = {
            'price': {
                "city": self.city,
                "iataCode": self.iata_code,
                "lowestPrice": self.lowest_price,
                "bargainPrice": self.bargain_price
            }
        }
        endpoint = f"{self.url_web}/{self.row_id}"
        response = requests.put(url=endpoint, json=self.params, auth=basic)
        print("response.status_code =", response.status_code)
        print("response.text= ", response.text)
