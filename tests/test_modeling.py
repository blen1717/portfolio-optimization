import pandas as pd
from src.modeling import fit_arima, evaluate_forecast

def test_arima_fit():
    train = pd.Series([1,2,3,4,5])
    model = fit_arima(train, max_p=1, max_q=1, d=0)
    assert model is not None
