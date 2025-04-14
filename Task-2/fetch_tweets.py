
import tweepy
import pandas as pd

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAA7v0QEAAAAAkCjPUrMzddHiYVV5A3XclIp5PYQ%3Dmu6XaGwhBpwz43JsiZqQrQjmXQW44DAPraWbNe6XYlTy6G2oGI"

def fetch_tweets(keyword, max_results=20):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)

    try:
        response = client.search_recent_tweets(
            query=keyword,
            tweet_fields=["created_at", "text", "author_id", "lang"],
            max_results=max_results
        )

        tweets = []
        if response.data:
            for tweet in response.data:
                tweets.append([tweet.created_at, tweet.author_id, tweet.text])

        df = pd.DataFrame(tweets, columns=["Date", "Author", "Tweet"])
        return df

    except tweepy.TooManyRequests:
        return "rate_limit_exceeded"
    except Exception as e:
        return f"Error: {e}"
