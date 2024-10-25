terminal_values = [3, 5, 17, 8, -2, 5, -1, 7]

def minimax(node, depth, is_maximizing):
    if depth == 3:
        return terminal_values[node]

    if is_maximizing:
        best_value = float('-inf')
        for i in range(2):
            val = minimax(2 * node + i, depth + 1, False)
            best_value = max(best_value, val)
        return best_value
    else:
        best_value = float('inf')
        for i in range(2):
            val = minimax(2 * node + i, depth + 1, True)
            best_value = min(best_value, val)
        return best_value

optimal_value = minimax(0, 0, True)
print("Optimal value is", optimal_value)
