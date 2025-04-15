import pandas as pd

stocks = pd.read_csv('data/it_company_stocks.csv')
currency = pd.read_csv('data/currency_exchange_rates.csv')

stocks['Date'] = pd.to_datetime(stocks['Date'])
currency['Date'] = pd.to_datetime(currency['Date'])

merged = pd.merge(stocks, currency, on='Date', how='left')
merged.to_csv('data/merged_data.csv', index=False)
