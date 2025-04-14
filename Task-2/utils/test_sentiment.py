import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from analyze_sentiment import analyze_sentiment

import pandas as pd
from analyze_sentiment import analyze_sentiment

# Sample data for testing
data = {
    "Tweet": [
        "I love this product!",
        "This is the worst experience ever.",
        "It's okay, not great, not terrible.",
        "i am felling bad ",
        "its okay"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Analyze sentiments
result_df = analyze_sentiment(df)

# Show result
print(result_df)
