from fetch_tweets import fetch_tweets

df = fetch_tweets("elon", max_results=10)
print(df)
