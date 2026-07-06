import pytest
import pandas as pd
from src.modeling import evaluate_forecast

def test_evaluate_forecast():
    actual = pd.Series([100, 102, 104])
    predicted = pd.Series([101, 103, 105])
    metrics = evaluate_forecast(actual, predicted)
    assert metrics is not None
    assert metrics["MAE"] == 1.0
