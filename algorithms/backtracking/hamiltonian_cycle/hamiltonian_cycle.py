def is_safe(v, graph, path, pos):
    """
    Check if the current vertex can be added to the path.
    """
    # Check if this vertex is an adjacent vertex of the previously added vertex
    if graph[path[pos - 1]][v] == 0:
        return False

    # Check if the vertex has already been included
    for i in range(pos):
        if path[i] == v:
            return False

    return True

def ham_cycle_util(graph, path, pos):
    """
    Recursive utility function to solve Hamiltonian Cycle problem.
    """
    # Base case: If all vertices are included in the path
    if pos == len(graph):
        # And if there is an edge from the last included vertex to the first vertex
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # Try different vertices as a next candidate in Hamiltonian Cycle
    for v in range(1, len(graph)):
        if is_safe(v, graph, path, pos):
            path[pos] = v

            if ham_cycle_util(graph, path, pos + 1):
                return True

            # Backtrack
            path[pos] = -1

    return False

def hamiltonian_cycle(graph):
    """
    Solves the Hamiltonian Cycle problem using Backtracking.
    """
    path = [-1] * len(graph)
    
    # Let us put vertex 0 as the first vertex in the path.
    # If there is a Hamiltonian Cycle, then the path can be
    # started from any point of the cycle as the graph is undirected.
    path[0] = 0

    if not ham_cycle_util(graph, path, 1):
        print("Solution does not exist")
        return False

    print("Solution Exists: Following is one Hamiltonian Cycle")
    print(path + [path[0]]) # Print path + start vertex to show cycle
    return True

if __name__ == "__main__":
    # Example graph
    # (0)--(1)--(2)
    #  |   / \   |
    #  |  /   \  |
    #  | /     \ |
    # (3)-------(4)
    graph1 = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ]
    
    hamiltonian_cycle(graph1)
    
    graph2 = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
    ]
    print("\nGraph 2:")
    hamiltonian_cycle(graph2)
