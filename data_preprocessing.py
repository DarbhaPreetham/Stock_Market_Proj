import yfinance as yf
import pandas as pd

# Fetch Apple stock data
apple_stock = yf.download('AAPL', start='2020-01-01', end='2023-01-01')

# Add moving average features and other technical indicators
def add_technical_indicators(df):
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()
    df['Price_Change'] = df['Close'].pct_change()
    df['Volatility'] = df['Close'].rolling(window=30).std()
    return df.dropna()

# Process stock data
processed_data = add_technical_indicators(apple_stock)

# Save the processed data to CSV
processed_data.to_csv('apple_stock_processed.csv', index=False)
