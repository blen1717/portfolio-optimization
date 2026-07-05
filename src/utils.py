import matplotlib.pyplot as plt
import seaborn as sns

def plot_forecast(actual, predicted, title="Forecast vs Actual"):
    plt.figure(figsize=(12,6))
    plt.plot(actual.index, actual, label='Actual')
    plt.plot(predicted.index, predicted, label='Predicted', linestyle='--')
    plt.title(title)
    plt.legend()
    plt.grid()
    return plt.gcf()
