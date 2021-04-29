import pandas as pd

df = pd.read_csv("example_twitter_data_file.csv")

df.describe().to_csv("example_summary_stats.csv")
#print(df.describe())