class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list representation of the graph
        self.graph = {}

    def add_edge(self, u, v):
        """
        Add an edge between vertices u and v.
        """
        # If vertex u is not already in the graph, add it with an empty list as its value
        if u not in self.graph:
            self.graph[u] = []
        # Add vertex v to the adjacency list of vertex u
        self.graph[u].append(v)

    def DFS(self, start):
        """
        Perform Depth-First Search traversal starting from the given vertex.
        """
        # Initialize a set to keep track of visited vertices
        visited = set()

        def dfs_util(vertex):
            """
            Utility function for DFS traversal.
            """
            # Mark the current vertex as visited
            visited.add(vertex)
            print("Visited:", vertex)

            # Visit all adjacent vertices recursively
            if vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        dfs_util(neighbor)

        # Start DFS traversal from the given vertex
        dfs_util(start)


# Example usage:
g = Graph()

# Add edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Perform DFS traversal starting from vertex 2
print("Depth-First Search:")
g.DFS(2)
