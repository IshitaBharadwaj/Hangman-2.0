import tweepy

# Authenticate to Twitter
#auth = tweepy.OAuthHandler(#fill this)
#auth.set_access_token(#fill this)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

    
    
    import tweepy

# Authenticate to Twitter
#auth = tweepy.OAuthHandler(#fill this)
#auth.set_access_token(#fill this)

# Create API object
api = tweepy.API(auth)
 
# Create a tweet
api.update_status("Hello Tweepy")
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}") #most recent tweets by which user
api.update_status("Test tweet from Tweepy Python") #create tweet
