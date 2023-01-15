from Quetzalcoatl.params_manager import Params_manager
from Quetzalcoatl.extractor import Extractor

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