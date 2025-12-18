from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        """
        Recursive helper function for topological sort.
        """
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    def topological_sort(self):
        """
        The main function to do Topological Sort.
        """
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        # Print contents of the stack in reverse
        print(stack[::-1])
        return stack[::-1]

if __name__ == "__main__":
    # Create a graph given in the above diagram
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Following is a Topological Sort of the given graph:")
    g.topological_sort()
    # Expected: 5 4 2 3 1 0 (or similar valid ordering)
