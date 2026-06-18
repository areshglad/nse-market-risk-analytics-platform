import pandas as pd

df = pd.read_csv("data/nse_daily_returns.csv")

returns_matrix = df.pivot(
    index="Date",
    columns="ticker",
    values="daily_return"
)

correlation_matrix = returns_matrix.corr()

print("\nCorrelation Matrix")
print(correlation_matrix)

correlation_matrix.to_csv(
    "data/correlation_matrix.csv"
)