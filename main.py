from collections import deque

class Graph:
    def __init__(self, a_list):
        self.a_list = a_list

    def get_neighbors(self, v):
        return self.a_list[v]

    def h(self, n):
        H = {
            'S': 10,
            'A': 8,
            'B': 9,
            'C': 7,
            'D': 4,
            'E': 3,
            'F': 0,
            'G': 6,
            'H': 6
        }
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

a_list = {
    'S': [('A', 3), ('B', 2), ('C', 5)],
    'A': [('C', 3), ('G', 2)],
    'B': [('D', 6)],
    'C': [('H', 3)],
    'D': [('F', 3)],
    'E': [('F', 5)],
    'G': [('D', 4)],
    'H': [('A', 4)]
}
graph1 = Graph(a_list)
graph1.a_star_algorithm('S','F')
