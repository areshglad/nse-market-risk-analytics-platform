import pandas as pd
import numpy as np

df = pd.read_csv("data/nse_daily_returns.csv")

df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values(["ticker", "Date"])

# 21-day rolling volatility
df["rolling_volatility_21d"] = (
    df.groupby("ticker")["daily_return"]
      .rolling(window=21)
      .std()
      .reset_index(level=0, drop=True)
)

# Annualized volatility
df["annualized_volatility"] = (
    df["rolling_volatility_21d"] * np.sqrt(252)
)

df.to_csv("data/nse_volatility.csv", index=False)

print("Volatility calculation complete")
print(df[["ticker",
          "Date",
          "daily_return",
          "rolling_volatility_21d",
          "annualized_volatility"]].tail())