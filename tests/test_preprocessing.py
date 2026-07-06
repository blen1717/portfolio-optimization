import pytest
import pandas as pd
import numpy as np
from src.preprocessing import check_stationarity

def test_stationarity():
    np.random.seed(42)
    series = pd.Series(np.cumsum(np.random.randn(100)))
    result = check_stationarity(series)
    assert result is not None
    assert result["stationary"] == False
