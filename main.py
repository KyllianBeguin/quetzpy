# =================================== IMPORT LIBRARIES ====================================
import src.Quetzalcoatl as Quetzalcoatl
from datetime import datetime
import time
import json

# ============================== LOAD PARAMETERS AND SECRET ===============================
# Load secret
# bearer_token = json.load(open("bearer_token.json"))["bearer_token"]
bearer_token = json.load(open("secret.json"))["bearer_token"]

# Load parameters for main function
main_setup = json.load(open("main_setup.json"))

# Store parameters in variables
nb_runs = main_setup["numbers of runs"]
sleeping_time = main_setup["sleeping time"]
words_to_catch = main_setup["words to catch"]
topics = main_setup["topics"]
lang = main_setup["lang"]

# ================================= INITIALIZE VARIABLES ==================================


# ========================== [DEFINE] RUN A QUETALCOATL OBJECT ===========================
def run_quetzalcoatl(topic_ : str, words_to_catch , lang_ = ''):
    """
    Demo time !\n
    After initializing a Quezal baby
    """
    # Initialize a Quetzal baby
    Quetzal = Quetzalcoatl.Quetzalcoatl(bearer_token, topic = topic_)

    # Extract tweets with your prefered language
    Quetzal.extract_tweets(lang=lang_)
    # Cleaning the tweets
    Quetzal.tweet_cleaner()
    # Mining the tweets
    Quetzal.tweet_miner()

    # Compute statistics
    # Test n°1 : Ask for number of times appear the following words
    Quetzal.tweets_stats(stat_name = "track words", param = words_to_catch)
    test_track_words = Quetzal._result

    # test n°2 : View the hashtags that are strongly linked to the query
    treshold_hashtags = int(100*0.30)
    Quetzal.tweets_stats(stat_name = "show occurrence", param = ["hashtags", treshold_hashtags])
    test_hashtags = Quetzal._result

    # test n°3 : Same than n°3, mentions
    treshold_mentions = int(100*0.01)
    Quetzal.tweets_stats(stat_name = "show occurrence", param = ["mentions", treshold_mentions])
    test_mentions = Quetzal._result

    # test n°4 : Extract the side topics
    sub_topics = Quetzal.sub_topics

    # test n°5 : Extract emojies occurrence
    # emojies = Quetzal.emojies

    data = {}
    data["track words"] = test_track_words
    data["show occurrence hashtags"] = test_hashtags
    data["show occurrence mentions"] = test_mentions
    data["sub topics"] = sub_topics
    # data["emojies"] = emojies

    return data

# ============================ [DEFINE] RUN THE SCRAPING LOOP =============================
def main():
    current_run_nb = 1

    while current_run_nb <= nb_runs:
        for topic_ in topics:
            data_ = run_quetzalcoatl(topic_ = topic_, words_to_catch = words_to_catch, lang_= lang)
            now_ = datetime.now()
            now_string = now_.strftime("%d/%m/%Y %H:%M:%S")
            data_json = {now_string:data_}
            try:
                with open(f"data_{now_.strftime('%d%m%Y')}_{topic_}.json", "r+") as f:
                    f_data = json.load(f)
                    f_data["data"].append(data_json)
                    f.seek(0)
                    json.dump(f_data, f, indent = 4, ensure_ascii=False)
            except FileNotFoundError:
                with open(f"data_{now_.strftime('%d%m%Y')}_{topic_}.json", "w") as f:
                    json.dump(data_json, f, indent = 4, ensure_ascii=False)
        
        if nb_runs != current_run_nb:
            print(f"Data extraction n°{current_run_nb} done")
            time.sleep(sleeping_time)
            current_run_nb += 1

    return

if __name__ == '__main__':
    main()