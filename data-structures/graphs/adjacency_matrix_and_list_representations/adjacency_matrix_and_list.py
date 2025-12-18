class GraphRepresentation:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.adj_list = [[] for _ in range(size)]

    def add_edge(self, u, v):
        # For Matrix
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1 # Undirected
        
        # For List
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_representations(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)
            
        print("\nAdjacency List:")
        for i, neighbors in enumerate(self.adj_list):
            print(f"{i}: {neighbors}")

if __name__ == "__main__":
    g = GraphRepresentation(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)
    
    g.print_representations()
