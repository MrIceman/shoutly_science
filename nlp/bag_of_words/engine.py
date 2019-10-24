import nltk
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

from nlp.util.text import clean_text

nltk.download('stopwords')

stop_words = stopwords.words('german')


# tokenizes the story, removes the stop words and
# returns a matrix with all important words within a story
def get_weighted_words_of_stories(reports):
    text_data = [clean_text(r['title'].lower()) for r in reports]
    print('text data: {}'.format(text_data))
    tfidf = TfidfVectorizer()
    feature_matrix = tfidf.fit_transform(text_data)
    index_dictionary = {}
    for k, v in tfidf.vocabulary_.items():
        index_dictionary[v] = k
    return feature_matrix, index_dictionary
