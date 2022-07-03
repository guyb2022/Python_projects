from sms_handler import Sender
from weather_report import Weather


weather = Weather()
weather.set_params(35.605528, 32.688282, 'current,minutely,daily')
forcast = weather.get_weather_forcast()

sms_sender = Sender()

rainy_day = False
# check last 12 hours to see if the forecasts has a rainy condition
for index in range(12):
    if int(forcast['hourly'][index]['weather'][0]['id']) < 700:
        rainy_day = True
        break
# Send the SMS
if rainy_day:
    sms_sender.send_sms(["It's going to be a rainy day"])
else:
    sms_sender.send_sms(["It's going to be a sunny day"])
