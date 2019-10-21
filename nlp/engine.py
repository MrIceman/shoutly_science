from nlp.classes import WORDS, CLASSES
from util.word import mark_in_word


def classify_report(report):
    found = False
    for key, value in WORDS.items():
        title = report['title'].replace('\n', '').replace('-', ' ').lower()
        if mark_in_word(title, value):
            classification = CLASSES[key]
            report['class'] = classification
            found = True
    if found:
        return
    # nothing was found within the title lets check the body
    for word in report['story'].replace('\n', '').replace('-', ' ').split():
        lowered_word = word.lower()
        # lets compare the word with our classification names
        if found:
            return
        for key, value in WORDS.items():
            if found:
                return
            if mark_in_word(lowered_word, value):
                classification = CLASSES[key]
                report['class'] = classification
                found = True
