import aspect_based_sentiment_analysis as absa

recognizer = absa.aux_models.BasicPatternRecognizer()
nlp = absa.load(pattern_recognizer=recognizer)
completed_task = nlp(text="We love slack but it is too expensive.", aspects=['slack', 'price'])
slack, price = completed_task.examples

absa.summary(slack)
absa.display(slack.review)