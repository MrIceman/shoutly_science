import json

import matplotlib.pyplot as plt

from nlp.engine import classify_report

lng = []
lat = []

with open('data/july-august-niedersachsen-2019.json') as file:
    json_data = json.load(file)

temp_results = []
for i in json_data:
    story = i['body']
    destructed_name = i['company']['name'].split()

    model = {
        'title': i['title'],
        'local': destructed_name[len(destructed_name) - 1],
        'url': i['url'],
        'date': i['published'],
        'story': i['body'],
        'foreign_key': i['id'],
        'class': 'other'
    }
    temp_results.append(model)

classified_data = {}

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
# plt.plot(['classified', 'unclassified'], [len(classified_summed_data), len(unclassified_data)])

plt.plot([key for key, value in classified_data.items()], [len(value) for key, value in classified_data.items()])
plt.show()
