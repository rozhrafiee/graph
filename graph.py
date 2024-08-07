import csv
import json
from collections import defaultdict, deque
import heapq

class Graph:
    def init(self):
        self.adj_matrix = []
        self.adj_list = defaultdict(list)
        self.vertices = []
        self.edges = []

    @staticmethod
    def from_csv(file_path):
        graph = Graph()
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            graph.adj_matrix = [[int(cell) for cell in row] for row in reader]
            graph.vertices = [i for i in range(len(graph.adj_matrix))]
            graph._matrix_to_list()
        return graph

    @staticmethod
    def from_adj_matrix(matrix):
        graph = Graph()
        graph.adj_matrix = matrix
        graph.vertices = [i for i in range(len(matrix))]
        graph._matrix_to_list()
        return graph

    @staticmethod
    def from_json(json_str):
        graph = Graph()
        edges = json.loads(json_str)
        for edge in edges:
            u, v, w = edge['u'], edge['v'], edge['weight']
            graph.adj_list[u].append((v, w))
            graph.adj_list[v].append((u, w))  # for undirected graphs
            if u not in graph.vertices:
                graph.vertices.append(u)
            if v not in graph.vertices:
                graph.vertices.append(v)
        graph._list_to_matrix()
        return graph

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

    def _matrix_to_list(self):
        self.adj_list.clear()
        self.edges.clear()
        for i, row in enumerate(self.adj_matrix):
            for j, val in enumerate(row):
                if val > 0:
                    self.adj_list[i].append((j, val))
                    self.edges.append((i, j, val))

    def _list_to_matrix(self):
        n = len(self.vertices)
        self.adj_matrix = [[0] * n for _ in range(n)]
        for u in self.adj_list:
            for v, w in self.adj_list[u]:
                self.adj_matrix[u][v] = w

    def num_vertices(self):
        return len(self.vertices)

    def num_edges(self):
        return len(self.edges)

    def get_vertices(self):
        return self.vertices

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([v for v, _ in self.adj_list[vertex] if v not in visited])
        return result

    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend([v for v, _ in self.adj_list[vertex] if v not in visited])
        return result

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