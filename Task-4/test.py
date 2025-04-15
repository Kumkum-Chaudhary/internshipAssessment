from scraper import scrape_cnbc

headlines, links, dates = scrape_cnbc()

print("Headlines:", headlines)
print("Links:", links)
print("Dates:", dates)
