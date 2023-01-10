import modules.twitter_connection as connect
import src.modules.data_cleaning as data_cleaning
import src.modules.data_mining as data_mining
import src.modules.data_stats as data_stats
import src.modules.decorators as decorators

class Params_manager():

    def __init__(self, name_config_extractor = "/configuration_extractor.json", name_config_runner = "/configuration_runner.json", create_files = True) -> None:
        """
        Create and initialize `configuration_runner.json` and `extractor_configuration.json` used by the `Extractor` and the `Runner` objects\n
        :name_config_extractor: name for the extractor configuration file. Default = "/configuration_extractor.json"\n
        :name_config_runner: name for the runner configuration file. Default = "/configuration_runner.json"\n
        Invoking a Params_manager automatically creates the files
        """
        self.params_extractor = {
            "bearer token" : "MY TOKEN",
            "words to catch" : ["word 1", "word 2"],
            "topics" : ["topic 1", "topic 2"],
            "lang" : "en",
            "max results" : 10
        }

        self.params_runner = {
            "numbers of runs" : 1,
            "sleeping time (sec)" : 0
        }

        self.path = "./__config__"
        self.name_config_extractor = name_config_extractor
        self.name_config_runner = name_config_runner

        if create_files:
            self.create_files()

    def create_files(self) -> None:
        """
        Create the two files recquired by the `Extractor` class
        """

        import os
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        
        import json
        if not os.path.exists(self.path + self.name_config_extractor):        
            json.dump(self.params_extractor, open(self.path + self.name_config_extractor, "w"), indent = 4)

        if not os.path.exists(self.path + self.name_config_runner):
            json.dump(self.params_runner, open(self.path + self.name_config_runner, "w"), indent = 4)

        return

    def load_extrac_params(self) -> None:
        """
        Load parameters for `Extractor`\n
        `Extractor` parameters' names begin with `Extrac_`
        """

        import json
        path_to_config_extrac_file = self.path + self.name_config_extractor
        config_extractor = json.load(open(path_to_config_extrac_file))
        self.Extrac_bearer_token = config_extractor["bearer token"]
        self.Extrac_topics = config_extractor["topics"]
        self.Extrac_lang = config_extractor["lang"]
        self.Extrac_max_results = config_extractor["max results"]
        self.Extrac_track_words = config_extractor["stats"]["track words"]
        self.Extrac_track_words_threshold = config_extractor["stats threshold"]["track words"]
        self.Extrac_show_occurrence = config_extractor["stats"]["show occurrence"]
        self.Extrac_show_occurrence_threshold = config_extractor["stats threshold"]["show occurrence"]
        return

    def load_run_params(self) -> None:
        """
        Load parameters for `Runner`\n
        `Runner` parameters' names begin with `Run_`
        """
        import json
        path_to_runner_config_file = self.path + self.name_config_runner
        config_runner = json.load(open(path_to_runner_config_file))
        self.Run_nb_runs = config_runner["numbers of runs"]
        self.Run_sleep_time = config_runner["sleeping time (sec)"]

        return

    def load_params(self) -> None:
        self.load_extrac_params()
        self.load_run_params()

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

class Runner():
    def __init__(self, Params_manager : Params_manager, Extractor : Extractor) -> None:
        """
        Run the extraction according to the parameters
        """
        self.params_manager = Params_manager
        self.extractor = Extractor
        return

    def run_extractor_actions(self):
        """
        Run the Extractor's actions with state = True
        """

        extrac_actions_true = [action for action in self.extractor.actions_states.keys() if self.extractor.actions_states[action] == True]
        for action_to_perform in extrac_actions_true:
            self.extractor.perform_actions[action_to_perform]()

        return

    def write_output(self, directory = "./data"):
        """
        Write the output in the `./data` directory
        """
        import os
        if not os.path.exists(directory):
            os.mkdir(directory)

        from datetime import datetime
        now = datetime.now().strftime('%d%m%Y')

        for topic in self.extractor.params_manager.Extrac_topics:
            file_name = f"/data_{now}_{topic}.json"

            import json
            if not os.path.exists(directory + file_name):
                json.dump({"data" : []}, open(directory + file_name, "w"), indent = 4, ensure_ascii = False)

            with open(directory + file_name, "r+", encoding="utf-8") as f:
                f_data = json.load(f)
                f_data["data"].append(self.extractor.data_topics[topic])
                f.seek(0)
                json.dump(f_data, f, indent = 4, ensure_ascii=False)
    
        return

    def run_extraction(self):
        """
        Run the extraction according to the parameters
        """

        current_run = 0
        from time import sleep

        while current_run < self.params_manager.Run_nb_runs:
            
            self.extractor.extract_tweets()
            self.run_extractor_actions()
            self.write_output()

            current_run += 1
            if current_run == self.params_manager.Run_nb_runs:
                break

            else:
                sleep(self.params_manager.Run_sleep_time)