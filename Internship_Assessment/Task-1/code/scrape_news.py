import pandas as pd
import feedparser
import os

def scrape_from_google_news():
    query = "tech deals India"
    rss_url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}&hl=en-IN&gl=IN&ceid=IN:en"

    feed = feedparser.parse(rss_url)
    data = []

    for entry in feed.entries:
        data.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })

    news_df = pd.DataFrame(data)

    os.makedirs("data", exist_ok=True)
    news_df.to_csv("data/news_raw.csv", index=False)
    print("✅ Scraped and saved to data/news_raw.csv")

if __name__ == "__main__":
    scrape_from_google_news()
