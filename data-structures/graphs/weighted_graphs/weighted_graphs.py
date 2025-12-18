def weighted_graph_demo():
    # Adjacency List with Weights: vertex -> list of (neighbor, weight)
    graph = {
        0: [(1, 10), (2, 5)],
        1: [(2, 2)],
        2: []
    }
    
    print("Weighted Graph (Adj List):")
    for u, neighbors in graph.items():
        print(f"Vertex {u} connects to:")
        for v, w in neighbors:
            print(f"  -> {v} with weight {w}")

if __name__ == "__main__":
    weighted_graph_demo()
