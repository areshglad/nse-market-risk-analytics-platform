import pandas as pd
import numpy as np

df = pd.read_csv("data/nse_daily_returns.csv")

# Equal-weighted portfolio return
portfolio_returns = (
    df.groupby("Date")["daily_return"]
      .mean()
      .reset_index()
)

portfolio_returns.rename(
    columns={"daily_return": "portfolio_daily_return"},
    inplace=True
)

var_95 = np.percentile(portfolio_returns["portfolio_daily_return"], 5)
var_99 = np.percentile(portfolio_returns["portfolio_daily_return"], 1)

results = pd.DataFrame({
    "metric": ["Historical VaR 95%", "Historical VaR 99%"],
    "value": [var_95, var_99]
})

results.to_csv("data/nse_var_results.csv", index=False)

print("Historical VaR calculation complete")
print(results)