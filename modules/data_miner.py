import re

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