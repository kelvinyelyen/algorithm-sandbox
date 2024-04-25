# Import deque from collections module for efficient queue implementation
from collections import deque


class Graph:
    def __init__(self):
        """
        Initialize a graph object with an empty adjacency list.
        """
        self.graph = {}

    def add_edge(self, u, v):
        """
        Add an edge between vertices u and v in the graph.
        """
        # If vertex u is not in the graph, add it with an empty list as its value
        if u not in self.graph:
            self.graph[u] = []
        # Add vertex v to the adjacency list of vertex u
        self.graph[u].append(v)

    def bfs(self, start):
        """
        Perform Breadth-First Search traversal starting from the given vertex.
        """
        visited = set()  # Initialize an empty set to keep track of visited vertices
        # Initialize a deque with the starting vertex as the first element
        queue = deque([start])

        # Iterate until the queue is empty
        while queue:
            vertex = queue.popleft()  # Dequeue a vertex from the left side of the deque
            # If the vertex has not been visited yet
            if vertex not in visited:
                print("Visited:", vertex)  # Print the visited vertex
                visited.add(vertex)  # Mark the vertex as visited
                # If the vertex has adjacent vertices
                if vertex in self.graph:
                    # Enqueue its unvisited neighbors
                    for neighbor in self.graph[vertex]:
                        if neighbor not in visited:
                            queue.append(neighbor)


# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Perform BFS traversal starting from vertex 2
print("Breadth-First Search:")
g.bfs(2)
