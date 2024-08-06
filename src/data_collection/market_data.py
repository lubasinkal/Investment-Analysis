import yfinance as yf
import pandas as pd
from datetime import datetime

def download_data(ticker, start_date,end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')
    if isinstance(ticker, list):
        for i in ticker:
            data = yf.download(i, start = start_date, end = end_date)
            # data.to_csv(f"../data/raw/market data/{i}_{datetime.now().strftime('%Y-%m-%d')}.csv")
            data.to_csv(f"../data/raw/market data/{i}.csv")
    else:
        data = yf.download(ticker, start = start_date, end = end_date)
        # data.to_csv(f"../data/raw/market data/{ticker}_{datetime.now().strftime('%Y-%m-%d')}.csv")
        data.to_csv(f"../data/raw/market data/{i}.csv")


def main():
    ticker= ["AAPL","META","ABG.JO","MSFT"]
    start_date = '2000-01-01'
    end_date = datetime.today().strftime('%Y-%m-%d')
    download_data(ticker,start_date,end_date)


if __name__ == '__main__':
    main()