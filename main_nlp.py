import json

import matplotlib.pyplot as plt
from nlp.bag_of_words.engine import _get_weighted_words_of_stories, classify_reports


def analyse_classes(reports):
    classifications = {}
    for report in reports:
        y = classifications.get(report['class'], [])
        y.append(i)
        classifications[report['class']] = y
    for k, v in classifications.items():
        print('{}: {}'.format(k, len(v)))

    plt.tight_layout()
    plt.plot([k for k, _ in classifications.items()], [len(v) for _, v in classifications.items()])
    plt.show()
    return classifications


def add_json_from_file(target_collection, filename):
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
# add_json_from_file(json_data, 'data/located_data_22-october.json')
add_json_from_file(json_data, 'data/data-dump-13-nov-2019.json')

temp_results = []

for i in json_data:
    if i is None:
        continue
    try:
        story = i['story']
    except:
        story = i['description']

    try:
        city = i['local']
    except:
        city = i['city']

        model = {
            'title': i['title'],
            'local': city,
            'url': i.get('url', ''),
            'date': i['date'],
            'story': story,
            'class': 'other'
        }
        temp_results.append(model)


def classify_and_analyse_temp():
    classify_reports(temp_results)
    return analyse_classes(temp_results)


matrix, index_dict = _get_weighted_words_of_stories(temp_results)


def get_words_for_story(story_index):
    results = {}
    for row in matrix[story_index].toarray():
        for column, value in enumerate(row):
            if value > 0:
                results[index_dict[column]] = value
    for k, v in results.items():
        print('{}: {}'.format(k, v))
    # return results
