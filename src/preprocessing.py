from statsmodels.tsa.stattools import adfuller

def check_stationarity(series):
    try:
        result = adfuller(series.dropna())
        return {
            "statistic": result[0],
            "pvalue": result[1],
            "stationary": result[1] <= 0.05
        }
    except Exception as e:
        print(f"Error: {e}")
        return None
