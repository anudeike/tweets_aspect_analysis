# import the necessary packages
import click
from analyze import run_analyzer
import pandas as pd

"""
This is the command line entry point into the package.

To use this file you will need a couple of things:
1. Twitter Data in the form with the required columns (will be in the readme). This must be a csv file
2. The XGBoost Model File (should by a file made using the pickle package)
3. An env file that contains your twitter credentials and your twitter credentials

All of these will be passed into a function that will run for you.

"""

@click.command()
@click.argument('twitter_file_path', type=click.Path(exists=True))
@click.argument('model_file_path', type=click.Path(exists=True))
@click.argument("database_file_path", type=click.Path(exists=True))
@click.option('--count', '-c', default=0, help="Number of rows to analyze. Default is 0, which means that it will go through all available tweet batches.")
@click.option('--start', '-s', default=0, help="Index of the row to start counting at. Default is 0")
def analyze_tweets(twitter_file_path, model_file_path, database_file_path, count, start):

    # all we need to do now is to pass the information into the next file
    click.echo(f"Analyzing tweets...\nTwitter File Path: {twitter_file_path}\nModel File Path: {model_file_path}\nDatabase File Path: {database_file_path}\nCount: {count}\nStarting at index: {start}")

    # run the analyzer
    run_analyzer(twitter_file_path, model_file_path, database_file_path, count, start)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #df = pd.read_csv("example_twitter_data_file.csv")
    #print(df)
    analyze_tweets()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
