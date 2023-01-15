def track_words(self, Params_manager, topic : str) -> dict:
    """
    View how many times a word is detected in the tweets\n
    Take a list of words to track\n
    Returns a dict of the tracked words and the associated occurrence
    """

    # Initialize the dict of {words: occurrence}
    dict_tracker = dict()
    for to_track_word in Params_manager.Extrac_track_words:
        result = sum([1 for key, val in self.data_topics[topic]["tweets"].items() if to_track_word.lower() in val["text_cleaned"]])
        dict_tracker[to_track_word] = result

    return dict_tracker

def track_all():
    print("foo")
    return "foo"

def show_occurrence(self, Params_manager, topic) -> dict:
    """
    View the occurrence of either linked hashtags or mentions\n
    Take a parameter to know if it shall analyze hashtags or mentions\n
    Returns a dict of words and the associated occurrence
    """

    results = dict()
    
    for show_this_occurence in Params_manager.Extrac_show_occurrence:
        all_words = []
        for key, val in self.data_topics[topic]["tweets"].items():
            all_words.extend(val[show_this_occurence])
            
        all_words_uniques = set(all_words)

        result_for_this = {item:all_words.count(item) for item in all_words_uniques}
        result_for_this_sorted = dict(filter(lambda item_sort : item_sort[1] >= Params_manager.Extrac_show_occurrence_threshold, sorted(result_for_this.items(), key = lambda item : item[1], reverse = True)))
        results[show_this_occurence] = result_for_this_sorted

    return results