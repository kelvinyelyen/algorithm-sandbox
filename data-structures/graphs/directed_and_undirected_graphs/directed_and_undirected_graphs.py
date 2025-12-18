def graph_demo():
    # Directed Graph: Edges have direction
    # 0 -> 1
    directed = {0: [1], 1: []}
    
    # Undirected Graph: Edges are bidirectional
    # 0 -- 1
    undirected = {0: [1], 1: [0]}
    
    print("Directed:", directed)
    print("Undirected:", undirected)

if __name__ == "__main__":
    graph_demo()
