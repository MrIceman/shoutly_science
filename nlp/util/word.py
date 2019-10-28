def word_in_list(word, marked_words):
    for w in marked_words:
        if w in word:
            return True
    return False
