import tweepy as tw

class Quetzalcoatl():
    """
    Main class\n
    - Extract tweets based on a given topic\n
    - Run the extraction for a given period of time
    """

    def __init__(self, bearer_token, topic):
        self.token = bearer_token
        self.topic = topic
        return

    def connect(self):
        auth = tw.OAuth2BearerHandler(self.token)
        api = tw.API(auth)
        self.TweeterApi = api
        return
    
    def query_tweeter(self, language = ''):
        """
        Extract 100 tweets on the topic\n
                """
        # Extract the list of tweets
        search = self.TweeterApi.search_tweets(q=self.topic, lang = language, count = 100)

        # Clean the list and return the cleaned data
        # Information to keep
        keys_keep = ["text", "retweet_count", "favorite_count", "id"]
        # For each item in search, extract and save in _data the information to keep
        _data = {"item_" + str(i): {key:search[i]._json[key] for key in search[i]._json if key in keys_keep} for i in range(len(search))}
        # For each item, update it by saving the user_id from search
        # TO DO : S'OCCUPER DE ÇA
        # _data.update({item["user_id"]: search[list(_data.keys()).index(item)]._json["user"]["id"] for item in list(_data.keys())})

        
        return _data
    
    def extract_tweets(self, language = ''):
        """
        Remove the 'RT tweets' from the set of tweets
        """
        _data = self.query_tweeter(language = language)

        keys = tuple(_data.keys())
        _data_noRT = {item:_data[item] for item in keys if 'RT' not in _data[item]['text'][0:2]}
        _data_RT = {item:_data[item] for item in keys if 'RT' in _data[item]['text'][0:2]}

        self._data = _data_noRT
        self._data_RT = _data_RT
        return