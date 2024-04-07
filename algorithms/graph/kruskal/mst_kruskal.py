class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    mst = []
    total_cost = 0

    # Create disjoint set with all vertices
    vertices = set(graph.keys())
    ds = DisjointSet(vertices)

    # Sort edges by weight
    edges = sorted([(u, v, weight) for u in graph for v, weight in graph[u].items()], key=lambda x: x[2])

    for edge in edges:
        u, v, weight = edge
        if ds.find(u) != ds.find(v):
            mst.append((u, v))
            total_cost += weight
            ds.union(u, v)

    return mst, total_cost

# Example usage:
graph = {
    'A': {'B': 5, 'D': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'B': 2, 'D': 4, 'E': 6},
    'D': {'A': 3, 'B': 1, 'C': 4, 'E': 5},
    'E': {'C': 6, 'D': 5}
}

mst, total_cost = kruskal(graph)
print("Minimum Spanning Tree (Edges):", mst)
print("Total Cost:", total_cost)
