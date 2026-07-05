import numpy as np
from pypfopt import EfficientFrontier

def optimize_portfolio(expected_returns, cov_matrix, risk_free_rate=0.02):
    ef = EfficientFrontier(expected_returns, cov_matrix)
    weights = ef.max_sharpe(risk_free_rate=risk_free_rate)
    return ef.clean_weights()
