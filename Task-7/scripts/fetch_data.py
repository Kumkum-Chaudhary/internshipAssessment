import yfinance as yf
import requests
import pandas as pd
from datetime import datetime, timedelta

companies = {
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "Wipro": "WIPRO.NS",
    "HCLTech": "HCLTECH.NS"
}

end_date = datetime.today()
start_date = end_date - timedelta(days=30)

stock_data = {}
for name, ticker in companies.items():
    df = yf.download(ticker, start=start_date, end=end_date)
    df['Company'] = name
    stock_data[name] = df

all_stocks = pd.concat(stock_data.values())
all_stocks.reset_index(inplace=True)
all_stocks.to_csv("data/it_company_stocks.csv", index=False)

currency_url = f"http://apilayer.net/api/live?access_key=29e79088b665108fe1bf7040c1b78572&currencies=INR&source=USD&format=1"
response = requests.get(currency_url)
currency_json = response.json()

print("Currency API Response:", currency_json)

if "success" in currency_json and currency_json["success"]:
    current_rate = currency_json["quotes"]["USDINR"]
    currency_df = pd.DataFrame([{
        "Date": datetime.today().date(),
        "USD_INR": current_rate
    }])

    currency_df.to_csv("data/currency_exchange_rates.csv", index=False)
    print("Currency data saved successfully.")
else:
    print("Error fetching currency data:", currency_json.get("error", {}).get("info"))
