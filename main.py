import json
import matplotlib.pyplot as plt

from nlp.bag_of_words.engine import get_weighted_words_of_stories
from nlp.dictionary.engine import classify_report

lng = []
lat = []

with open('data/located_data_22-october.json', encoding='utf8') as file:
    json_data = json.load(file)

temp_results = []
for i in json_data:
    story = i['story']

    model = {
        'title': i['title'],
        'local': i['local'],
        'url': i['url'],
        'date': i['date'],
        'story': i['story'],
        'class': 'other'
    }
    temp_results.append(model)

classified_data = {}

# with open('words.json', 'w') as file:
#    json.dump([{'{}'.format(k): '{}'.format(v)} for k, v in tfidf.items()], file, ensure_ascii=False)

"""
for i in temp_results:
    classify_report(i)
    if i['class'] != 'other':
        results = classified_data.get(i['class'], [])
        results.append(i)
        classified_data[i['class']] = results
    else:
        print('other')

plt.tight_layout()
# plt.plot([x for x in classified_data.keys()], [len(y) for y in classified_data.values()])
classified_summed_data = [item for k, v in classified_data.items() for item in v]
unclassified_data = [v for v in temp_results if v not in classified_summed_data]

with open('unclassified_data.json', 'w', encoding='UTF8') as classified:
    import json

    json.dump(unclassified_data, classified, ensure_ascii=False)

# shows amount of classified and unclassified

with open('words.json') as json_file:
    data = json.load(json_file)

temp_dict = {}
for x in data:
    temp_dict[list(x.keys())[0]] = list(x.values())[0]

sorted_dict = {}
for key, value in sorted(temp_dict.items(), key=lambda item: item[0], reverse=True):
    sorted_dict[key] = temp_dict[key]

plt.plot([k for k in list(sorted_dict.keys())[0:5]],
         [v for v in list(sorted_dict.values())[0:5]])
plt.show()
"""
matrix, index_dict = get_weighted_words_of_stories(temp_results)


def get_words_for_story(story_index):
    results = {}
    for row in matrix[story_index].toarray():
        for column, value in enumerate(row):
            if value > 0.2:
                results[index_dict[column]] = value
    for k, v in results.items():
        print('{}: {}'.format(k, v))
    # return results
