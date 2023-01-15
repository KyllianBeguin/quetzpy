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
