// FILE FOR TESTING PURPOSES 
// SENTIMENTAL ANALYSIS

import tweepy
import pickle
import re

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n]: "
    elif default == "yes":
        prompt = " [Y/n]: "
    elif default == "no":
        prompt = " [y/N]: "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def tweet_cleaner(text):
    #remove @mentions, RT symbols, urls, extra chars, convert to lowercase and strip
    noRT = re.sub(r'^[RT]+','',text)
    nomention = re.sub(r'@[A-Za-z0-9_:]+','',noRT)
    nourl = re.sub('https?://[A-Za-z0-9./]+','',nomention)
    alphanum_only = re.sub(r'[^a-zA-Z0-9 ]+', '',nourl)
    stripped = alphanum_only.lower().strip()
    res = re.sub(' +', ' ', stripped)
    return res

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

query = input("Enter hashtag to search: ")
cnt = int(input("Enter number of tweets to retrieve: "))

query = "#" + query
tweets = []

for tweet in tweepy.Cursor(api.search,q=query,lang="en",tweet_mode='extended').items(cnt):
    output_file.write(tweet.full_text+'\n')
    tweets.append(tweet.full_text)
    print(tweet.full_text)

print("\n UPDATED : \n")
    
ctweets = []
for tweet in tweets:
    ctweet = tweet_cleaner(tweet)
    if len(ctweet)>5:
         ctweets.append(ctweet)
    print(ctweet)
