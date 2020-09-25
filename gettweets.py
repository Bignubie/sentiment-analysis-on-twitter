import tweepy

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

hashtag = input("Enter hashtag to search:")
hashtag = "#" + hashtag

cnt = int(input("Enter number of tweets to retrieve:"))

for tweet in tweepy.Cursor(api.search,q=hashtag,lang="en").items(cnt):
    output_file.write(unicode(tweet.text).encode("utf-8") + '\n')