# =================================== IMPORT LIBRARIES ====================================
import src.Quetzalcoatl as Quetzalcoatl

# ========================== [DEFINE] RUN A QUETALCOATL OBJECT ===========================
def demo():
    """
    Demo time !\n
    After initializing a Quezal baby
    """
    # Invoke a Params_manager object and gic it the DEMO configuration files
    pm = Quetzalcoatl.Params_manager(name_config_extractor =  "/DEMO_configuration_extractor.json", name_config_runner = "/DEMO_configuration_runner.json",create_files = False)
    
    # Load the parameters
    pm.load_params()

    # Invoke an Extractor object
    Extractor = Quetzalcoatl.Extractor(Params_manager = pm)
    Extractor.activate_action("tweet miner")
    Extractor.set_tweets_stats("show occurrence")
    Extractor.activate_action("tweets stats")

    # Invoke a Runner object
    Runner = Quetzalcoatl.Runner(Params_manager = pm, Extractor = Extractor)

    Runner.run_extraction()

    return

# ============================ [DEFINE] RUN THE SCRAPING LOOP =============================


if __name__ == '__main__':
    demo()