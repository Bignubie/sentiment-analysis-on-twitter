import pickle
import re

tweets = pickle.load(open("tweetdump","rb"))
#tweets.append("RT dndsdgi 12212 sfashHHj http://sfsf.com.s.s./s/s.apsx @cat")
print(tweets)

def tweet_cleaner(text):
    #remove @mentions, RT symbols, urls, extra chars, convert to lowercase and strip
    noRT = re.sub(r'^[RT]+','',text)
    nomention = re.sub(r'@[A-Za-z0-9_:]+','',noRT)
    nourl = re.sub(r'(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*','',nomention)
    alphanum_only = re.sub(r'[^a-zA-Z0-9 ]+', '',nourl)
    stripped = alphanum_only.lower().strip()
    return stripped

ctweets = []
for tweet in tweets:
    ctweet = tweet_cleaner(tweet)
    if len(ctweet)>5:
         ctweets.append(ctweet)
print(len(ctweets))
print(ctweets)
