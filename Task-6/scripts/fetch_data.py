import yfinance as yf
import pandas as pd

symbol = "^CNXIT"
start_date = "2020-01-01"
end_date = "2024-12-31"

data = yf.download(symbol, start=start_date, end=end_date)
data.to_csv("data/historical_prices.csv")
print(f"Downloaded data for {symbol} saved to data/historical_prices.csv")
