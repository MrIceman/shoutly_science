from pylab import *
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

import json

with open('data/data-dump-13-nov-2019.json', 'r') as my_file:
    data = json.load(my_file)
    CLASSIFICATION_TYPE = 2
    filtered_data = [z for z in data if
                     52.4 < z['lat'] < 52.75 and 8 > z['lng'] > 6.5 and z['classification'] == CLASSIFICATION_TYPE]
    x = [s['lat'] for s in filtered_data if s['classification']]
    y = [t['lng'] for t in filtered_data if t['classification']]
    color = ['b' for _ in filtered_data if _['classification']]

scatter(x, y, s=1, marker='o', c=color, cmap=3)

left, right = ax.get_xlim()
low, high = ax.get_ylim()
arrow(left, 3, right - left, 0, length_includes_head=True, head_width=0.15)
arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)

grid()

show()

clustered_elements = []
clusters = dict()

DISTANCE_THRESHOLD_LAT = 0.01
DISTANCE_THRESHOLD_LNG = 0.01
for idx, val in enumerate(filtered_data):
    if val is None:
        continue
    if val['id'] in clustered_elements:
        continue

    current_element = val
    # initial item, we start clustering with it
    clustered_elements.append(current_element['id'])
    current_list = clusters.get(current_element['id'], [])
    clusters[current_element['id']] = current_list
    current_element = val

    for succ in filtered_data:
        if succ is None:
            continue

        if succ['id'] in clustered_elements:
            continue
        elif square(current_element['lat'] - succ['lat']) < DISTANCE_THRESHOLD_LAT and square(
                current_element['lng'] - succ['lng']) < DISTANCE_THRESHOLD_LNG:
            # initial item, we start clustering with it
            clustered_elements.append(succ['id'])
            current_list = clusters.get(current_element['id'], [])
            current_list.append(succ['id'])
            clusters[current_element['id']] = current_list
            # we have a successor


def square(value):
    return value * value
