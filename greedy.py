import heapq
from collections import defaultdict
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, node1, node2, distance):
        self.edges[node1].append((node2, distance))
        self.edges[node2].append((node1, distance))

def manhattan_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return abs(x1 - x2) + abs(y1 - y2)

def greedy_search(graph_i, start, goal):
    open_nodes = []
    heapq.heappush(open_nodes, (0, start))
    came_from = {}
    
    while open_nodes:
        _, current = heapq.heappop(open_nodes)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor, _ in graph_i.edges[current]:
            if neighbor not in came_from or neighbor == start:
                priority = manhattan_distance(neighbor, goal)
                heapq.heappush(open_nodes, (priority, neighbor))
                came_from[neighbor] = current

    return None

def plot_graph(graph_i, path_i):
    fig, ax = plt.subplots()

    for node, neighbors in graph_i.edges.items():
        for neighbor, _ in neighbors:
            plt.plot([node[0], neighbor[0]], [node[1], neighbor[1]], 'bo-', linewidth=0.5, markersize=8)

    if path_i:
        path_x, path_y = zip(*path_i)
        plt.plot(path_x, path_y, 'ro-', linewidth=2, markersize=10)

    ax.set_aspect('equal')
    plt.grid(True)
    plt.show()

graph = Graph()
graph.add_edge((0, 0), (0, 1), 5)
graph.add_edge((0, 1), (1, 0.5), 1)
graph.add_edge((2.4, 0), (1, 0.5), 1)
graph.add_edge((2.4, 0), (1, 1), 1)

path = greedy_search(graph, (0, 0), (1, 1))
print(path)

plot_graph(graph, path)
