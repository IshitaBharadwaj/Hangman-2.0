import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("ZibErTrMcmCxpsiddAZODNhfh", 
    "JdNlW1rvswHU7hfJffyB9gnDTeDSBjAmTiFh9Ub4XKGgyyHPy1")
auth.set_access_token("1363842412842426368-a6hh1U1Zb6zWcKsjT45Lsqx2AA7UlN", 
    "XrTxAtCi3OVxLCoe9Q6FUttN0OTTagk3Jvn3giCqRQ9ZI")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

    
    
    import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("1363842412842426368-1xEL8FdwFLH9i2VWPfNK8Kh6KETKKd", "z9UjdHZYwY9v2KulRCvNiMJpomOgx5Y8fYuC2FkcI7kVG")
auth.set_access_token("99mfrwuLuJErs7AUuM4dL2WhD", "ReA1R2GOMCM1vcKOOgGKrA2s7x89PwotsN0lUZ1BgQgNaHfEfR")

# Create API object
api = tweepy.API(auth)
 
# Create a tweet
api.update_status("Hello Tweepy")
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}") #most recent tweets by which user
api.update_status("Test tweet from Tweepy Python") #create tweet
