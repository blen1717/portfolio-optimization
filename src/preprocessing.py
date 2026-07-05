from statsmodels.tsa.stattools import adfuller

def check_stationarity(series, alpha=0.05):
    result = adfuller(series, autolag='AIC')
    is_stationary = result[1] <= alpha
    return {'statistic': result[0], 'pvalue': result[1], 'stationary': is_stationary}
