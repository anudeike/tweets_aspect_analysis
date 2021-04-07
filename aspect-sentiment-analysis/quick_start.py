"""
This a quick and well commented example of the aspect-sentiment-analysis package.
"""

import aspect_based_sentiment_analysis as absa

# this loads the default model/classifier for sentiment analysis
nlp = absa.load()

# this is interesting
text = ("We are great fans of Slack, but we wish the subscriptions "
        "were more accessible to small startups.")

# slack, price
slack, price = nlp(text, aspects=['slack', 'price'])

assert price.sentiment == absa.Sentiment.negative
assert slack.sentiment == absa.Sentiment.positive