import matplotlib.pyplot as plt
import pandas as pd

# Load the processed data
data = pd.read_csv('../data/processed/market data/processed_AAPL_data.csv', index_col=0)

# Display the first few rows of the dataset
data.head()



# Plot the closing price
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Closing Price', color='blue')
plt.title('Closing Price of AAPL Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Plot closing price with moving averages
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Closing Price', color='blue')
plt.plot(data['MA_30'], label='30-Day Moving Average', color='red')
plt.plot(data['MA_100'], label='100-Day Moving Average', color='green')
plt.title('AAPL Closing Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Plot daily log returns
plt.figure(figsize=(12, 6))
plt.plot(data['Log Returns'], label='Log Returns', color='blue')
plt.title('Daily Log Returns of AAPL')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.grid(True)
plt.show()


# Plot cumulative returns
plt.figure(figsize=(12, 6))
plt.plot(data['Cumulative Percentage Return'], label='Cumulative Percentage Return', color='blue')
plt.title('Cumulative Percentage Return of AAPL')
plt.xlabel('Date')
plt.ylabel('Cumulative Return (%)')
plt.grid(True)
plt.show()

# Plot rolling volatility
plt.figure(figsize=(12, 6))
plt.plot(data['Volatility 30'], label='30-Day Rolling Volatility', color='red')
plt.title('30-Day Rolling Volatility of AAPL')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.grid(True)
plt.show()

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
plt.title('Volatility for AAPL')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
