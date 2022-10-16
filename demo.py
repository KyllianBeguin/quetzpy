import Quetzalcoatl
import json

# STEP 1 : LOAD YOUR TOKEN -------------------------------------------------------------------------

# bearer_token = json.load(open("bearer_token.json"))["bearer_token"]
bearer_token = json.load(open("secret.json"))["bearer_token"]


# STEP 2 : RUN THE EXTRACTION / MINING / CLEANING --------------------------------------------------
# Initialize a Quetzal baby
Quetzal = Quetzalcoatl.Quetzalcoatl(bearer_token, topic = "#MarcheContreLaVieChere")
# Extract tweets wiith your prefered language
Quetzal.extract_tweets(lang='')
# Cleaning the tweets
Quetzal.tweet_cleaner()
# Data Mining
Quetzal.tweet_miner()

# STEP 3 : VIEW SOME OUTPUTS -----------------------------------------------------------------------

for item in Quetzal._data:
    print("TEXT CLEANED")
    print(Quetzal._data[item]['text_cleaned'])
    print("\nHASHTAGS")
    print(Quetzal._data[item]['hashtags'])
    print("\nMENTIONS")
    print(Quetzal._data[item]['mentions'])
    print("\n----------\n")