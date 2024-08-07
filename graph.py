import csv
import json
from collections import defaultdict, deque
import heapq
class Graph:
     def to_csv(self, file_path):
        with open(file_path, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in self.adj_matrix:
                writer.writerow(row)

    def to_adj_matrix(self):
        return self.adj_matrix

    def to_json(self):
        json_edges = [{'u': u, 'v': v, 'weight': w} for u in self.adj_list for v, w in self.adj_list[u]]
        return json.dumps(json_edges)


    def num_vertices(self):
        return len(self.vertices)

    def num_edges(self):
        return len(self.edges)

    def get_vertices(self):
        return self.vertices
    def dijkstra(self, start):
        min_heap = [(0, start)]
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        while min_heap:
            curr_dist, u = heapq.heappop(min_heap)
            if curr_dist > distances[u]:
                continue
            for v, weight in self.adj_list[u]:
                distance = curr_dist + weight
                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(min_heap, (distance, v))
        return distances

# Example Usage:
# g = Graph.from_csv('graph.csv')
# print(g.num_vertices())
# print(g.bfs(0))
