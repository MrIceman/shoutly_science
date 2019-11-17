import pandas as pd

from nlp.util.date import convert_presse_time_to_ms

data_path = 'data/dump-16-11-19.json'
panda_data = pd.read_json(data_path)
print(panda_data.columns)


def unix(row):
    row.date = pd.Timestamp(row.date).timestamp()
    return row

data = panda_data.apply(unix, axis='columns')

model = ['id', 'lat', 'lng', 'date']
X = data[model]