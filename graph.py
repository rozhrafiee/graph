import csv
import json
from collections import defaultdict, deque
import heapq
class Graph:
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
