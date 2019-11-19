import random

import matplotlib.pyplot as plt
from pylab import *

from clustering.engine import ClusterEngine

fig = plt.figure()
ax = fig.add_subplot(111)

import json

taken_colors = []


def get_color():
    return "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])


with open('data/dump-16-11-19.json', 'r') as my_file:
    data = json.load(my_file)
CLASSIFICATION_TYPE = 0

engine = ClusterEngine(data, CLASSIFICATION_TYPE)
clusters = engine.get_clusters()

x, y, colors = [], [], []
last_color = None

for _, v in clusters.items():
    if len(v) < 5:
        continue

    color = get_color()
    for i in v:
        x.append(i['lat'])
        y.append(i['lng'])
        colors.append(color)

scatter(x, y, s=5, marker='o', c=colors, cmap=3)

mean_lats = []
mean_lngs = []
mean_colors = []
for _, v in clusters.items():
    if len(v) < 5:
        continue
    # lets get the mean
    mean_lat = sum([p['lat'] for p in v]) / len(v)
    mean_lng = sum([p['lng'] for p in v]) / len(v)
    mean_colors.append('#000000')
    mean_lats.append(mean_lat)
    mean_lngs.append(mean_lng)

scatter(mean_lats, mean_lngs, s=5, c=mean_colors, cmap=3, marker='o', )

left, right = ax.get_xlim()
low, high = ax.get_ylim()
arrow(left, 3, right - left, 0, length_includes_head=True, head_width=0.15)
arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)

grid()

show()


def square(value):
    return value * value
