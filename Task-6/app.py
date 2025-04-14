import streamlit as st
import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Forecasting", layout="wide")
st.title("📈 Simple Stock Movement Forecaster")

symbol = st.text_input("Enter IT stock symbol (e.g., TCS.NS, INFY.NS, ^CNXIT)", value="^CNXIT")
start_date = st.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2024-12-31"))

if st.button("Run Forecast"):
    data = yf.download(symbol, start=start_date, end=end_date)
    
    if data.empty:
        st.error("No data found for the selected stock or dates.")
    else:
        data["Next_Close"] = data["Close"].shift(-1)
        data.dropna(inplace=True)

        X = data[["Close"]]
        y = data["Next_Close"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        st.subheader("📊 Model Performance")
        st.metric("Mean Squared Error", f"{mse:.2f}")
        st.metric("R² Score", f"{r2:.4f}")

        st.subheader("📉 Actual vs. Predicted Plot")
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(y_test.values, label="Actual", linewidth=2)
        ax.plot(predictions, label="Predicted", linestyle="--")
        ax.set_title("Stock Price Prediction")
        ax.set_xlabel("Time")
        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)
