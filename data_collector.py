import yfinance as yf
import pandas as pd

# Function to download stock data
def download_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data.reset_index(inplace=True)
    return stock_data

# Example: Collect data for Apple stock
apple_stock = download_stock_data('AAPL', '2020-01-01', '2023-01-01')
apple_stock.to_csv('apple_stock_data.csv', index=False)

