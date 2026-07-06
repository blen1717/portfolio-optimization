import yfinance as yf
import pandas as pd

def fetch_prices(tickers, start, end):
    try:
        data = yf.download(tickers, start=start, end=end, progress=False)
        if data.empty:
            return None
        if "Adj Close" in data.columns:
            prices = data["Adj Close"]
        else:
            prices = data["Close"]
        return prices.dropna()
    except Exception as e:
        print(f"Error: {e}")
        return None

def compute_returns(prices):
    return prices.pct_change().dropna()
