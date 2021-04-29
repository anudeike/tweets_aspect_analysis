# How to Use the Tweet Analyzer to Analyze Sentiment of Tweets
This account classifer is meant for running on a dataset of tweets with known author types. 
## Requirements
* XGBoost Model
* Classification bank: A csv list that looks like this:

|  id|classification  |
|--|--|
|  example_screen_username|0  |
* A config.json file (will be explained below)
* A table of preproccessed data

## Setup
### Installing the relevant libraries
You should be able to install the relevant libraries pretty easily with the `requirements.txt` file that will be provided but the list of libraries that are needed are listed below.
* botometer~=1.6  
* pandas~=1.2.3  
* numpy~=1.18.3  
* click~=7.1.2  
* python-dotenv~=0.14.0

### Getting the correct files
The example files should be stored in the directory with the main python files but double check that all the files that were stated above are present in the home directory.

### Having a .env file
This project requires the use of a dotenv file. This is both for security and ease of use purposes. The homedirectory should already include an example, but if you don't have one, you should create one with the following format:
```
TWITTER_API_KEY=WG6dfDuyqgxQsbm2XkSCKzzuE  
TWITTER_API_SECRET=os1fTHci5JSdfg1BWA98d1YrInvWG9fTc9eCOrZ2x9T7HgoVCV  
TWITTER_ACCESS_TOKEN=1161101984688218113-OToVZdmMMV9euRKitHYAWhvS2A59kS  
TWITTER_ACCESS_SECRET=wpwTBRYDcNhYHK0RALDL9LbWAPuBjf4HDwShosRpSOmvn  
RAPID_FIRE_KEY=93e5b6e789msh21f8c0a25171494p1d5236jsnd91e3eb8aa6b
```
**Note**: You will need access to your keys from rapidapi.com and twitter.com for this project. 

## Running the file
### Making sure your config file is set up
The `config.json` is the file that you pass into the command line in order to be able to use the functions in `analyze.py`. It should look something like this:
```
{  
  "tweet_data_path": "example_twitter_data_file.csv",  
  "model_file_path": "XGB_Default_Classifier.dat",  
  "database_file_path": "example.db",  
  "classification_bank_path": "classification_bank.csv",  
  "count": 0,  
  "start_index": 0,  
  "human_only": true  
}
```
* tweet_data_path: This should be the path to the prepared tweet dataset
* model_file_path: Path to the XGBoost Model
* database_file_path: Path to the sql database used to save the information
* classification_bank_path: Path to a bank of pre-classified users
* count: Amount of tweets to analyze
* start_index: What row in the tweet dataset to start at
* human_only (**Warning** not fully tested): Only analyze tweets by humans

### Command to Run the file
You should be able to run the file with the command:
`py analyze.py config.json`

Here's a quick example of what your output might look like:
```
2021-04-13 01:06:31.523647: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
2021-04-13 01:06:31.533429: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
2021-04-13 01:06:44.295588: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'nvcuda.dll'; dlerror: nvcuda.dll not found
2021-04-13 01:06:44.302965: E tensorflow/stream_executor/cuda/cuda_driver.cc:313] failed call to cuInit: UNKNOWN ERROR (303)
2021-04-13 01:06:44.313538: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: DESKTOP-LFUOOM7
2021-04-13 01:06:44.322722: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: DESKTOP-LFUOOM7
2021-04-13 01:06:44.334967: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
2021-04-13 01:06:44.380813: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x171747da1f0 initialized for platform Host (this does not guarantee that XLA will be used). Devic
es:
2021-04-13 01:06:44.388587: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
Received: ('example_twitter_data_file.csv', 'XGB_Default_Classifier.dat', 'example.db')
sys:1: DtypeWarning: Columns (1) have mixed types.Specify dtype option on import or set low_memory=False.
Reading all available rows...
(0):
MorganEilish fetched from classification bank.
(0): Prediction for MorganEilish: 1
Sentiment Analysis Result: [{'vaccine_scores': [0.7618547, 0.21436433, 0.023780933], 'vaccine_overall_sent': <Sentiment.neutral: 0>}, {'virus_scores': [0.7132395, 0.084173776, 0.20258673],
 'virus_overall_sent': <Sentiment.neutral: 0>}, {'vaccines_scores': [0.3490187, 0.63623023, 0.014751054], 'vaccines_overall_sent': <Sentiment.negative: 1>}, {'vaccination_scores': [0.58906
645, 0.39385727, 0.01707632], 'vaccination_overall_sent': <Sentiment.neutral: 0>}]
Processed tweet # 0
C:\Users\Ikechukwu Anude\PycharmProjects\aspect_tweet_processing\venv\lib\site-packages\pandas\core\generic.py:2779: UserWarning: The spaces in these column names will not be changed. In p
andas versions < 0.14, spaces were converted to underscores.
  sql.to_sql(
(1):
OliverNope fetched from classification bank.
(1): Prediction for OliverNope: 1
Sentiment Analysis Result: [{'vaccine_scores': [0.6328869, 0.35139006, 0.015723072], 'vaccine_overall_sent': <Sentiment.neutral: 0>}, {'virus_scores': [0.43320942, 0.4734329, 0.0933577], '
virus_overall_sent': <Sentiment.negative: 1>}, {'vaccines_scores': [0.49292278, 0.49308687, 0.013990367], 'vaccines_overall_sent': <Sentiment.negative: 1>}, {'vaccination_scores': [0.70842
54, 0.28429058, 0.0072840042], 'vaccination_overall_sent': <Sentiment.neutral: 0>}]
Processed tweet # 1
(2):
super_mario_21 fetched from classification bank.
(2): Prediction for super_mario_21: 1
Sentiment Analysis Result: [{'vaccine_scores': [0.6023475, 0.01725877, 0.3803937], 'vaccine_overall_sent': <Sentiment.neutral: 0>}, {'virus_scores': [0.6356933, 0.1612814, 0.20302531], 'vi
rus_overall_sent': <Sentiment.neutral: 0>}, {'vaccines_scores': [0.71155626, 0.034605674, 0.25383806], 'vaccines_overall_sent': <Sentiment.neutral: 0>}, {'vaccination_scores': [0.8719411,
0.015240982, 0.11281793], 'vaccination_overall_sent': <Sentiment.neutral: 0>}]
Processed tweet # 2