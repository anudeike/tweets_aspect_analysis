# import the necessary packages
import pickle
import botometer
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
import sqlite3
#import aspect_based_sentiment_analysis as absa

class AccountClassifierAnalyzer:
    def __init__(self, rapid_api_key, twitter_app_auth, model_path):

        # init the botometer module
        self.bom = botometer.Botometer(wait_on_ratelimit=True,
                                       rapid_api_key=rapid_api_key,
                                       **twitter_app_auth)

        # load the model
        self.model = self.load_model(model_path)


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