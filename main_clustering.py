from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import random

fig = plt.figure()
ax = fig.add_subplot(111)

import json

taken_colors = []


def get_color():
    colors = ['#2D1B3E', '#BF6D6D',
              '#E76C06',
              '#5A0EA2', '#918FC2', '#231ECC', '#1E95CC', '#5E8191', '#5E9184', '#06E7AD', '#5BE706',
              '#E7CF06',
              ]
    result = None
    for c in colors:
        if c not in taken_colors:
            taken_colors.append(c)
            result = c
            return result


with open('data/dump-16-11-19.json', 'r') as my_file:
    data = json.load(my_file)
    CLASSIFICATION_TYPE = 2
    filtered_data = [z for z in data if
                     52.4 < z['lat'] < 52.75 and 8 > z['lng'] > 6.5 and z['classification'] == CLASSIFICATION_TYPE]

clustered_elements = []
clusters = dict()

DISTANCE_THRESHOLD_LAT = 0.0001
DISTANCE_THRESHOLD_LNG = 0.0001

# parent is the parent of the cluster, e.g. the index id

parent_node = None


def find_and_append_successors(collection=None, parent=None, current_item=None):
    global parent_node
    global clustered_elements
    global clusters

    for p in collection:
        if p is None:
            continue
        if p['id'] in clustered_elements:
            continue
        if parent is not None:
            current_index = parent['id']
            neighbors = clusters.get(parent['id'], [])
        else:
            neighbors = []
            current_index = p['id']
            neighbors.append(p)
        clustered_elements.append(p['id'])

        for neighbor in collection:
            if neighbor == p:
                continue
            if neighbor is None:
                continue
            if neighbor['id'] in clustered_elements:
                continue
            if square(p['lat'] - neighbor['lat']) < DISTANCE_THRESHOLD_LAT and square(
                    p['lng'] - neighbor['lng']) < DISTANCE_THRESHOLD_LNG:
                neighbors.append(neighbor)
                clusters[current_index] = neighbors
                if parent is not None:
                    find_and_append_successors(neighbors, parent, neighbor)
                else:
                    find_and_append_successors(neighbors, p, neighbors)


find_and_append_successors(collection=filtered_data)

x, y, colors = [], [], []
last_color = None

for _, v in clusters.items():
    color = get_color()
    for i in v:
        x.append(i['lat'])
        y.append(i['lng'])
        colors.append(color)

scatter(x, y, s=4, marker='o', c=colors, cmap=3)

left, right = ax.get_xlim()
low, high = ax.get_ylim()
arrow(left, 3, right - left, 0, length_includes_head=True, head_width=0.15)
arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)

grid()

show()


def square(value):
    return value * value
