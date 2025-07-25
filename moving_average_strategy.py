import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch NIFTY 50 data using Yahoo Finance symbol for NIFTY 50 index
nifty = yf.download("^NSEI", start="2021-01-01", end="2023-01-01")

# Define short-term and long-term moving averages
short_window = 20
long_window = 50

# Calculate moving averages
nifty['Short_MA'] = nifty['Close'].rolling(window=short_window, min_periods=1).mean()
nifty['Long_MA'] = nifty['Close'].rolling(window=long_window, min_periods=1).mean()

# Generate signals: Buy when short MA crosses above long MA, sell when it goes below
nifty['Signal'] = 0
nifty['Signal'][short_window:] = \
    (nifty['Short_MA'][short_window:] > nifty['Long_MA'][short_window:]).astype(int)

# Generate trading positions: 1 means buy, 0 means sell/hold
nifty['Position'] = nifty['Signal'].diff()

# Plotting
plt.figure(figsize=(14, 6))
plt.plot(nifty['Close'], label='NIFTY 50 Close Price', alpha=0.5)
plt.plot(nifty['Short_MA'], label=f'{short_window}-Day MA', color='green')
plt.plot(nifty['Long_MA'], label=f'{long_window}-Day MA', color='red')

# Mark buy/sell signals
plt.plot(nifty[nifty['Position'] == 1].index,
         nifty['Short_MA'][nifty['Position'] == 1],
         '^', markersize=10, color='g', label='Buy Signal')
plt.plot(nifty[nifty['Position'] == -1].index,
         nifty['Short_MA'][nifty['Position'] == -1],
         'v', markersize=10, color='r', label='Sell Signal')

plt.title("Moving Average Crossover Strategy – NIFTY 50")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()
