import aspect_based_sentiment_analysis as absa
import pandas as pd


# this loads the default model/classifier for sentiment analysis
nlp = absa.load()

sentiment_data = []
def calculate_sentiment(row):
    # get the tweet
    tweet = row["proccessed_tweet"]

    # get the sentiment on the tweet
    vaccine, vaccines, vaccination = nlp(tweet, aspects=["vaccine", "vaccines", "vaccination"])


    # print
    # add to the sentiment data
    data = {
        'tweet': tweet,
        'vaccine_neutral': vaccine.scores[0],
        'vaccine_negative': vaccine.scores[1],
        'vaccine_positive': vaccine.scores[2],
        # skip regular polarity and go to total
        'vaccine_negative_neutral_ratio': vaccine.scores[1]/vaccine.scores[0], # negative polarity
        'vaccine_positive_neutral_ratio': vaccine.scores[2] / vaccine.scores[0], # positive polarity
        'vaccine_negative_positive_ratio': vaccine.scores[1]/vaccine.scores[2], # total negative polarity
        'vaccine_positive_negative_ratio': vaccine.scores[2] / vaccine.scores[1], # total postiive polarity


        'vaccines_neutral': vaccines.scores[0],
        'vaccines_negative': vaccines.scores[1],
        'vaccines_positive': vaccines.scores[2],

        'vaccines_negative_neutral_ratio': vaccines.scores[1] / vaccines.scores[0],
        'vaccines_positive_neutral_ratio': vaccines.scores[2] / vaccines.scores[0],
        'vaccines_negative_positive_ratio': vaccines.scores[1] / vaccines.scores[2],
        'vaccines_positive_negative_ratio': vaccines.scores[2] / vaccines.scores[1],


        'vaccination_neutral': vaccination.scores[0],
        'vaccination_negative': vaccination.scores[1],
        'vaccination_positive': vaccination.scores[2],
        'vaccination_negative_neutral_ratio': vaccination.scores[1] / vaccination.scores[0],
        'vaccination_positive_neutral_ratio': vaccination.scores[2] / vaccination.scores[0],
        'vaccination_negative_positive_ratio': vaccination.scores[1] / vaccination.scores[2],
        'vaccination_positive_negative_ratio': vaccination.scores[2] / vaccination.scores[1]
    }

    # append
    sentiment_data.append(data)

    print(f'Sentiment (vaccine) for tweet: %-{tweet}\n{vaccine.scores}')


def main():



    path = "vaccination_only_dataset.csv"

    # load the csv
    df = pd.read_csv(path)

    # calculate sentiment for each row
    df.apply(calculate_sentiment, axis=1)

    # convert to dataframe and export
    sent_df = pd.DataFrame(sentiment_data)

    # send
    sent_df.to_csv('vaccination_only/vaccination_only_dataset.csv')




if __name__ == "__main__":
    main()