# import aspect_based_sentiment_analysis as absa
import pandas as pd
import re

"""
take 50-100 tweets (control first)
take 50-100 tweets change all the vaccine-esque words to vaccine and run that

1. Run 50-100 sentiment analyzing the tweets for the vaccine, vaccinations, and vaccine paramters
2. Create an edited version where you only get the 
"""

df = pd.read_csv("experiement/test_dataset.csv")
df = df[0:1000] # take a slice

def change_vaccine_keyword(row):
    tweet = row["proccessed_tweet"]

    # list tweet
    row["proccessed_tweet"] = " ".join(["vaccination" if "vaccin" in word else word for word in tweet.split()])

    return row


df = df.apply(change_vaccine_keyword, axis=1)


df.to_csv("vaccination_only_dataset.csv")
#print(df["proccessed_tweet"])
