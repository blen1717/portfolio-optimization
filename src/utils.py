import matplotlib.pyplot as plt

def plot_forecast(actual, predicted, title="Forecast vs Actual"):
    plt.figure(figsize=(12, 6))
    plt.plot(actual.index, actual, label="Actual", color="blue")
    plt.plot(predicted.index, predicted, label="Predicted", color="red", linestyle="--")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
