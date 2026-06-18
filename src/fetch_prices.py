import os
import pandas as pd
import yfinance as yf

tickers = [
    "HDFCBANK.NS",
    "RELIANCE.NS",
    "INFY.NS",
    "ITC.NS",
    "TATAMOTORS.NS"
]

start_date = "2023-01-01"

all_data = []

for ticker in tickers:
    print(f"Downloading data for {ticker}")

    data = yf.download(
        ticker,
        start=start_date,
        auto_adjust=False,
        progress=False
    )

    # If yfinance returns multi-level columns, flatten them
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # Move index date into a normal column
    data = data.reset_index()

    # Rename first column to Date safely
    data.rename(columns={data.columns[0]: "Date"}, inplace=True)

    data["ticker"] = ticker

    required_columns = ["Date", "ticker", "Open", "High", "Low", "Close", "Volume"]

    if "Adj Close" in data.columns:
        required_columns.append("Adj Close")

    data = data[required_columns]

    all_data.append(data)

final_data = pd.concat(all_data, ignore_index=True)

os.makedirs("data", exist_ok=True)

final_data.to_csv("data/nse_stock_prices.csv", index=False)

print("Download complete")
print("Shape:", final_data.shape)
print("Columns:", final_data.columns.tolist())
print(final_data.head())