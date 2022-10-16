
import tweepy as tw

def connect_twitter(bearer_token):
    """
    Connect to tweeter
    """
    twitter_api = tw.Client(bearer_token=bearer_token)
    
    return twitter_api

def query_tweeter(twitter_api, topic, lang = ""):
    """
    Extract 100 tweets on the topic\n
    """
    # Extract the list of tweets
    try :
        search = twitter_api.search_recent_tweets(query=f"{topic} lang:{lang} -is:retweet", 
            tweet_fields = ['author_id','created_at','text','source','lang'],
            user_fields = ['name','username','location','verified']
            )
    except:
        search = twitter_api.search_recent_tweets(query=f"{topic} -is:retweet", 
            tweet_fields = ['author_id','created_at','text','source','lang'],
            user_fields = ['name','username','location','verified']
            )

    _data = {"item_" + str(i): search.data[i].data for i in range(len(search.data))}
    
    return _data