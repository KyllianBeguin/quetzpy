from quetzpy.params_manager import Params_manager
import quetzpy.modules.twitter_connection as connect
import quetzpy.modules.data_cleaning as data_cleaning
import quetzpy.modules.data_mining as data_mining
import quetzpy.modules.data_stats as data_stats
import quetzpy.modules.decorators as decorators

class Extractor():
    def __init__(self, Params_manager : Params_manager):
        """
        Main class\n
        - Extract tweets based on a given topic\n
        - Can extract hashtags, mentions, most dicussed topics in the tweets
        - Can track information you give it
        """
        self.params_manager = Params_manager

        self.actions_states = {
            "clean tweets" : True,
            "tweet miner" : False,
            "tweets stats" : False
        }

        self.perform_actions = {
            "extract tweets" : self.extract_tweets,
            "clean tweets" : self.tweet_cleaner,
            "tweet miner" : self.tweet_miner,
            "tweets stats" : self.tweets_stats
        }

        self.tweets_stats_param = "all"

        return

    def activate_action(self, action : str):
        """
        Switch action state to True in the self.activate_actions dict\n
        List on actions to activate :\n
        * tweet miner
        * tweet stats
        """
        if action not in self.actions_states.keys():
            raise ValueError(f"Action given is wrong. It should be from this list {list(self.activate_actions.keys())[1::]}")
        
        # Switch action to True to be performed
        self.actions_states[action] = True

        return
    
    def extract_tweets(self):
        """
        Use tweeter_connection module to :\n
        * Connect to Tweeter REST API\n
        * Run the query\n
        * Split the dataset between the RT tweets and the non-RT ones
        """
        twitter_api = connect.connect_twitter(self.params_manager.Extrac_bearer_token)
        data_topics = dict()
        for topic in self.params_manager.Extrac_topics:
            data_topics[topic] = dict()
            data_topics[topic]["tweets"] = connect.query_tweeter(twitter_api = twitter_api, topic = topic, lang = self.params_manager.Extrac_lang, max_results = self.params_manager.Extrac_max_results)

        self.data_topics = data_topics
        return
    
    def tweet_cleaner(self):
        """
        Clean text from tweet
        """

        for topic in self.params_manager.Extrac_topics:
            for item in self.data_topics[topic]["tweets"]:
                self.data_topics[topic]["tweets"][item]['text_cleaned'] = data_cleaning.hashtags_remover(self.data_topics[topic]["tweets"][item]['text'].lower())
                self.data_topics[topic]["tweets"][item]['text_cleaned'] = data_cleaning.mentions_remover(self.data_topics[topic]["tweets"][item]['text_cleaned'])
                self.data_topics[topic]["tweets"][item]['text_cleaned'] = data_cleaning.websites_remover(self.data_topics[topic]["tweets"][item]['text_cleaned'])

        return

    def tweet_miner(self):
        """
        Extract data from tweet
        """
        for topic in self.params_manager.Extrac_topics:
            for item in self.data_topics[topic]["tweets"]:
                self.data_topics[topic]["tweets"][item]['hashtags'] = data_mining.hashtag_extractor(self.data_topics[topic]["tweets"][item]['text'].lower())
                self.data_topics[topic]["tweets"][item]['mentions'] = data_mining.mention_extractor(self.data_topics[topic]["tweets"][item]['text'].lower())

            self.data_topics[topic]["sub topics"] = data_mining.sub_topics_extractor([val['text_cleaned'] for val in self.data_topics[topic]["tweets"].values()])
            self.data_topics[topic]["emojies"] = data_mining.emojies_extractor([val['text_cleaned'] for val in self.data_topics[topic]["tweets"].values()])

        return

    def set_tweets_stats(self, new_param: str):
        """
        Set the tweets stats parameter to one of the following:\n
        * track words: Track only the words mentioned in the config file\n
        * show occurence:  Show the number of times hashtags or mention appears. Default: on hashtags\n
        * all: Run track word and show occurrence\n
        By default, the parameter is set to all.
        """
        if new_param not in ["all", "track words", "show occurrence"]:
            return "New parameter should be from this list:\nall, track words, show occurrence"
        self.tweets_stats_param = new_param

    def tweets_stats(self):
        """
        Compute statistics for the extracted tweets
        """
        stats_menu = {
            "track words": data_stats.track_words,
            "show occurrence": data_stats.show_occurrence,
            "all": data_stats.track_all
            }
        for topic in self.params_manager.Extrac_topics:
            self.data_topics[topic]["stats"] = stats_menu[self.tweets_stats_param](self, self.params_manager, topic)

        return
