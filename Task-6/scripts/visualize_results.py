import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/historical_prices.csv")
df["Next_Close"] = df["Close"].shift(-1)
df.dropna(inplace=True)

X = df[["Close"]]
y = df["Next_Close"]

_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = joblib.load("scripts/stock_model.joblib")
predictions = model.predict(X_test)

plt.figure(figsize=(10, 5))
plt.plot(y_test.values, label="Actual", linewidth=2)
plt.plot(predictions, label="Predicted", linestyle="--")
plt.title("Actual vs. Predicted Stock Prices")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.show()
