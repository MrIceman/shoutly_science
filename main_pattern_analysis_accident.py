import json

with open('data/dump-7-12-19.json', 'r') as file:
    data = json.load(file)
    print('data len: {}'.format(len(data)))
