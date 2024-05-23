import yfinance as yf
import pandas as pd
import argparse
from datetime import datetime, timedelta

def download_stock_data(ticker, start_date, end_date, interval='5m'):
    """
    Download stock data from Yahoo Finance in chunks of 7 days to bypass limitations on 5m interval data.

    :param ticker: str, Stock ticker symbol.
    :param start_date: datetime, Start date.
    :param end_date: datetime, End date.
    :param interval: str, Data interval. Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo].
    :return: pd.DataFrame, Stock data.
    """
    all_data = []

    while start_date < end_date:
        chunk_end_date = min(start_date + timedelta(days=7), end_date)
        stock_data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=chunk_end_date.strftime('%Y-%m-%d'), interval=interval)
        
        if not stock_data.empty:
            all_data.append(stock_data)
        start_date = chunk_end_date

    if all_data:
        return pd.concat(all_data)
    else:
        return pd.DataFrame()

def save_to_csv(dataframe, filename):
    """
    Save DataFrame to a CSV file.

    :param dataframe: pd.DataFrame, Data to save.
    :param filename: str, Path to the file where data will be saved.
    """
    dataframe.to_csv(filename, index=True)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    # Default dates: from 60 days ago to yesterday
    end_date_default = datetime.today() - timedelta(days=1)
    start_date_default = end_date_default - timedelta(days=60)

    parser = argparse.ArgumentParser(description='Download stock data from Yahoo Finance.')
    parser.add_argument('ticker', type=str, help='Stock ticker symbol')
    parser.add_argument('--start_date', type=str, default=start_date_default.strftime('%Y-%m-%d'), help='Start date in the format YYYY-MM-DD (default: 60 days ago)')
    parser.add_argument('--end_date', type=str, default=end_date_default.strftime('%Y-%m-%d'), help='End date in the format YYYY-MM-DD (default: yesterday)')
    parser.add_argument('--interval', type=str, default='5m', help='Data interval (default: 5m)')

    args = parser.parse_args()

    ticker = args.ticker
    start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
    end_date = datetime.strptime(args.end_date, '%Y-%m-%d')
    interval = args.interval

    # Download stock data
    stock_data = download_stock_data(ticker, start_date, end_date, interval)

    if not stock_data.empty:
        # Save to CSV
        filename = f"{ticker}_stock_data.csv"
        save_to_csv(stock_data, filename)
    else:
        print("No data downloaded.")
