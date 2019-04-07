import tweepy

consumer_key = 'PxLx8oCw3JnkolEK19GHoPDnO'
consumer_secret = 'fyyvskBdaQwLoQ44QtMGbkrXVvNO95UAOiuavPA15nWRpvwXLn'
access_token = '1094958827861094400-3WdYmPzW3NLLTQsZyKoRFnH1pbu6Y6'
access_token_secret = 'vMmnoNhPGtcPJ7DDBejNIUV07aOaUkJust2uDER7AEp2L'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()


name="modi"

tweetCount = 5


results = api.user_timeline(id=name, count=tweetCount)

for tweet in results:
   
   print (tweet.text)
