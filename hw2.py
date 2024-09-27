import collections


def bfs(tree, root, dest):
    visited, queue = {}, collections.deque([root])
    visited[root] = None
    queue.append(root)

    while queue:
        vertex = queue.popleft()
        print(vertex, end = " ")
        if vertex == dest:
            path = []
            while vertex:
                path.append(vertex)
                vertex = visited[vertex]
            return path[::-1]

        for neighbor in tree[vertex]:
            if neighbor not in visited:
                visited[neighbor] = vertex
                queue.append(neighbor)


if __name__ == '__main__':
    tree = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9], 5: [10, 11], 6: [12, 13], 7: [14, 15], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []}
    print("Breadth First Search path starting with 1 and destination node 11: ")
    print(bfs(tree, 1, 11))
