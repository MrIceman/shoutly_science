from nlp.classes import WORDS, CLASSES
from nlp.util.text import clean_and_tokenize_text
from nlp.util.word import word_in_list
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

stop_words = stopwords.words('german')


def classify_report(report):
    found = False
    for key, value in WORDS.items():
        title = report['title'].replace('\n', '').replace('-', ' ').lower()
        if word_in_list(title, value):
            classification = CLASSES[key]
            report['class'] = classification
            found = True
    if found:
        return
    # nothing was found within the title lets check the body
    filtered_tokenized_words = clean_and_tokenize_text(report['story'])
    for word in filtered_tokenized_words:
        lowered_word = word.lower()
        # lets compare the word with our classification names
        if found:
            return
        for key, value in WORDS.items():
            if found:
                return
            if word_in_list(lowered_word, value):
                classification = CLASSES[key]
                report['class'] = classification
                found = True
