import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="IT Sector Dashboard", page_icon="📊")

stock_data_path = "data/it_company_stocks.csv"
df_stock = pd.read_csv(stock_data_path)

company_map = {
    "TCS": "Close",
    "Infosys": "Close.1",
    "Wipro": "Close.2",
    "HCLTech": "Close.3"
}

st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>📈 Financial Dashboard for IT Sector</h1>
    <hr style='margin-top: -10px;'>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='color: #555;'>Visualize the stock performance of top Indian IT companies. Select a company from the dropdown below to view historical trends.</h4>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    selected_company = st.selectbox("🔍 Select Company", list(company_map.keys()), index=0)

if selected_company:
    selected_col = company_map[selected_company]
    df_plot = df_stock[["Date", selected_col]].dropna()
    df_plot["Date"] = pd.to_datetime(df_plot["Date"])

    st.markdown(f"<h3 style='color: #4CAF50;'>📊 {selected_company} Stock Performance</h3>", unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df_plot["Date"], df_plot[selected_col], color='#4CAF50', linewidth=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (INR)")
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_facecolor("#f9f9f9")
    st.pyplot(fig)
