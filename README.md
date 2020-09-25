# Sentiment Analysis on Twitter

Twitter is a growing platform with more than 321 million active users, sending a daily average of 500 million tweets. Twitter allows businesses to reach a broad audience and connect with customers without any intermediaries. Our project aims to classify these tweets into various categories which will provide feedback to businesses about their product. Sentiment analysis which is also known as _opinion mining_, is the automated process of analyzing text data and sorting it into **sentiments**: positive, negative, or neutral. Using sentiment analysis tools to analyze twitter data can help companies better understand the public opinion of their brand.

## Group Members:
    18075005 Adarsh Agrawal  
    18075021 Harirai Mahajan  
    18075024 Ishan Gupta  
    18075044 Prakhar Dwivedi  
    
## Approach 
- Scrap tweets of the required handle/hashtag using API.
- Data preprocessing: Cleaning and dumping the collected data in a file.
- Train a model on labelled data
- Use different algorithms to perform supervised learning
- Hyperparameter tuning using Validation dataset
- Testing the model on new tweets (Test dataset)

## Work done till now    
- `gettweets.py` Scrap Tweets corresponding to the user query, filter undesired tweets and dump the data in a file.
- `cleanup.py` Load the scrapped tweets and preprocess them to remove urls, handles and unnecessary characters.
- `test.py` Test the progress till now.
