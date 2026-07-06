from pypfopt import EfficientFrontier
import pandas as pd

def optimize_max_sharpe(expected_returns, cov_matrix):
    try:
        ef = EfficientFrontier(pd.Series(expected_returns), cov_matrix)
        ef.max_sharpe()
        return ef.clean_weights()
    except Exception as e:
        print(f"Error: {e}")
        return {asset: 1/len(expected_returns) for asset in expected_returns}
