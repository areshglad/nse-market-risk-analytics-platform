import os
import pandas as pd
import numpy as np

df = pd.read_csv("data/nse_daily_returns.csv")

df["Date"] = pd.to_datetime(df["Date"])

returns_pivot = df.pivot(
    index="Date",
    columns="ticker",
    values="daily_return"
)

returns_pivot = returns_pivot.dropna()

print("Return matrix created")
print("Shape:", returns_pivot.shape)
print(returns_pivot.head())

# Expected annual returns
expected_returns = returns_pivot.mean() * 252

# Annual covariance matrix
cov_matrix = returns_pivot.cov() * 252

print("\nExpected Returns")
print(expected_returns)

print("\nCovariance Matrix")
print(cov_matrix)



num_portfolios = 10000

results = []

for _ in range(num_portfolios):

    weights = np.random.random(len(expected_returns))
    weights /= np.sum(weights)

    portfolio_return = np.sum(weights * expected_returns)

    portfolio_volatility = np.sqrt(
        np.dot(
            weights.T,
            np.dot(cov_matrix, weights)
        )
    )

    sharpe_ratio = portfolio_return / portfolio_volatility

    results.append([
        portfolio_return,
        portfolio_volatility,
        sharpe_ratio,
        *weights
    ])

columns = [
    "return",
    "volatility",
    "sharpe"
] + list(expected_returns.index)

portfolio_df = pd.DataFrame(
    results,
    columns=columns
)

print(portfolio_df.head())

portfolio_df.to_csv(
    "data/random_portfolios.csv",
    index=False
)

print("10,000 portfolios generated")



# Maximum Sharpe Portfolio

max_sharpe_portfolio = portfolio_df.loc[
    portfolio_df["sharpe"].idxmax()
]

# Minimum Variance Portfolio

min_variance_portfolio = portfolio_df.loc[
    portfolio_df["volatility"].idxmin()
]

print("\nMaximum Sharpe Portfolio")
print(max_sharpe_portfolio)

print("\nMinimum Variance Portfolio")
print(min_variance_portfolio)

max_sharpe_portfolio.to_frame().T.to_csv(
    "data/max_sharpe_portfolio.csv",
    index=False
)

min_variance_portfolio.to_frame().T.to_csv(
    "data/min_variance_portfolio.csv",
    index=False
)


portfolio_df.to_csv(
    "data/efficient_frontier.csv",
    index=False
)

print("Efficient Frontier dataset saved")