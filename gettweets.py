import tweepy
import pickle
import sys

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

query = input("Enter hashtag to search: ")
query = "#" + query

cnt = int(input("Enter number of tweets to retrieve: "))
tweets = []

if not query_yes_no("Do you want to keep retweets?"):
     query = query + " -filter:retweets"

for tweet in tweepy.Cursor(api.search,q=query,lang="en",tweet_mode='extended').items(cnt):
    output_file.write(tweet.text+'\n')
    tweets.append(tweet.text)


output_file.close()
output_file = open("tweetdump","wb")
pickle.dump(tweets,output_file)

if len(tweets)!=1:
    print(str(len(tweets)) + " tweets collected!")
else:
    print(str(len(tweets)) + " tweet collected!")

