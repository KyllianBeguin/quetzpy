import Quetzalcoatl
import json

Bearer_token = "AAAAAAAAAAAAAAAAAAAAAKv%2FeQEAAAAAX2Vfj2qtecbSEOCuRL%2FYKKdSDaw%3DIJf39mVQmAglieiCOHK1g7V9bvpVfFZzfSAKMxlS9MFTT6wzdt"
# auth = tw.OAuth2BearerHandler(Bearer_token)
# api = tw.API(auth)

# Recherche
# search = api.search_tweets(q="Steam", lang = "fr", count = 100)
# item0 = search[0]._json
# keys_keep = ["text", "retweet_count", "favorite_count", "id"]
# item0_clean = {key:item0[key] for key in item0 if key in keys_keep}
# item0_clean["user_id"] = item0["user"]["id"]
# print(json.dumps(item0_clean, indent = 2))

# ----------------

Quetzal = Quetzalcoatl.Quetzalcoatl(Bearer_token, topic = "#twitchstreamer")
Quetzal.connect()
Quetzal.extract_tweets(language = "fr")
# print(len(Quetzal._data))
# print(Quetzal._data_RT)
print(json.dumps(Quetzal._data, indent = 2))