import heapq
from collections import defaultdict
import matplotlib.pyplot as plt

# Classe que representa um grafo
class Graph:
    # Inicializa o grafo com as arestas vazias
    def __init__(self):
        self.edges = defaultdict(list)

    # Adiciona uma aresta entre dois nós com uma distância
    def add_edge(self, node1, node2, distance):
        self.edges[node1].append((node2, distance))
        self.edges[node2].append((node1, distance))

# Calcula a distância de Manhattan entre dois nós
def manhattan_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return abs(x1 - x2) + abs(y1 - y2)

# Implementação do algoritmo A* para encontrar o caminho mais curto
def a_star(graph_i, start, goal):
    open_nodes = []
    heapq.heappush(open_nodes, (0, start))
    came_from = {}
    cost_so_far = {start: 0} # função g

    while open_nodes:
        _, current = heapq.heappop(open_nodes)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor, distance in graph_i.edges[current]:
            new_cost = cost_so_far[current] + distance
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:  # função g
                cost_so_far[neighbor] = new_cost
                priority = new_cost + manhattan_distance(neighbor, goal)
                heapq.heappush(open_nodes, (priority, neighbor))
                came_from[neighbor] = current

    return None  # Nenhum caminho encontrado

# Plota o grafo e o caminho encontrado pelo algoritmo A*
def plot_graph(graph_i, path_i):
    fig, ax = plt.subplots()

    # Plota as arestas
    for node, neighbors in graph_i.edges.items():
        for neighbor, _ in neighbors:
            plt.plot([node[0], neighbor[0]], [node[1], neighbor[1]], 'bo-', linewidth=0.5, markersize=8)

    # Plota o caminho encontrado
    if path_i:
        path_x, path_y = zip(*path_i)
        plt.plot(path_x, path_y, 'ro-', linewidth=2, markersize=10)

    ax.set_aspect('equal')
    plt.grid(True)
    plt.show()

# Criação do grafo e adição de arestas
graph = Graph()
graph.add_edge((0, 0), (0, 1), 5)
graph.add_edge((0, 1), (1, 0.5), 1)
graph.add_edge((2.4, 0), (1, 0.5), 1)
graph.add_edge((2.4, 0), (1, 1), 1)

# Encontra o caminho utilizando o algoritmo A* e exibe o resultado
path = a_star(graph, (0, 0), (1, 1))
print(path)

# Plota o grafo com o caminho encontrado
plot_graph(graph, path)