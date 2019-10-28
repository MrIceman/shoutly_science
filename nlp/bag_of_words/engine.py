import nltk
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

from nlp.classes import WORDS, CLASSES
from nlp.util.text import clean_text
from nlp.util.word import mark_in_word

nltk.download('stopwords')

stop_words = stopwords.words('german')


# tokenizes the story, removes the stop words and
# returns a matrix with all important words within a story
def _get_weighted_words_of_stories(reports):
    text_data = [clean_text(r['title'].lower()) for r in reports]
    print('text data: {}'.format(text_data))
    tfidf = TfidfVectorizer()
    feature_matrix = tfidf.fit_transform(text_data)
    index_dictionary = {}
    for k, v in tfidf.vocabulary_.items():
        index_dictionary[v] = k
    return feature_matrix, index_dictionary


def classify_reports(reports):
    matrix, index_dict = _get_weighted_words_of_stories(reports)

    results = {}
    for row in matrix:
        for column, value in enumerate(row.toarray()):
            if value > 0.2:
                results[index_dict[column]] = value
    for k, v in results.items():
        print('{}: {}'.format(k, v))
    for index, item in enumerate(reports):
        for bow in matrix[index].toarrayy():
            pass




def _classify_report(report, bag_of_words):
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
    filtered_tokenized_words = clean_and_tokenize_text(report['story'])
    for word in filtered_tokenized_words:
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
