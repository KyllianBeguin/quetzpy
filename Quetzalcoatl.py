import modules.tweeter_connection as connect
import modules.data_cleaning as data_cleaning
import modules.data_mining as data_mining
import modules.data_stats as data_stats


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
    
    def extract_tweets(self, lang = ""):
        """
        Use tweeter_connection module to :\n
        * Connect to Tweeter REST API\n
        * Run the query\n
        * Split the dataset between the RT tweets and the non-RT ones
        """
        twitter_api = connect.connect_twitter(self.token)
        _data = connect.query_tweeter(twitter_api = twitter_api, topic = self.topic, lang = lang)

        self._data = _data
        return
    
    def tweet_cleaner(self):
        """
        Clean text from tweet
        """
        # self._data = data_cleaning.remove_duplicates(self) #PB02
        for item in self._data:
            self._data[item]['text_cleaned'] = data_cleaning.hashtags_remover(self._data[item]['text'].lower())
            self._data[item]['text_cleaned'] = data_cleaning.mentions_remover(self._data[item]['text_cleaned'])
            self._data[item]['text_cleaned'] = data_cleaning.websites_remover(self._data[item]['text_cleaned'])

        return

    def tweet_miner(self):
        """
        Extract data from tweet
        """

        for item in self._data:
            self._data[item]['hashtags'] = data_mining.hashtag_extractor(self._data[item]['text'].lower())
            self._data[item]['mentions'] = data_mining.mention_extractor(self._data[item]['text'].lower())

        self.sub_topics = data_mining.sub_topics_extractor([self._data[key]['text_cleaned'] for key, val in self._data.items()])
        self.emojies = data_mining.emojies_extractor([self._data[key]['text_cleaned'] for key, val in self._data.items()])

        return

    def tweets_stats(self, stat_name = "all", param = []):
        """
        Compute statistics for the extracted tweets
        """
        stats_menu = {
            "track words": data_stats.track_words,
            "show occurrence": data_stats.show_occurrence,
            "all": data_stats.track_all
            }

        import inspect

        if "param" in inspect.signature(stats_menu[stat_name]).parameters:
            self._result = stats_menu[stat_name](self, param)
        else:
            self._result = stats_menu[stat_name]()

        return