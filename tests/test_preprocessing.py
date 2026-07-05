import pandas as pd
from src.preprocessing import check_stationarity

def test_stationarity():
    # Create a random walk series
    np.random.seed(42)
    series = pd.Series(np.cumsum(np.random.randn(100)))
    result = check_stationarity(series)
    assert result['stationary'] == False
