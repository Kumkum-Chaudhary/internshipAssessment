import streamlit as st
from fetch_tweets import fetch_tweets
from analyze_sentiment import analyze_sentiment
import matplotlib.pyplot as plt
import pandas as pd
import time

st.set_page_config(page_title="Twitter Sentiment Analyzer", layout="wide")
st.title("📊 Twitter Sentiment Analyzer")

# Store last run time to control rate
if "last_click_time" not in st.session_state:
    st.session_state.last_click_time = 0

keyword = st.text_input("Enter a keyword to search tweets")
max_results = st.slider("Number of tweets", 10, 100, 20)

if st.button("Analyze"):
    current_time = time.time()
    if current_time - st.session_state.last_click_time < 10:
        st.warning("⏳ Please wait a few seconds before clicking again.")
    else:
        st.session_state.last_click_time = current_time

        with st.spinner("Fetching tweets..."):
            df = fetch_tweets(keyword, max_results)

        # Handle errors before analysis
        if isinstance(df, str):
            if df == "rate_limit_exceeded":
                st.error("⚠️ Twitter API rate limit hit. Please wait 1–2 minutes.")
            else:
                st.error(f"❌ Error: {df}")
        else:
            with st.spinner("Analyzing sentiment..."):
                df = analyze_sentiment(df)

            st.success("Done!")

            st.subheader("🧾 Sample Tweets")
            st.dataframe(df)

            st.subheader("📊 Sentiment Distribution")
            st.bar_chart(df["Sentiment"].value_counts())

            st.subheader("📈 Sentiment Over Time")
            df["Date"] = pd.to_datetime(df["Date"])

            # Group by hour instead of date if same-day data
            if df["Date"].dt.date.nunique() == 1:
                df["TimeGroup"] = df["Date"].dt.strftime("%H:%M")  # group by time
            else:
                df["TimeGroup"] = df["Date"].dt.date.astype(str)  # group by day

            time_chart = df.groupby(["TimeGroup", "Sentiment"]).size().unstack().fillna(0)
            st.line_chart(time_chart)

