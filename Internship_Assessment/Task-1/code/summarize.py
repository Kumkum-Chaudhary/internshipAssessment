from transformers import pipeline
import pandas as pd
import os

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

raw_path = "data/news_raw.csv"
if not os.path.exists(raw_path):
    print("❌ news_raw.csv not found. Please run scrape_news.py first.")
    exit()

raw_df = pd.read_csv(raw_path)
summaries = []

for title in raw_df["title"]:
    if len(title.split()) < 10:
        summary = title  
    else:
        try:
            summary = summarizer(title, max_length=40, min_length=10, do_sample=False)[0]['summary_text']
        except Exception as e:
            summary = "Summary generation failed"
    summaries.append(summary)

summary_df = pd.DataFrame({
    "title": raw_df["title"],
    "published": raw_df["published"],
    "summary": summaries
})

os.makedirs("data", exist_ok=True)
summary_df.to_csv("data/news_summary.csv", index=False)
print("✅ Summarization complete. Saved to data/news_summary.csv")
