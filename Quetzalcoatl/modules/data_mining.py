import re
import Quetzalcoatl.modules.data_cleaning as data_cleaning

def hashtag_extractor(tweet_text: str) -> list:
    """
    Extract hashtags from a tweet\n
    Returns a list of hashtags
    """

    try:
        # hashtags = pattern.match(tweet_text)
        hashtags = re.findall(r"#(\w+)", tweet_text)

    except:
        hashtags = ['']

    return hashtags

def mention_extractor(tweet_text: str) -> list:
    """
    Extract mentions from a tweet\n
    Returns a list of mentions
    """
    try:
        # hashtags = pattern.match(tweet_text)
        mentions = re.findall(r"@(\w+)", tweet_text)

    except:
        mentions = ['']

    return mentions

def sub_topics_extractor(tweets_text_list : list, lang_ = 'fr_core_news_sm', max_most_common = 5) -> any:
    """
    Extract sub_topicts\n
    take all the tweets' text as parameter\n
    return a dict of sub_topics
    """

    # Load the correct language for spacy
    import spacy
    from spacy.lang.fr.stop_words import STOP_WORDS
    from string import punctuation
    from collections import Counter

    # IMPORTANT : You must download the language package from spacy
    nlp = spacy.load(lang_)

    # Concatenate the list of texts
    big_text = data_cleaning.get_big_text(tweets_text_list)
    big_text = data_cleaning.emojies_remover(big_text)

    doc = nlp(big_text)

    keywords = []
    stopwords = list(STOP_WORDS)
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    for token in doc:
        if(token.text in stopwords or token.text in punctuation):
            continue
        if token.pos_ in pos_tag:
            keywords.append(token.text)
    freq_words = Counter(keywords)

    return freq_words.most_common(max_most_common)

def emojies_extractor(tweets_text_list : list, lang_ = 'fr_core_news_sm', max_most_common = 5) -> any:
    """
    Extract occurrence of emojies\n
    take all the tweets' text as parameter\n
    return a dict of most used emojies
    """
    import spacy
    from spacymoji import Emoji
    from collections import Counter

    nlp = spacy.load(lang_)
    nlp.add_pipe("emoji", first = True)

    # Concatenate the list of texts
    big_text = data_cleaning.get_big_text(tweets_text_list)

    doc = nlp(big_text)
    emojies = [emoji[0] for emoji in doc._.emoji]
    freq_emojies = Counter(emojies)

    return freq_emojies.most_common(max_most_common)