import re

def hashtags_remover(tweet_text: str) -> str:
    """
    Remove the hashtags from a tweet\n
    Returns a text without any hastags
    """
    pattern = re.compile(r"\s#+\S+")

    tweet_text_cleaned = pattern.sub("", tweet_text)

    return tweet_text_cleaned

def mentions_remover(tweet_text: str) -> str:
    """
    Remove the mentions from a tweet\n
    Returns a text without any mentions
    """
    pattern = re.compile(r"\s@+\S+")

    tweet_text_cleaned = pattern.sub("", tweet_text)

    return tweet_text_cleaned

def websites_remover(tweet_text: str) -> str:
    """
    Remove the websites from a tweet\n
    Returns a text without any website
    """
    pattern = re.compile(r"\S+\\+\S+")
    tweet_text_cleaned_1 = pattern.sub("", tweet_text)

    pattern = re.compile(r"\s+http+\S+")

    tweet_text_cleaned_2 = pattern.sub("", tweet_text_cleaned_1)

    return tweet_text_cleaned_2

def remove_duplicates(self) -> str:
    """
    Remove duplicated tweets\n
    - Make an item_id from text and author_id\n
    - Drop duplicate based on item_id
    """
    items_id = []

    for item in self._data:
        length_text_quater = len(self._data[item]["text"])//4
        item_id = self._data[item]["text"][:length_text_quater] + str(self._data[item]["author_id"])
        items_id.append(item_id)
    
    set_items_id = set(items_id)

    if len(set_items_id) < len(items_id):
        temp = []
        new_data = {}
        for item in self._data:
            length_text_quater = len(self._data[item]["text"])//4
            if self._data[item]["text"][:length_text_quater] + str(self._data[item]["author_id"]) not in temp:
                temp.append(self._data[item]["text"][:length_text_quater] + str(self._data[item]["author_id"]))
                new_data.update(self._data[item])

        self._data = new_data
    
        return
    
    else:
        return self._data

def get_big_text(tweets_text_list : list):
    """
    Make a big text with all the tweets
    """

    big_text = ' '.join(tweets_text_list)
    big_text = big_text.replace('\n', ' ')
    big_text = re.sub(r'https?:\/\/.\S+', "", big_text)
    
    return big_text

def emojies_remover(big_text : str, lang_ = 'fr_core_news_sm'):
    """
    removes the emojies from the big text
    """

    import spacy
    from spacymoji import Emoji

    nlp = spacy.load(lang_)
    nlp.add_pipe("emoji", first = True)

    doc = nlp(big_text)
    emojies = set([emoji[0] for emoji in doc._.emoji])

    for emoji in emojies:
        big_text = big_text.replace(emoji, '')

    return big_text