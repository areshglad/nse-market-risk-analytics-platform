import pandas as pd

df = pd.read_csv("data/nse_daily_returns.csv")

portfolio_returns = (
    df.groupby("Date")["daily_return"]
      .mean()
      .reset_index()
)

portfolio_returns["cumulative_return"] = (
    1 + portfolio_returns["daily_return"]
).cumprod()

portfolio_returns["running_max"] = (
    portfolio_returns["cumulative_return"]
).cummax()

portfolio_returns["drawdown"] = (
    portfolio_returns["cumulative_return"]
    /
    portfolio_returns["running_max"]
) - 1

max_drawdown = portfolio_returns["drawdown"].min()

print("\nMaximum Drawdown")
print(max_drawdown)

portfolio_returns.to_csv(
    "data/nse_drawdown.csv",
    index=False
)
