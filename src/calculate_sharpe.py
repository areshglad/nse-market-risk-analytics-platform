import pandas as pd
import numpy as np

df = pd.read_csv("data/nse_daily_returns.csv")

portfolio_returns = (
    df.groupby("Date")["daily_return"]
      .mean()
      .reset_index()
)

avg_daily_return = portfolio_returns["daily_return"].mean()
daily_volatility = portfolio_returns["daily_return"].std()

annual_return = avg_daily_return * 252
annual_volatility = daily_volatility * np.sqrt(252)

risk_free_rate = 0.065

sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility

results = pd.DataFrame({
    "metric": [
        "Annual Return",
        "Annual Volatility",
        "Risk Free Rate",
        "Sharpe Ratio"
    ],
    "value": [
        annual_return,
        annual_volatility,
        risk_free_rate,
        sharpe_ratio
    ]
})

results.to_csv("data/nse_sharpe_results.csv", index=False)

print(results)