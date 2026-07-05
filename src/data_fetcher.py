import yfinance as yf
import pandas as pd

def fetch_prices(tickers, start, end):
    """Download adjusted close prices and return DataFrame."""
    data = yf.download(tickers, start=start, end=end, auto_adjust=False)['Adj Close']
    data.dropna(inplace=True)
    return data

def compute_returns(prices):
    return prices.pct_change().dropna()
