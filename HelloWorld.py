import requests
import pandas as pd
from tqdm import tqdm

# Replace with your actual Alpha Vantage API key
api_key = 'YOUR_API_KEY'

# Function to fetch stock data from Alpha Vantage
def fetch_stock_data(symbol):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key,
        'outputsize': 'compact'
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Check if 'Time Series (Daily)' key is in the response
    if 'Time Series (Daily)' in data:
        df = pd.DataFrame(data['Time Series (Daily)']).T
        df.index = pd.to_datetime(df.index)
        df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        df = df.astype(float)
        return df
    else:
        print(f"Error fetching data for {symbol}: {data}")
        return None

# List of stock ticker symbols (example)
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']  # Replace with your list

# Dictionary to store stock data
stock_data = {}

# Fetch data for each ticker
for ticker in tqdm(tickers, desc="Fetching data"):
    stock_data[ticker] = fetch_stock_data(ticker)

# Example: Combine all data into a single DataFrame
all_data = pd.concat(stock_data.values(), keys=stock_data.keys())

# Display the combined data
print(all_data.head())
