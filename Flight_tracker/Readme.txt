We would like to track several location to fly
For each location we will search for a cheap flight with: tequila-api
Once a cheaper flight was found we will update the google sheet with: api.sheety.co
And than an SMS will be sent to the user with:Twilio

To use the Environment Varaibles create a file .env under root
For example:
# Sheety Google Sheets
SHT_API=<Your API>
SHT_USER=<user name>
SHT_PASS=<password>)
SHT_AUT=<sheety api>
# Tequila flight tracker
FLY_API=<flight api>
FLY_PASS=<flughts password>
# Twilio SMS sender
AUTH_TOKEN=<sms token>
ACCOUNT_SID=<sms sid>
SMS_FROM=<sms Twilio number>
SMS_TO=<your number>
