"""Non recursive implementation of a DFS algorithm."""

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        """
        Add an edge between vertices u and v.
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append(v)

    def DFS(self, start):
        """
        Perform Depth-First Search traversal starting from the given vertex using a stack.
        """
        stack = [start]  # Initialize stack with the starting vertex
        visited = set()  # Set to keep track of visited vertices

        while stack:
            # Pop the top vertex from the stack
            vertex = stack.pop()
            # If the vertex has not been visited yet
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                print("Visited:", vertex)

                # Push unvisited neighbors onto the stack
                if vertex in self.adjacency_list:
                    for neighbor in reversed(self.adjacency_list[vertex]):
                        if neighbor not in visited:
                            stack.append(neighbor)


# Example usage:
G = {
    "A": ["B", "C", "D"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "D"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}

# Create an instance of the Graph class
graph = Graph()

# Add edges to the graph
for vertex, neighbors in G.items():
    for neighbor in neighbors:
        graph.add_edge(vertex, neighbor)

# Perform Depth-First Search starting from vertex "A"
print("Depth-First Search:")
graph.DFS("A")
