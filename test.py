import tweepy
import pickle
import re

twitter_keys = {
        'consumer_key':        'Jz6tdLX58ljCP8slSdYmrVnaV',
        'consumer_secret':     'syS20YGPenEifTtcZW3l7hRsR1DchlTjby88VhiBC50SAqQY5F',
        'access_token_key':    '1309201685756035072-CsIelkaZJcOKus67op8pGw2ktm7Qbh',
        'access_token_secret': 'VJPMXViIJ1K7lrGpix2NXtfQFKvJFrr1W6BRivhQ2x4Va'
    }

# Authenticate to Twitter
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'],twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'],twitter_keys['access_token_secret'])

api = tweepy.API(auth,wait_on_rate_limit=True)

output_file = open("tweets.txt","w")

hashtag = "#pop"
cnt = 10
tweets = []


for tweet in tweepy.Cursor(api.user_timeline,id="realDonaldTrump").items(cnt):
    tweets.append(tweet.text)
    

for t in tweets:
    print(t)
    
    
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
            
print(" ")        
print("UPDATED :")
print(" ")
    
for t in ctweets:
    print(t)
