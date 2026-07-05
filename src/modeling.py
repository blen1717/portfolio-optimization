from pmdarima import auto_arima
import numpy as np

def fit_arima(train, seasonal=False, **kwargs):
    model = auto_arima(train, seasonal=seasonal, **kwargs)
    return model

def evaluate_forecast(actual, predicted):
    from sklearn.metrics import mean_absolute_error, mean_squared_error
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    return {'MAE': mae, 'RMSE': rmse, 'MAPE': mape}
