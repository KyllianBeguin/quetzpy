def track_words(self, param = []) -> dict:
    """
    View how many times a word is detected in the tweets\n
    Take a list of words to track\n
    Returns a dict of the tracked words and the associated occurrence
    """

    # Initialize the dict of {words: occurrence}
    dict_tracker = dict()

    for to_track_word in param:
        result = sum([1 for key, item in self._data.items() if to_track_word in item['text']])
        dict_tracker[to_track_word] = result

    return dict_tracker

def track_all():
    print("foo")
    return "foo"

def show_occurrence(self, param = ["hashtags", 0]) -> dict:
    """
    View the occurrence of either linked hashtags or mentions\n
    Take a parameter to know if it shall analyze hashtags or mentions\n
    Returns a dict of words and the associated occurrence
    """
    
    all_words = []

    for key, item in self._data.items():
        all_words.extend(item[param[0]])

    all_words_uniques = set(all_words)

    result = {item:all_words.count(item) for item in all_words_uniques}
    result_sorted = dict(filter(lambda item_sort : item_sort[1] > param[1], sorted(result.items(), key = lambda item : item[1], reverse = True)))


    return result_sorted