import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

from nlp.classes import WORDS, CLASSES, MULTIPLE_INDEX
from nlp.util.text import clean_text
from nlp.util.word import word_in_list

nltk.download('stopwords')

stop_words = stopwords.words('german')


def classify_reports(reports):
    matrix, index_dict = _get_weighted_words_of_stories(reports)
    # go through each row, a row represents the values within a title
    for report_index, row in enumerate(matrix.toarray()):
        bow = []
        # go through each column, a column represents the vocabulary and the value
        # represents the tfidf value
        for column, value in enumerate(row):
            # filter out words that have a low tfidf value (they are uncommon and therefore not used for classification)
            if value > 0.01:
                bow.append(index_dict[column])
        # use the words and compare them with our dictionary for the actual classifications
        _classify_report(reports[report_index], bow)


def get_word_matrix_for_reports(reports):
    # go through each row, a row represents the values within a title
    matrix, index_dict = _get_weighted_words_of_stories(reports)

    return matrix


# tokenizes the story, removes the stop words and
# returns a matrix with all important words within a story
def _get_weighted_words_of_stories(reports):
    # prepare the title, make it lower and remove trash words
    text_data = [clean_text(r['title'].lower()) for r in reports]
    tfidf = TfidfVectorizer()
    # get the bag of words matrix
    feature_matrix = tfidf.fit_transform(text_data)
    # create the lookup dictionary
    index_dictionary = {}
    # k is the index of the word and v is the word
    for k, v in tfidf.vocabulary_.items():
        index_dictionary[v] = k
    return feature_matrix, index_dictionary


def _classify_report(report, bag_of_words):
    found = False
    # by default the class is 'other'
    report['class'] = 12
    for word in bag_of_words:
        if found:
            return
        for key, value in WORDS.items():
            target_word = word.lower()
            # check if a word is within the bag of words that we can use to classify the report
            if word_in_list(target_word, value):
                # todo check if report has been classified already and if yes then evaluate
                # the decision
                if report['class'] != 12 and report['class'] != key:
                    # report has been classified already, if this is another classification then it is 'multiple
                    report['class'] = MULTIPLE_INDEX
                    return
                classification = key
                report['class'] = classification
