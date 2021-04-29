# import the necessary packages
from AccountClassifer import AccountClassifierAnalyzer
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
import sqlite3
import sys
import json
import aspect_based_sentiment_analysis as absa

load_dotenv()
nlp = absa.load()

"""
To use this file you will need a couple of things:
1. Twitter Data in the form with the required columns (will be in the readme)
2. The XGBoost Model File (should by a file made using the pickle package)
3. An env file that contains your twitter credentials and your twitter credentials
4. 
"""


def get_tokens_from_env():
    """
    Get the tokens from the env file located in this directory
    :return: rapid_api_key, twitter_keys_object
    """
    no_env_error_message = """It doesn't seem like I can find your .env file.
    Please make sure that it is in the same directory as this file and make sure that the
    variables are labeled accord to the README."""

    if (rapid_api_key := os.getenv('RAPID_FIRE_KEY')) == None:
        # raise an error
        raise ValueError(f'{no_env_error_message}\n\nCould not find variable RAPID_FIRE_KEY.')

    if (twitter_consumer_key := os.getenv('TWITTER_API_KEY')) == None:
        # raise an error
        raise ValueError(f'{no_env_error_message}\n\nCould not find variable TWITTER_API_KEY.')

    if (twitter_consumer_secret := os.getenv('TWITTER_API_SECRET')) == None:
        # raise an error
        raise ValueError(f'{no_env_error_message}\n\nCould not find variable TWITTER_API_SECRET.')

    # if there are no errors then you can go ahead and return all the keys
    twitter_app_auth = {
        'consumer_key': twitter_consumer_key,
        'consumer_secret': twitter_consumer_secret,
    }

    return rapid_api_key, twitter_app_auth

def get_tweet_dataframe(file_path, num_rows, start_index, skip_error_lines=True):
    """
    Returns a dataframe of the selected rows
    :param file_path: path to the csv file
    :param num_rows: number of rows to read from
    :param start_index: starting index
    :param skip_error_lines: If this is False, then lines that cause errors will be dropped.
    :return: dictionary
    """

    # make sure to only read info within the desired range
    def skip_function(ind):

        # if the count is zero then just return true
        if num_rows == 0 or start_index == 0:
            return False

        if start_index + num_rows > ind > start_index:
            return True

        return False

    if num_rows != 0:
        print(f"Reading rows {start_index} through {start_index + num_rows}...")
    else:
        print("Reading all available rows...")

    # read from the csv
    # names="No.,Is retweet?,Tweet ID,Post Date,User Display Name,User ID,User Info,User Location,Tweet Content,Number of Quotes,Number of Replies,Number of Likes,Number of Retweets,Raw link 1,Solved link 1,Raw link 2,Solved link 2,Raw link 3,Solved link 3,Raw link 4,Solved link 4,Raw link 5,Solved link 5,proccessed_tweet".split(',')
    df = pd.read_csv(file_path, skiprows=lambda x: skip_function(x), error_bad_lines=skip_error_lines)

    return df


def run_analyzer(preprocessed_tweet_data_file_path, model_path, database_path, classification_bank_path, count=0, start_index=0, human_only=True):

    print(f'Received: {preprocessed_tweet_data_file_path, model_path, database_path}')

    # get the keys and tokens from an env file
    rapid_api_token, twitter_app_auth_tokens = get_tokens_from_env()

    # get an object to do the classification
    # this contains the botometer object
    account_classifier = AccountClassifierAnalyzer(rapid_api_key=rapid_api_token,
                                                   twitter_app_auth=twitter_app_auth_tokens,
                                                   model_path=model_path,
                                                   database_path=database_path,
                                                   path_to_classification_bank=classification_bank_path,
                                                   human_only=human_only,
                                                   nlp=nlp)


    # get the dataframe of all the tweets
    tweet_df = get_tweet_dataframe(file_path=preprocessed_tweet_data_file_path,
                        num_rows=count,
                        start_index=start_index)

    # turn into an array of dictionaries
    # tweets_dict_array = tweet_df.to_dict(orient='records')
    # print(tweets_dict_array)
    # exit(9)
    # use df.apply to cycle through each dataframe
    tweet_df.apply(account_classifier.run, axis=1)




if __name__ == '__main__':

    # import a json config file
    config_file = sys.argv[1]
    f = open(config_file)

    # turn into a dictionary and get all the necessary values
    config_data = json.load(f)

    # run the analyzer
    run_analyzer(preprocessed_tweet_data_file_path=config_data['tweet_data_path'],
                 classification_bank_path=config_data['classification_bank_path'],
                 model_path=config_data["model_file_path"],
                 database_path=config_data["database_file_path"],
                 count=config_data["count"],
                 start_index=config_data["start_index"],
                 human_only=config_data["human_only"])

