import pandas as pd
import os

data_dir = '../data/raw/market data/'
files = os.listdir(data_dir)
print(files)


data = pd.read_csv(f'{data_dir}AAPL.csv')
print(data.head())
print(data.describe())
import matplotlib.pyplot as plt

# Plot the closing price over time
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Closing Price')
plt.title('Closing Price of AAPL')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()
data['MA_30'] = data['Close'].rolling(window=30).mean()
data['MA_100'] = data['Close'].rolling(window=100).mean()

plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Closing Price')
plt.plot(data['MA_30'], label='30-Day Moving Average')
plt.plot(data['MA_100'], label='100-Day Moving Average')
plt.title('AAPL Closing Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()


#### RETURNS

data['Daily Returns'] = data['Close'].pct_change()

# Plot daily returns
plt.figure(figsize=(12, 6))
plt.plot(data['Daily Returns'], label='Daily Returns')
plt.title('Daily Returns for AAPL')
plt.xlabel('Date')
plt.ylabel('Return')
plt.grid(True)
plt.show()

import numpy as np
# Calculate returns and add to DataFrame
data["Log Returns"] = np.log(data["Close"] / data["Close"].shift(1))
# Calculate cumulative log returns
data['Cumulative Log Returns'] = data['Log Returns'].cumsum()

# Calculate cumulative returns from cumulative log returns
data['Cumulative Returns'] = np.exp(data['Cumulative Log Returns']) - 1

# Convert cumulative returns to percentage
data['Cumulative Percentage Return'] = data['Cumulative Returns'] * 100

# Plot daily returns
plt.figure(figsize=(12, 6))
plt.plot(data['Log Returns'], label='Log Returns')
plt.title('Log Returns for AAPL')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.grid(True)
plt.show()


# Plot cumulative returns
plt.figure(figsize=(12, 6))
plt.plot(data['Cumulative Percentage Return'], label='Cumulative Percentage Return')
plt.title('Cumulative Percentage Return for AAPL')
plt.xlabel('Date')
plt.ylabel('Cumulative Return (%)')
plt.grid(True)
plt.show()

# Calculate rolling statistics
data['Rolling Mean'] = data['Log Returns'].rolling(window=30).mean()
data['Rolling Std'] = data['Log Returns'].rolling(window=30).std()

# Plot rolling statistics
plt.figure(figsize=(12, 6))
plt.plot(data['Log Returns'], label='Log Returns')
plt.plot(data['Rolling Mean'], label='30-Day Rolling Mean')
plt.plot(data['Rolling Std'], label='30-Day Rolling Std')
plt.title('Log Returns with Rolling Statistics for AAPL')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.legend()
plt.grid(True)
plt.show()
print(data.head())

data['Volatility 30'] = data['Log Returns'].rolling(window=30).std()
data['Volatility 100'] = data['Log Returns'].rolling(window=100).std()

import matplotlib.pyplot as plt

# Plot log returns and volatility
plt.figure(figsize=(14, 7))

# Plot log returns
plt.subplot(2, 1, 1)
plt.plot(data['Log Returns'], label='Log Returns', color='blue')
plt.title('Log Returns for AAPL')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.grid(True)
plt.legend()

# Plot volatility
plt.subplot(2, 1, 2)
plt.plot(data['Volatility 30'], label='Volatility (30-Day Rolling Std)', color='red')
plt.plot(data['Volatility 100'], label='Volatility (100-Day Rolling Std)', color='orange')
plt.title('Volatility for AAPL')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

data.to_csv('../data/processed/market data/processed_AAPL_data.csv')
data.head()


