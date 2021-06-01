# How to Use the Tweet Analyzer to Analyze Sentiment of Tweets
This account classifer is meant for running on a dataset of tweets with known author types. 
## Requirements
* XGBoost Model
* Classification bank: A csv list that looks like this:

|  id|classification  |
|--|--|
|  example_screen_username|0  |
* A config.json file (will be explained below)
* A table of preproccessed data (an example can be found [here](https://github.com/anudeike/tweets_aspect_analysis/blob/main/apsa_from_classification_bank/example_twitter_data_file.csv), make sure that the data you decide to use exactly fits this format)

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

```

## Understanding the output
The first part of the output might look something like this:
```
2021-04-13 01:06:31.523647: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
2021-04-13 01:06:31.533429: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
2021-04-13 01:06:44.295588: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'nvcuda.dll'; dlerror: nvcuda.dll not found
2021-04-13 01:06:44.302965: E tensorflow/stream_executor/cuda/cuda_driver.cc:313] failed call to cuInit: UNKNOWN ERROR (303)
2021-04-13 01:06:44.313538: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: DESKTOP-_____
2021-04-13 01:06:44.322722: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: DESKTOP-_____
2021-04-13 01:06:44.334967: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
2021-04-13 01:06:44.380813: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x171747da1f0 initialized for platform Host (this does not guarantee that XLA will be used). Devic
es:
2021-04-13 01:06:44.388587: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
```
If you get a couple of messages like this, you can mostly disregard them. They are simply warning that have to do with how tensorflow deals with finding a backend to use.
```
Received: ('example_twitter_data_file.csv', 'XGB_Default_Classifier.dat', 'example.db')
sys:1: DtypeWarning: Columns (1) have mixed types.Specify dtype option on import or set low_memory=False.
```
This is a pandas warning. You can disregard this also. 
```
(0):
MorganEilish fetched from classification bank.
(0): Prediction for MorganEilish: 1
Sentiment Analysis Result: [{'vaccine_scores': [0.7618547, 0.21436433, 0.023780933], 'vaccine_overall_sent': <Sentiment.neutral: 0>}, {'virus_scores': [0.7132395, 0.084173776, 0.20258673],
 'virus_overall_sent': <Sentiment.neutral: 0>}, {'vaccines_scores': [0.3490187, 0.63623023, 0.014751054], 'vaccines_overall_sent': <Sentiment.negative: 1>}, {'vaccination_scores': [0.58906
645, 0.39385727, 0.01707632], 'vaccination_overall_sent': <Sentiment.neutral: 0>}]
Processed tweet # 0
```
The next couple of lines of console output should be information on the status of the package. `Sentiment Analysis Result:` displays the overall sentiment in `[neutral, negative, positive]` form for each aspect, vaccine, virus and vaccination respectively. Those score are rated from (0, 1) with 1 being the highest mangitude. The values should always add up to 1. 

This information is appended to the information from the pre-processed file and then stored in the output database. 

# Notes on Using the Package
## From the Homepage
The home page of the article should be linked above. 

On the github homepage, there's a link that reads: "[**Do You Trust in Aspect-Based Sentiment Analysis? Testing and Explaining Model Behaviors**](https://rafalrolczynski.com/2021/03/07/aspect-based-sentiment-analysis/)". It points to an article that lays out the reason for the package's existence and how effective their model is at understanding the sentiment of words (in relation to the context). I won't be able to fully summarize the entire article in this readme, but some of the important highlights include the shape of the Machine Learning Pipeline: Pre-process -> Tokenize -> Encode -> Predict -> Review -> Post-Process, and the explanation of the "professor" class.

## The Professor
The "Professor" is an additional module that seeks to provide a "sanity check" to the result of the model. It reviews the internal states, supervises the model and provides explanations of the model prediction to the end user. This allows the developers to gain insight into the decision making process of the model and uncover a bit of the mystery in the black box.

### Implementation
Implementing a "Professor" should be relatively straight forward. Just include instantiate the nlp class like so: 
```
name = 'absa/classifier-rest-0.2'
model = absa.BertABSClassifier.from_pretrained(name)
tokenizer = absa.BertTokenizer.from_pretrained(name)
professor = absa.Professor()     # Explained in detail later on.
text_splitter = absa.sentencizer()  # The English CNN model from SpaCy.
nlp = absa.Pipeline(model, tokenizer, professor, text_splitter)
```
(You shouldn't have to worry about passing in parameters)
**Note**: This (and further lines of code after this) only run in a juptyer notebook enviornment (AFAIK).

## Understanding Patterns
Before I explain what patterns are and why they are important, copy and paste this bit of code into a jupyter notebook of your choice (you can use Google Colab too)
```
import aspect_based_sentiment_analysis as absa

text = ("i wrote this in may, describing how covid-19 was now endemic in the us. my guess was 15,000 to 20,000 americans would get sick and 500 to 1,000 americans would die every day until we got an effective vaccine. i was wrong. way too optimistic.")

  

recognizer = absa.aux_models.BasicPatternRecognizer()

nlp = absa.load(pattern_recognizer=recognizer)

completed_task = nlp(text=text, aspects=['virus', 'vaccine'])

virus, vaccine = completed_task.examples

  

# so it seems like the weights match the tokens.

weights = virus.review.patterns[0].weights

tokens = virus.review.patterns[0].tokens

  

# we should zip them to get the most important tokens

print(f'Length of weights: {len(weights)}')

print(f'Length of tokens: {len(tokens)}')

  

print(virus.review.patterns)

absa.summary(virus)

absa.display(virus.review)
```
When you run this code you should get an output like this:
```
Length of weights: 58 Length of tokens: 58 [Pattern(importance=1.0, tokens=['i', 'wrote', 'this', 'in', 'may', ',', 'describing', 'how', 'covid', '-', '19', 'was', 'now', 'endemic', 'in', 'the', 'us', '.', 'my', 'guess', 'was', '15', ',', '000', 'to', '20', ',', '000', 'americans', 'would', 'get', 'sick', 'and', '500', 'to', '1', ',', '000', 'americans', 'would', 'die', 'every', 'day', 'until', 'we', 'got', 'an', 'effective', 'vaccine', '.', 'i', 'was', 'wrong', '.', 'way', 'too', 'optimistic', '.'], weights=[0.02, 0.04, 0.04, 0.02, 0.03, 0.03, 0.04, 0.03, 0.03, 0.02, 0.01, 0.02, 0.03, 0.04, 0.02, 0.02, 0.01, 0.06, 0.02, 0.05, 0.05, 0.01, 0.01, 0.03, 0.03, 0.01, 0.02, 0.05, 0.05, 0.04, 0.07, 0.06, 0.04, 0.03, 0.02, 0.01, 0.01, 0.04, 0.05, 0.03, 0.06, 0.03, 0.03, 0.06, 0.03, 0.05, 0.03, 0.09, 0.19, 0.13, 0.1, 0.16, 0.3, 0.22, 0.39, 1.0, 1.0, 0.26]), Pattern(importance=0.91, tokens=['i', 'wrote', 'this', 'in', 'may', ',', 'describing', 'how', 'covid', '-', '19', 'was', 'now', 'endemic', 'in', 'the', 'us', '.', 'my', 'guess', 'was', '15', ',', '000', 'to', '20', ',', '000', 'americans', 'would', 'get', 'sick', 'and', '500', 'to', '1', ',', '000', 'americans', 'would', 'die', 'every', 'day', 'until', 'we', 'got', 'an', 'effective', 'vaccine', '.', 'i', 'was', 'wrong', '.', 'way', 'too', 'optimistic', '.'], weights=[0.04, 0.07, 0.06, 0.04, 0.04, 0.06, 0.07, 0.06, 0.07, 0.02, 0.02, 0.02, 0.04, 0.07, 0.03, 0.05, 0.02, 0.11, 0.04, 0.45, 0.1, 0.03, 0.04, 0.07, 0.07, 0.02, 0.04, 0.08, 0.06, 0.07, 0.08, 0.07, 0.07, 0.06, 0.05, 0.03, 0.03, 0.06, 0.06, 0.05, 0.16, 0.08, 0.05, 0.1, 0.05, 0.13, 0.08, 0.16, 0.39, 0.51, 0.91, 0.6, 0.91, 0.57, 0.59, 0.73, 0.5, 0.28]), Pattern(importance=0.67, tokens=['i', 'wrote', 'this', 'in', 'may', ',', 'describing', 'how', 'covid', '-', '19', 'was', 'now', 'endemic', 'in', 'the', 'us', '.', 'my', 'guess', 'was', '15', ',', '000', 'to', '20', ',', '000', 'americans', 'would', 'get', 'sick', 'and', '500', 'to', '1', ',', '000', 'americans', 'would', 'die', 'every', 'day', 'until', 'we', 'got', 'an', 'effective', 'vaccine', '.', 'i', 'was', 'wrong', '.', 'way', 'too', 'optimistic', '.'], weights=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.03, 0.02, 0.01, 0.01, 0.01, 0.04, 0.01, 0.02, 0.01, 0.03, 0.01, 0.02, 0.01, 0.01, 0.01, 0.02, 0.01, 0.01, 0.01, 0.02, 0.02, 0.01, 0.02, 0.05, 0.02, 0.02, 0.01, 0.01, 0.01, 0.03, 0.03, 0.02, 0.07, 0.03, 0.04, 0.11, 0.06, 0.12, 0.25, 0.67, 0.67, 0.09, 0.01, 0.02, 0.06, 0.02, 0.01, 0.02, 0.04, 0.04]), Pattern(importance=0.64, tokens=['i', 'wrote', 'this', 'in', 'may', ',', 'describing', 'how', 'covid', '-', '19', 'was', 'now', 'endemic', 'in', 'the', 'us', '.', 'my', 'guess', 'was', '15', ',', '000', 'to', '20', ',', '000', 'americans', 'would', 'get', 'sick', 'and', '500', 'to', '1', ',', '000', 'americans', 'would', 'die', 'every', 'day', 'until', 'we', 'got', 'an', 'effective', 'vaccine', '.', 'i', 'was', 'wrong', '.', 'way', 'too', 'optimistic', '.'], weights=[0.01, 0.03, 0.02, 0.01, 0.01, 0.03, 0.02, 0.01, 0.09, 0.04, 0.04, 0.02, 0.02, 0.07, 0.02, 0.04, 0.03, 0.09, 0.02, 0.03, 0.03, 0.02, 0.03, 0.05, 0.02, 0.02, 0.03, 0.04, 0.07, 0.01, 0.03, 0.1, 0.03, 0.05, 0.02, 0.01, 0.03, 0.06, 0.09, 0.02, 0.08, 0.04, 0.04, 0.08, 0.07, 0.14, 0.13, 0.46, 0.64, 0.26, 0.04, 0.05, 0.07, 0.06, 0.02, 0.02, 0.07, 0.08]), Pattern(importance=0.55, tokens=['i', 'wrote', 'this', 'in', 'may', ',', 'describing', 'how', 'covid', '-', '19', 'was', 'now', 'endemic', 'in', 'the', 'us', '.', 'my', 'guess', 'was', '15', ',', '000', 'to', '20', ',', '000', 'americans', 'would', 'get', 'sick', 'and', '500', 'to', '1', ',', '000', 'americans', 'would', 'die', 'every', 'day', 'until', 'we', 'got', 'an', 'effective', 'vaccine', '.', 'i', 'was', 'wrong', '.', 'way', 'too', 'optimistic', '.'], weights=[0.01, 0.01, 0.02, 0.01, 0.01, 0.01, 0.02, 0.01, 0.01, 0.01, 0.01, 0.0, 0.01, 0.01, 0.01, 0.01, 0.0, 0.03, 0.01, 0.03, 0.01, 0.01, 0.01, 0.02, 0.01, 0.01, 0.01, 0.02, 0.01, 0.01, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.02, 0.01, 0.01, 0.02, 0.01, 0.01, 0.03, 0.01, 0.02, 0.02, 0.03, 0.03, 0.13, 0.14, 0.13, 0.14, 0.34, 0.42, 0.55, 0.55, 0.12])] Sentiment.negative for "virus" Scores (neutral/negative/positive): [0.048 0.919 0.033]
```
![picture of the output](https://res.cloudinary.com/cheezitromansh/image/upload/v1622090755/sns_i9k41f.png)

A pattern is a weighting group of tokens represented as a vector that assigns a weight to each token in the text provided. The range of the weight is (0, 1)  . This weight shows how the token relates to the pattern and consequently the decision the model has made. 

For example: At importance level 1.0 for the aspect "slack", then sentence 'we are great fans of slack.' could have the pattern vector: [0.23 0.28 0.56 1.00 0.39 1.00 0.19]. This highlights that the tokens 'slack' and 'fans' play an important role in determining the output of the model.

You can read more about this in the Pattern section of this [article].(https://rafalrolczynski.com/2021/03/07/aspect-based-sentiment-analysis/)
