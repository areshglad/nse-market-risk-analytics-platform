import pandas as pd


ASSET_COLUMNS = [
    "HDFCBANK.NS",
    "INFY.NS",
    "ITC.NS",
    "RELIANCE.NS",
]


def prepare_weights(input_file, output_file):
    portfolio = pd.read_csv(input_file)

    weights = portfolio[ASSET_COLUMNS].iloc[0].reset_index()
    weights.columns = ["asset", "weight"]

    weights.to_csv(output_file, index=False)

    print(f"\nSaved: {output_file}")
    print(weights)


prepare_weights(
    "data/max_sharpe_portfolio.csv",
    "data/max_sharpe_weights.csv",
)

prepare_weights(
    "data/min_variance_portfolio.csv",
    "data/min_variance_weights.csv",
)
