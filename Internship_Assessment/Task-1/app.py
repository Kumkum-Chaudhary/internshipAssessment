import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📰 Tech Deal News Summarizer", layout="wide")
st.title("Tech Deal News Summarizer")

summary_path = "code/data/news_summary.csv"

if not os.path.exists(summary_path):
    st.warning("⚠️ Summary file not found. Please run summarize.py first.")
else:
    df = pd.read_csv(summary_path)

    if df.empty:
        st.error("❌ The summary file is empty. Please check the summarization script.")
    else:
        with st.sidebar:
            st.header("🔍 Filter Options")

            keyword = st.text_input("Search by keyword")
            if keyword:
                df = df[df['title'].str.contains(keyword, case=False) | df['summary'].str.contains(keyword, case=False)]

            st.markdown("---")
            st.subheader("📅 Filter by Date")
            df['published'] = pd.to_datetime(df['published'])
            min_date = df['published'].min().date()
            max_date = df['published'].max().date()
            date_range = st.date_input("Select range", [min_date, max_date])

            if len(date_range) == 2:
                start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
                df = df[(df['published'] >= start) & (df['published'] <= end)]

        st.success(f"✅ Found {len(df)} summarized article(s)")

        for idx, row in df.iterrows():
            with st.expander(f"📰 {row['title']}", expanded=False):
                st.write(f"🗓️ Published on: {row['published']}")
                st.markdown(f"📝 **Summary:** {row['summary']}")

        if df.empty:
            st.warning("😕 No articles match the filters. Try adjusting the search or date range.")
