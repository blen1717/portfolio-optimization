from pmdarima import auto_arima
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

def fit_arima(train, seasonal=False, **kwargs):
    try:
        model = auto_arima(train, seasonal=seasonal, error_action="ignore",
                           suppress_warnings=True, stepwise=True, **kwargs)
        return model
    except Exception as e:
        print(f"Error: {e}")
        return None

def evaluate_forecast(actual, predicted):
    try:
        mae = mean_absolute_error(actual, predicted)
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        mape = np.mean(np.abs((actual - predicted) / actual)) * 100
        return {"MAE": mae, "RMSE": rmse, "MAPE": mape}
    except Exception as e:
        print(f"Error: {e}")
        return None
