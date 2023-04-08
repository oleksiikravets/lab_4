from matrix import *
import numpy as np

matrix = np.matrix(graph)
print(f"Matrix of weights: \n{matrix}\n")

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.num_rows = len(graph)

    def breadth_first_search(self, start, end, parent):

        visited = [False] * (self.num_rows)

        queue = []

        queue.append(start)
        visited[start] = True

        while queue:

            current_node = queue.pop(0)

            for index, value in enumerate(self.graph[current_node]):
                if visited[index] == False and value > 0:

                    queue.append(index)
                    visited[index] = True
                    parent[index] = current_node
                    if index == end:
                        return True

        return False

    def ford_fulkerson(self, source, sink):

        parent = [-1] * (self.num_rows)

        max_flow = 0

        while self.breadth_first_search(source, sink, parent):

            path_flow = float("Inf")
            current_node = sink
            while (current_node != source):
                path_flow = min(path_flow, self.graph[parent[current_node]][current_node])
                current_node = parent[current_node]

            max_flow += path_flow

            current_node = sink
            while (current_node != source):
                previous_node = parent[current_node]
                self.graph[previous_node][current_node] -= path_flow
                self.graph[current_node][previous_node] += path_flow
                current_node = previous_node

        return max_flow

graph_obj = Graph(graph)

source_node = 0
sink_node = 7

print("Maximum flow is %d " % graph_obj.ford_fulkerson(source_node, sink_node))
