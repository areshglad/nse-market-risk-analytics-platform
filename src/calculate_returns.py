import os
import pandas as pd
import numpy as np

prices = pd.read_csv("data/nse_stock_prices.csv")

prices["Date"] = pd.to_datetime(prices["Date"])
prices = prices.sort_values(["ticker", "Date"])

prices["daily_return"] = prices.groupby("ticker")["Close"].pct_change()
prices["log_return"] = prices.groupby("ticker")["Close"].transform(
    lambda x: np.log(x / x.shift(1))
)

returns = prices.dropna(subset=["daily_return", "log_return"])

os.makedirs("data", exist_ok=True)

returns.to_csv("data/nse_daily_returns.csv", index=False)

print("Daily returns created successfully")
print("Shape:", returns.shape)
print("Columns:", returns.columns.tolist())
print(returns.head())
