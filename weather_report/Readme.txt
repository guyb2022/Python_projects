This program track the weather report: api.openweathermap.org
according to the user coordinates (latitude, longitude)
When the desire condition are met (sunny/rainy) an SMS is sent:  Twilio API

To use the environment severable, create a file .env under the root
For example:
# Weather report
API_KEY=<your api key>
# Twilio SMS sender
AUTH_TOKEN=<your token>
ACCOUNT_SID=<yout account sid>
SMS_FROM=<twilio phone number>
SMS_TO=<your phone number>
