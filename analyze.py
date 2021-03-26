# import the necessary packages
from AccountClassifer import AccountClassifierAnalyzer
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
import sqlite3
#import aspect_based_sentiment_analysis as absa

load_dotenv()
#nlp = absa.load()

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

def get_rows_in_csv(file_path, num_rows, start_index, skip_error_lines=True):
    """
    Returns a dataframe of the selected rows
    :param file_path: path to the csv file
    :param num_rows: number of rows to read from
    :param start_index: starting index
    :param skip_error_lines: If this is False, then lines that cause errors will be dropped.
    :return: dictionary
    """

    # df = pd.read_csv(file_path)
    # print(df)
    # exit(9)
    # make sure to only read info within the desired range
    def skip_function(ind):

        # if the count is zero then just return true
        if num_rows == 0 or start_index == 0:
            return False

        if start_index + num_rows > ind > start_index:
            return True

        return False

    df = pd.read_csv(file_path, skiprows=lambda x: skip_function(x), error_bad_lines=skip_error_lines)

    # turn it into a dictionary for easier processing
    df_dicts = df.to_dict(orient='records')

    return df_dicts

def run_analyzer(preprocessed_tweet_data_file_path, model_path, database_path, count=0, start_index=0):

    print(f'Received: {preprocessed_tweet_data_file_path, model_path, database_path}')


    # get the keys and tokens from an env file
    rapid_api_token, twitter_app_auth_tokens = get_tokens_from_env()

    # get an object to do the classification
    # this contains the botometer object
    account_classifier = AccountClassifierAnalyzer(rapid_api_token,
                                                   twitter_app_auth_tokens,
                                                   model_path=model_path)

    # get the rows that were targeted
    rows = get_rows_in_csv(preprocessed_tweet_data_file_path,
                         num_rows=count,
                         start_index=start_index)

    print(rows)


