import pandas as pd
from transformers import pipeline

def summarize_texts(texts):
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    summaries = []
    for text in texts:
        try:
            summary = summarizer(text[:1024], max_length=50, min_length=15, do_sample=False)[0]['summary_text']
            summaries.append(summary)
        except:
            summaries.append("Summary failed")
    return summaries

def summarize_news():
    df = pd.read_csv("data/news_raw.csv")
    df = df.dropna(subset=["title"])
    df["summary"] = summarize_texts(df["title"])
    df.to_csv("data/news_summary.csv", index=False)
    print("✅ Summarized and saved to data/news_summary.csv")

if __name__ == "__main__":
    summarize_news()
