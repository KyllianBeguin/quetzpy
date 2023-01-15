# =================================== IMPORT LIBRARIES ====================================
from Quetzalcoatl.params_manager import Params_manager
from Quetzalcoatl.extractor import Extractor
from Quetzalcoatl.runner import Runner

# ========================== [DEFINE] RUN A QUETALCOATL OBJECT ===========================
def demo():
    """
    Demo time !\n
    After initializing a Quezal baby
    """
    # Invoke a Params_manager object and gic it the DEMO configuration files
    pm = Params_manager(name_config_extractor =  "/DEMO_configuration_extractor.json", name_config_runner = "/DEMO_configuration_runner.json",create_files = False)
    
    # Load the parameters
    pm.load_params()

    # Invoke an Extractor object
    extrac = Extractor(Params_manager = pm)
    extrac.activate_action("tweet miner")
    extrac.set_tweets_stats("show occurrence")
    extrac.activate_action("tweets stats")

    # Invoke a Runner object
    run = Runner(Params_manager = pm, Extractor = extrac)

    run.run_extraction()

    return

# ============================ [DEFINE] RUN THE SCRAPING LOOP =============================


if __name__ == '__main__':
    demo()