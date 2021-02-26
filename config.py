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
