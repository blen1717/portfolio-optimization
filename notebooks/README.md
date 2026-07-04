# Week 9 Challenge – Interim Submission

## 📌 Overview
This repository contains our progress for the interim submission of the 10 Academy Week 9 challenge.  
We have completed Task 1 (full EDA, stationarity testing, risk metrics) and Task 2 (ARIMA modelling on TSLA).  

All code is contained in the Jupyter notebook Week9_Interim.ipynb, which runs in Google Colab.  

---

## 📊 Data
- Source: Yahoo Finance (yfinance)  
- Tickers: TSLA, BND, SPY  
- Period: 2015-01-01 to 2026-06-30  
- Fields: Adjusted close prices, daily returns  

Data files are stored in the data/ directory.

---

## 🔍 Task 1 – Exploratory Data Analysis

### Key Visualisations (saved in results/plots/)
- Closing prices over time – shows long‑term trends and volatility.
- Daily returns – reveals volatility clustering and extreme events.
- 30‑day rolling volatility (annualised) – highlights periods of market stress.
- Correlation heatmap – shows relationships between the three assets.

### Stationarity Tests (ADF)
- Prices: Non‑stationary (p‑value > 0.05 for all assets).  
- Returns: Stationary (p‑value < 0.05 for all assets).  
⇒ We will use d=1 (first difference) in ARIMA/SARIMA models.

### Risk Metrics (Annualised)
| Asset | VaR (95%) | CVaR (95%) | Sharpe Ratio | Max Drawdown | Volatility |
|-------|-----------|------------|--------------|--------------|------------|
| TSLA  | -4.12%    | -6.87%     | 0.68         | -73.6%       | 58.3%      |
| BND   | -0.58%    | -0.74%     | 0.45         | -10.2%       | 5.2%       |
| SPY   | -1.53%    | -2.31%     | 0.79         | -33.7%       | 17.4%      |

---

## 📈 Task 2 – ARIMA Model (Initial)

- Target: TSLA price  
- Training: 2015–2024  
- Testing: 2025–2026  
- Optimal order: (1,1,1) (found by auto_arima)  

Performance on test set:
- RMSE: $28.45  
- MAE:  $22.12  
- MAPE: 8.34%  

The forecast vs actual plot is available in results/plots/arima_forecast.png.

---

## 🚀 Next Steps (Final Submission)
- Implement SARIMA (with weekly seasonality) and LSTM.
- Compare models (MAE, RMSE, MAPE).
- Generate 6‑month forecasts with confidence intervals.
- Optimise portfolio using Efficient Frontier (MPT).
- Backtest the recommended strategy against a 60/40 benchmark.

---

## 🔧 How to Run
1. Open Week9_Interim.ipynb in Google Colab or Jupyter.
2. Install dependencies from requirements.txt.
3. Run cells in order (all code is self‑contained).

---
