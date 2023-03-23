import heapq

class Node:
    def __init__(self, state, parent, action, h):
        self.state = state
        self.parent = parent
        self.action = action
        self.h = h

    def __lt__(self, other):
        return self.h < other.h

def greedy_search(start_state, goal_state, distances):
    frontier = []
    start_node = Node(start_state, None, None, distances[start_state].get(goal_state, float('inf')))
    heapq.heappush(frontier, (start_node.h, start_node))
    explored = set()
    visited_states = []

    while frontier:
        current_node = heapq.heappop(frontier)[1]
        visited_states.append(current_node.state)

        if current_node.state == goal_state:
            path = []
            while current_node.parent is not None:
                path.append(current_node.action)
                current_node = current_node.parent
            path.reverse()
            return path, visited_states

        explored.add(current_node.state)

        for neighbor in distances[current_node.state]:
            if neighbor not in explored:
                h = distances[neighbor].get(goal_state, float('inf'))
                neighbor_node = Node(neighbor, current_node, neighbor, h)
                heapq.heappush(frontier, (neighbor_node.h, neighbor_node))

    return None, visited_states

# Exemplo de uso

distances = {
    'A': {'B': 1, 'C': 3, 'D': 7, 'F': float('inf')},
    'B': {'A': 1, 'C': 1, 'E': 2, 'F': float('inf')},
    'C': {'A': 3, 'B': 1, 'D': 3, 'E': 1, 'F': float('inf')},
    'D': {'A': 7, 'C': 3, 'F': float('inf')},
    'E': {'B': 2, 'C': 1, 'F': 2},
    'F': {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': 2}
}

start_city = 'A'
goal_city = 'E'

path, visited_states = greedy_search(start_city, goal_city, distances)

if path is None:
    print("Não foi possível encontrar um caminho.")
else:
    print(f"Caminho encontrado: {start_city} -> {' -> '.join(path)}.")
    print(f"Estados visitados: {' -> '.join(visited_states)}")
