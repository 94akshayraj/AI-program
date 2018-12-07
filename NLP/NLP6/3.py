import tweepy

consumer_key = "PE12jwENPbGFtcWcZbjwQNTiX"
consumer_secret = "OcOpgWkc8PWEziqmtt0LaKyAMiEaZAuJpt0T3nPOP9LTSvLyAx"
access_token = "585332053-AlzfrOxVGSuTf4QEhFS2FLA2GcsVwLjARlivdcmB"
access_token_secret = "PQQmrUqD0dkF1qImN6mwik8qGoWIeaPXydPzcseNazXRE"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
API.me()

public_tweets = api.user_timeline("FIFAcom")
for tweet in public_tweets:
    print(tweet.text)