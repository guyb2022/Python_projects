import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Loading the environment variables
load_dotenv(".env")


class TickerSymbol:
    """Class to get the stock data and return a data frame"""
    def __init__(self):
        """Init of variables"""
        self.ticker = ""
        self.web_url = 'https://www.alphavantage.co/query'
        self.api_key = os.getenv('ALFA_API')

    def get_data(self):
        """Get the stock data from the site"""
        response = requests.get(f'{self.web_url}?function=TIME_SERIES_DAILY&symbol={self.ticker}&apikey={self.api_key}')
        data = response.json()['Time Series (Daily)']
        data_list = [(key, value) for (key, value) in data.items()]
        # create the df for later purpose, although we only need the last day
        df_data = pd.DataFrame(columns=['Date', 'open', 'high', 'low', 'close', 'volume'])

        for index in range(len(data_list)):
            df2 = {'Date': pd.to_datetime(data_list[index][0], format='%Y-%m-%d'),
                   'open': data_list[index][1]['1. open'], 'high': data_list[index][1]['2. high'],
                   'low': data_list[index][1]['3. low'], 'close': float(data_list[index][1]['4. close']),
                   'volume': data_list[index][1]['5. volume']}
            df_data = df_data.append(df2, ignore_index=True)
        df_data = df_data.set_index('Date')

        return df_data

    def get_daily_returns(self, ticker):
        """Calculate the daily returns for each day"""
        self.ticker = ticker
        df_stock = self.get_data()
        df_stock.to_csv(f'{self.ticker}_data.csv')
        df_stock = df_stock.sort_values(by='Date', ascending=True)
        df_stock['daily_returns %'] = df_stock['close'].pct_change() * 100
        df_stock = df_stock.sort_values(by='Date', ascending=False)
        daily_returns = round(df_stock['daily_returns %'].head(1).values[0], 3)

        return daily_returns
