from sms_handler import Sender
from sheety_file import Sheety
from flight_track import FlightTrack
import warnings
from datetime import datetime, timedelta

warnings.filterwarnings("ignore")

today = datetime.today().strftime('%d/%m/%Y')
half_month = (datetime.today() + timedelta(days=180)).strftime('%d/%m/%Y')
sheety_data = Sheety()
# Init the Sheety
df_data = sheety_data.get_request()
flight_track = FlightTrack()
# Init the SMS sender
sender = Sender()


def find_minimum_price():
    """
    Search the sites on the df and find cheaper flight
    Once found update the price in the google sheet and send an SMS
    """
    for row in df_data.iterrows():
        response = flight_track.get_flights('STN', row[1]['iata_code'], str(today), str(half_month))
        find_bargain = False
        for index in range(len(response['data'])):
            if response['data'][index]['price'] <  row[1]['lowestPrice']:
                min_price = response['data'][index]['price']
                find_bargain = True
        if find_bargain:
            print(f"Found new bargain price: {min_price} for: { row[1]['iata_code']}")
            sheety_data.put_request(row[1]['id'], [row[1]['city'], row[1]['iata_code'],
                                                   row[1]['lowestPrice'], min_price])
            sender.send_sms([f"Found great Deal!!!\n From London: STN to {row[1]['city']}: {row[1]['iata_code']}\n"
                            f"Only ${min_price} instead of ${row[1]['lowestPrice']}"])


if __name__ == '__main__':
    find_minimum_price()



