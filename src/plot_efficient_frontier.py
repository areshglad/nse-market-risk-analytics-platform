import pandas as pd
import matplotlib.pyplot as plt

portfolio_df = pd.read_csv("data/efficient_frontier.csv")

max_sharpe = portfolio_df.loc[
    portfolio_df["sharpe"].idxmax()
]

min_volatility = portfolio_df.loc[
    portfolio_df["volatility"].idxmin()
]

plt.figure(figsize=(12,8))

plt.scatter(
    portfolio_df["volatility"],
    portfolio_df["return"],
    c=portfolio_df["sharpe"],
    cmap="viridis"
)

plt.colorbar(label="Sharpe Ratio")

plt.scatter(
    max_sharpe["volatility"],
    max_sharpe["return"],
    marker="*",
    s=400,
    label="Max Sharpe Portfolio"
)

plt.scatter(
    min_volatility["volatility"],
    min_volatility["return"],
    marker="X",
    s=300,
    label="Minimum Variance Portfolio"
)

plt.xlabel("Volatility")
plt.ylabel("Expected Return")
plt.title("Efficient Frontier")

plt.legend()

plt.savefig(
    "outputs/efficient_frontier.png",
    bbox_inches="tight"
)

plt.show()