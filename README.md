# Moving Average Crossover Strategy – NIFTY 50

This project implements a basic **moving average crossover trading strategy** using Python. It fetches historical **NIFTY 50** index data and generates **buy/sell signals** based on the crossover of short-term and long-term moving averages.

## 📈 Strategy Overview

The **moving average crossover strategy** is a popular momentum-based trading approach. It involves:

- **Short-Term MA (e.g., 20-day)**: Captures recent trends.
- **Long-Term MA (e.g., 50-day)**: Represents broader trends.
- **Buy Signal**: When short MA crosses above long MA.
- **Sell Signal**: When short MA crosses below long MA.

## 🛠️ Technologies Used

- **Python**
- **pandas** – for data manipulation
- **yfinance** – to fetch historical stock/index data
- **matplotlib** – for visualizing price and signals

## 🔍 Features

- Fetches NIFTY 50 index data using `yfinance`
- Calculates short and long moving averages
- Generates buy/sell signals based on MA crossover
- Plots price chart with annotated entry/exit points

## 🧪 Example Output

![Strategy Chart](path-to-sample-plot.png)

> *Shows NIFTY 50 closing price with buy/sell signals based on 20/50 MA crossover.*

## 📦 Installation

```bash
pip install pandas yfinance matplotlib
