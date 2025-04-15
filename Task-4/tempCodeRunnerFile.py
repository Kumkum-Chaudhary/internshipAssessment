
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_cnbc():
    url = "https://www.cnbc.com"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return [], [], []
    
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    links = []
    dates = []

    for article in soup.find_all('article'):
        headline = article.find('a')
        if headline:
            headlines.append(headline.text.strip())
            links.append("https://www.cnbc.com" + headline['href'])
            pub_date = article.find('time')
            if pub_date and pub_date.get('datetime'):
                dates.append(pub_date['datetime'])
            else:
                dates.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    return headlines, links, dates

def save_to_csv():
    headlines, links, dates = scrape_cnbc()
    
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
