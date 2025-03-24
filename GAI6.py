from transformers import pipeline

# Sentiment analysis pipeline with a specified model
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# Analyze sentiment
sentence = "I love working with Python for AI development!"

result = sentiment_analyzer(sentence)

print(result)





# output = 
# Device set to use cpu
# [{'label': 'POSITIVE', 'score': 0.9976370334625244}]
# 
# 