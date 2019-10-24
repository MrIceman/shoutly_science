def mark_in_word(word, marked_words):
    for w in marked_words:
        if w in word:
            return True
    return False
