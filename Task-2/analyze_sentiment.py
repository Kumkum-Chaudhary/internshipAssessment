import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(df):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []

    for tweet in df["Tweet"]:
        score = analyzer.polarity_scores(tweet)["compound"]
        if score >= 0.05:
            sentiments.append("Positive")
        elif score <= -0.05:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")

    df["Sentiment"] = sentiments
    return df

