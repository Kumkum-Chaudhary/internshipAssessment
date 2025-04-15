import feedparser
import pandas as pd
from datetime import datetime

def scrape_yahoo_finance_rss():
    url = "https://finance.yahoo.com/rss/"
    feed = feedparser.parse(url)

    headlines = []
    links = []
    dates = []

    for entry in feed.entries:
        headlines.append(entry.title)
        links.append(entry.link)
        dates.append(entry.published)

    return headlines, links, dates

def save_to_csv():
    headlines, links, dates = scrape_yahoo_finance_rss()

    if headlines:
        data = pd.DataFrame({
            'Headline': headlines,
            'Link': links,
            'Publication Date': dates
        })
        data.to_csv('financial_updates.csv', index=False)
        print("Data saved to 'financial_updates.csv'.")
    else:
        print("No data to save.")

save_to_csv()
