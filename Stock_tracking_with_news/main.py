from stocks_data import TickerSymbol
from sms_sender import Sender
from news import News
from datetime import datetime

import warnings
warnings.filterwarnings("ignore")


if __name__ == "__main__":
    date = datetime.today().strftime('%Y-%m-%d')
    symbol = 'NVDA'
    # Create the stock object
    stock = TickerSymbol()
    daily_return = stock.get_daily_returns(symbol)
    # Create the news object
    news = News()
    news.set_params(symbol, date)
    articles = news.get_news()
    # Create the sms object
    sms = Sender()

    if daily_return >= 0:
        sign = '🔺'
    else:
        sign = '🔻'

    # Get the latest 3 news
    articles = [f"{symbol}: {sign}{daily_return}%\n Headline: {article['title']}.\nBrief: {article['description']}\n"
                for article in articles[0:3]]
    # send the SMS if stock daily return rise more than 5%
    if daily_return > 0.05:
        sms.send_sms(articles)


"""

"""