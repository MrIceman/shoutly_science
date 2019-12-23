import json

import numpy
from keras import Sequential
from keras.layers import Embedding, GlobalAveragePooling1D, Dense, Flatten
from keras_preprocessing.sequence import pad_sequences

from nlp.bag_of_words.engine import _get_weighted_words_of_stories, get_word_matrix_for_reports
from nlp.classes import CLASSES


def get_x_and_y_labels(reports):
    classes = []

    for i in reports:
        class_name = i['classification_name']
        class_key = 12  # by default its "other"
        for key, value in CLASSES.items():
            if class_key != 12:  # class key already found
                continue
            if class_name.lower() == value.lower():
                class_key = key
                continue
        classes.append(class_key)
    matrix = get_word_matrix_for_reports(reports)
    return classes, [y for y in matrix]


def add_json(target_collection, filename):
    add_urls = {}
    add_ids = []
    with open(filename, encoding='utf8') as file:
        _data = json.load(file)
        for i in _data:
            if add_urls.get(i['url'], None) is None and i['id'] not in add_ids:
                add_urls[i['url']] = 1
                add_ids.append(i['id'])
                target_collection.append(i)


json_data = []
add_json(json_data, '../../data/dump-23-12-19.json')

class_list, data_set = get_x_and_y_labels(json_data)

x_train = [d.toarray()[0] for d in data_set[0:3000]]
y_train = class_list[0:3000]

x_val = [d.toarray()[0] for d in data_set[3000:7415]]
y_val = class_list[3000:7415]

model = Sequential()
model.add(Embedding(len(data_set[0].toarray()[0]), 12, input_length=len(data_set[0].toarray()[0])))
model.add(Dense(32, activation='relu'))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
# model.add(Flatten())

model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

fitModel = model.fit(numpy.array(x_train), numpy.array(y_train), epochs=40, batch_size=512,
                     validation_data=(numpy.array(x_val), numpy.array(y_val)), verbose=1)

results = model.evaluate(data_set, class_list)
