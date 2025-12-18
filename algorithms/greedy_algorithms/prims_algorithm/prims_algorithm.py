import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_val and mst_set[v] == False:
                min_val = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1 # First node is always the root of

        for cout in range(self.V):
            # Pick the minimum distance vertex from the set of vertices not
            # yet processed. u is always equal to src in first iteration.
            u = self.min_key(key, mst_set)

            # Put the minimum distance vertex in the shortest path tree
            mst_set[u] = True

            # Update dist value of the adjacent vertices of the picked vertex
            # only if the current distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mst_set[v] == False and \
                   key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

if __name__ == "__main__":
    g = Graph(5)
    g.graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    g.prim_mst()
