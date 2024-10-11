graph = {
    'A': ['B', 'C', 'U'],
    'B': ['E', 'G'],
    'C': ['G', 'I', 'J'],
    'U': ['K', 'Y'],
    'E': ['G', 'M'],
    'G': ['M'],
    'I': ['M'],
    'J': ['K'],
    'K': ['J'],
    'Y': ['M'],
    'M': []
}

heuristics = {
    'A': 7,
    'B': 5,
    'C': 3,
    'U': 4,
    'E': 2,
    'G': 3,
    'I': 6,
    'J': 4,
    'K': 1,
    'Y': 2,
    'M': 0
}

def hill_climbing(starting_node, max_iterations):
    current_node = starting_node
    path = [current_node]

    for _ in range(max_iterations):
        neighbors = graph.get(current_node, [])
        neighbor_values = [(neighbor, heuristics[neighbor]) for neighbor in neighbors]

        if not neighbor_values:
            break
        best_neighbor, best_value = min(neighbor_values, key=lambda x: x[1])

        current_node = best_neighbor
        path.append(current_node)

        if current_node == 'M':
            break

    return path

starting_node = 'A'
max_iterations = 100
path = hill_climbing(starting_node, max_iterations)
print(path)
