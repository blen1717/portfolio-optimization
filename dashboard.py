
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Page config
st.set_page_config(
    page_title="Portfolio Optimizer",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Portfolio Optimization Dashboard")
st.markdown("Modern Portfolio Theory with TSLA, BND, and SPY")

# Sidebar
st.sidebar.header("⚙️ Portfolio Settings")

# Date range selector
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2015-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2025-12-31"))

# Download data button
if st.sidebar.button("📥 Update Data"):
    with st.spinner("Downloading data..."):
        tickers = ['TSLA', 'BND', 'SPY']
        data = yf.download(tickers, start=start_date, end=end_date, progress=False)
        prices = data['Close']
        returns = prices.pct_change().dropna()
        st.session_state['prices'] = prices
        st.session_state['returns'] = returns
        st.session_state['tickers'] = tickers
        st.success("✅ Data updated!")

# Check if data exists
if 'prices' not in st.session_state:
    # Load default data
    tickers = ['TSLA', 'BND', 'SPY']
    data = yf.download(tickers, start='2015-01-01', end='2025-12-31', progress=False)
    prices = data['Close']
    returns = prices.pct_change().dropna()
    st.session_state['prices'] = prices
    st.session_state['returns'] = returns
    st.session_state['tickers'] = tickers

prices = st.session_state['prices']
returns = st.session_state['returns']
tickers = st.session_state['tickers']

# ============================================
# MAIN CONTENT
# ============================================

# Row 1: Key Metrics
st.subheader("📈 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

mean_returns = returns.mean() * 252
std_returns = returns.std() * np.sqrt(252)
sharpe = mean_returns / std_returns

col1.metric("📊 Assets", len(tickers))
col2.metric("📅 Trading Days", len(prices))
col3.metric("📈 Avg Return", f"{mean_returns.mean():.2%}")
col4.metric("⚖️ Avg Risk", f"{std_returns.mean():.2%}")

# Row 2: Price Chart
st.subheader("📊 Price History")
fig, ax = plt.subplots(figsize=(12, 6))
for ticker in tickers:
    ax.plot(prices.index, prices[ticker], label=ticker, linewidth=2)
ax.set_xlabel("Date")
ax.set_ylabel("Price ($)")
ax.legend()
ax.grid(True, alpha=0.3)
st.pyplot(fig)

# Row 3: Asset Statistics
st.subheader("📊 Asset Statistics")
stats_df = pd.DataFrame({
    'Asset': tickers,
    'Annual Return': mean_returns.values,
    'Annual Risk': std_returns.values,
    'Sharpe Ratio': sharpe.values
})
stats_df['Annual Return'] = stats_df['Annual Return'].apply(lambda x: f"{x:.2%}")
stats_df['Annual Risk'] = stats_df['Annual Risk'].apply(lambda x: f"{x:.2%}")
stats_df['Sharpe Ratio'] = stats_df['Sharpe Ratio'].apply(lambda x: f"{x:.3f}")
st.dataframe(stats_df, use_container_width=True)

# Row 4: Portfolio Optimization
st.subheader("⚖️ Portfolio Optimization")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Adjust Asset Weights")
    w1 = st.slider("TSLA Weight (%)", 0, 100, 60)
    w2 = st.slider("SPY Weight (%)", 0, 100, 10)
    w3 = 100 - w1 - w2
    
    if w3 < 0:
        st.error("Weights exceed 100%!")
    else:
        st.write(f"BND Weight: {w3}%")
        
        weights = np.array([w1/100, w2/100, w3/100])
        port_return = np.dot(weights, mean_returns)
        port_risk = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
        port_sharpe = port_return / port_risk if port_risk > 0 else 0
        
        st.metric("Portfolio Return", f"{port_return:.2%}")
        st.metric("Portfolio Risk", f"{port_risk:.2%}")
        st.metric("Sharpe Ratio", f"{port_sharpe:.3f}")
        with col2:
    st.markdown("Recommended Allocation")
    # Show optimal weights from your analysis
    optimal = {'TSLA': 59.8, 'SPY': 10.6, 'BND': 29.6}
    st.write(f"📌 TSLA: {optimal['TSLA']}%")
    st.write(f"📌 SPY: {optimal['SPY']}%")
    st.write(f"📌 BND: {optimal['BND']}%")
    st.info("💡 This allocation maximizes risk-adjusted returns (Sharpe Ratio: 0.991)")

st.markdown("---")
st.caption("Built with ❤️ for 10 Academy Week 12 Capstone | Data from Yahoo Finance")
