import pandas as pd
import numpy as np

df = pd.read_csv("data/nse_daily_returns.csv")

portfolio_returns = (
    df.groupby("Date")["daily_return"]
      .mean()
      .reset_index()
)

returns = portfolio_returns["daily_return"]

var_95 = np.percentile(returns, 5)
var_99 = np.percentile(returns, 1)

cvar_95 = returns[returns <= var_95].mean()
cvar_99 = returns[returns <= var_99].mean()

results = pd.DataFrame({
    "metric": [
        "Historical VaR 95%",
        "Historical VaR 99%",
        "CVaR 95%",
        "CVaR 99%"
    ],
    "value": [
        var_95,
        var_99,
        cvar_95,
        cvar_99
    ]
})

results.to_csv(
    "data/nse_var_cvar_results.csv",
    index=False
)

print(results)