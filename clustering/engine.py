from pylab import *
from math import cos, asin, sqrt


def _distance(lat1, lon1, lat2, lon2):
    """
    Calculates the distance between point 1 and point 2
    :param lat1:
    :param lon1:
    :param lat2:
    :param lon2:
    :return:  distance in km
    """
    p = 0.017453292519943295  # Pi/180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))  # 2*R*asin...


class ClusterEngine:

    def __init__(self, data_items, classification, distance_between_points_in_km=10):
        self.data = [z for z in data_items if
                     50 < z['lat'] < 54 and 20 > z['lng'] > 0 and z['classification'] == classification]
        self.clustered_elements = []
        self.clusters = dict()
        self.distance_between_points = distance_between_points_in_km

    def get_clusters(self):
        self._find_and_append_successors(self.data)
        return self.clusters

    def get_means_for_clusters(self):
        mean_cords = []
        for _, v in self.clusters.items():
            if len(v) < 4:
                continue
            print('cluster {} has {} items'.format(_, len(v)))
            # lets get the mean
            mean_lat = sum([p['lat'] for p in v]) / len(v)
            mean_lng = sum([p['lng'] for p in v]) / len(v)
            items = [i for i in v]
            mean_cords.append({
                'lat': mean_lat,
                'lng': mean_lng,
                'items': items
            })
        return mean_cords

    def _find_and_append_successors(self, collection=None, parent=None):
        for p in collection:
            if p is None:
                continue
            if p['id'] in self.clustered_elements:
                continue
            if parent is not None:
                current_index = parent['id']
                neighbors = self.clusters.get(parent['id'], [])
            else:
                neighbors = []
                current_index = p['id']
                neighbors.append(p)
            self.clustered_elements.append(p['id'])

            for neighbor in collection:
                if neighbor == p:
                    continue
                if neighbor is None:
                    continue
                if neighbor['id'] in self.clustered_elements:
                    continue
                if _distance(p['lat'], p['lng'], neighbor['lat'], neighbor['lng']) < self.distance_between_points:
                    neighbors.append(neighbor)
                    self.clusters[current_index] = neighbors
                    if parent is not None:
                        self._find_and_append_successors(neighbors, parent)
                    else:
                        self._find_and_append_successors(neighbors, p)
