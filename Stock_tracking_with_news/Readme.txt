This program check for a stock price daily return changes from: Alpha Vantage
If the change is above 5% then we collect all relevant news on it with: newsapi.org
Than we sent the news in SMS with: Twilio

For environment veraibles create an .env file under root
for example:
NEWS_API=<your newsapi api>
ALFA_API=<your alph api>
AUTH_TOKEN=<your token>
ACCOUNT_SID=<your account sid>
SMS_FROM=<the twilio number>
SMS_TO=<your phone number>

