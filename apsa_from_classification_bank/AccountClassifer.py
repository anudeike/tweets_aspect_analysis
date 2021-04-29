# import the necessary packages
import pickle
import botometer
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
import sqlite3


class AccountClassifierAnalyzer:
    def __init__(self, rapid_api_key, twitter_app_auth, model_path, database_path, nlp, path_to_classification_bank=None, human_only=True):

        # init the botometer module
        self.tweet_index = 0

        self.nlp = nlp

        self.bom = botometer.Botometer(wait_on_ratelimit=True,
                                       rapid_api_key=rapid_api_key,
                                       **twitter_app_auth)

        # load the model
        self.model = self.load_model(model_path)

        # load the bank - only if it exists
        if path_to_classification_bank and len(path_to_classification_bank) > 0:
            self.classification_bank = pd.read_csv(path_to_classification_bank)


        # get the database connection
        self.database_connection = sqlite3.connect(database_path)

        # setting human only
        self.human_only = human_only


    def load_model(self, path):
        """
        Loads the model from a certain path.
        :param path: Path to model created by pkl
        :return: Model
        """

        try:
            pl = pickle.load(open(path, 'rb'))
            return pl
        except Exception as e:
            print(f'ERROR: {repr(e)}')

    def fetch_from_classification_bank(self, username):

        if self.classification_bank is None:
            raise FileNotFoundError("Classification bank was not found. Please include a path to a classification bank.")

        df = self.classification_bank

        # search
        res = df.loc[df['id'] == username]

        if res.empty:
            print(f'({self.tweet_index}): \n{username} could not be found in database.')
            return None

        pred = res.values

        print(f'({self.tweet_index}): \n{username} fetched from classification bank.')

        return pred[0][1]

    def get_sentiment(self, text):
        # get the sentiment in all of the target words

        vaccine, virus, vaccines, vaccination = self.nlp(text, aspects=["vaccine", "virus", "vaccines", "vaccination"])

        return [{
            "vaccine_scores": vaccine.scores,
            "vaccine_overall_sent": vaccine.sentiment
        }, {
            "virus_scores": virus.scores,
            "virus_overall_sent": virus.sentiment
        }, {
            "vaccines_scores": vaccines.scores,
            "vaccines_overall_sent": vaccines.sentiment
        }, {
            "vaccination_scores": vaccination.scores,
            "vaccination_overall_sent": vaccination.sentiment
        }]

    def run(self, row):

        try:

            # turn into dictionary
            #row = row.to_dict(orient='records')
            # classify the account
            # this fetches from the classification bank
            screen_name = row['User ID']

            # the fetched classification
            fetched = self.fetch_from_classification_bank(screen_name)

            if fetched is None:

                # for now we just skip if it is not in the classification bank
                print(f'({self.tweet_index}): Since {screen_name} was not found in the classification bank, it will be skipped.\n\n')
                self.tweet_index += 1
            else:
                # if it is in the bank
                print(f'({self.tweet_index}): Prediction for {screen_name}: {fetched}')

                # if non-human
                if int(fetched) == 0 and self.human_only == True:
                    # not counting non humans
                    print(
                        f'({self.tweet_index}): {screen_name} has been classified as a non-human and therefore will not be counted in the final analysis.')
                    self.tweet_index += 1
                    return None

                else:
                    row["prediction"] = fetched # should only be humans

            processed_tweet_content = row["proccessed_tweet"]


            mod_sentnece = " ".join(["vaccines" if "vaccin" in word else word for word in processed_tweet_content.split()])

            # get the sentiment
            sent = self.get_sentiment(mod_sentnece)
            print(f'Sentiment Analysis Result: {sent}')

            # vaccine scores
            row["vaccine_score_neutral"] = sent[0]["vaccine_scores"][0]
            row["vaccine_score_negative"] = sent[0]["vaccine_scores"][1]
            row["vaccine_score_positive"] = sent[0]["vaccine_scores"][2]
            row["vaccine_overall_sentiment"] = sent[0]["vaccine_overall_sent"]

            # virus scores
            row["virus_scores_neutral"] = sent[1]["virus_scores"][0]
            row["virus_scores_negative"] = sent[1]["virus_scores"][1]
            row["virus_scores_positive"] = sent[1]["virus_scores"][2]
            row["virus_overall_sentiment"] = sent[1]["virus_overall_sent"]

            # vaccines scores
            row["vaccines_scores_neutral"] = sent[2]["vaccines_scores"][0]
            row["vaccines_scores_negative"] = sent[2]["vaccines_scores"][1]
            row["vaccines_scores_positive"] = sent[2]["vaccines_scores"][2]
            row["vaccines_overall_sentiment"] = sent[2]["vaccines_overall_sent"]

            # vaccination scores
            row["vaccination_scores_neutral"] = sent[3]["vaccination_scores"][0]
            row["vaccination_scores_negative"] = sent[3]["vaccination_scores"][1]
            row["vaccination_scores_positive"] = sent[3]["vaccination_scores"][2]
            row["vaccination_overall_sentiment"] = sent[3]["vaccination_overall_sent"]



            print(f'Processed tweet # {self.tweet_index}')

            # put the row into the database
            row_dict = row.to_dict()
            row = pd.DataFrame(row_dict, index=[row_dict['No.']])

            row.to_sql(name="tweet_sentiment_information", con=self.database_connection, if_exists="append", index=False)
            self.database_connection.commit()

            # increments
            self.tweet_index += 1

            return row

        except Exception as e:
            print(f"[top-level]: {repr(e)}\n")
            return None
        pass

