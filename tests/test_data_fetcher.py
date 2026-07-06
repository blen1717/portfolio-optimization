import pytest
from src.data_fetcher import fetch_prices

def test_fetch_prices():
    data = fetch_prices(["TSLA"], "2023-01-01", "2023-01-10")
    assert data is not None
    assert not data.empty
