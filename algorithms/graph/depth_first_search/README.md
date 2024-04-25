# Depth-First Search (DFS)

DFS is a graph traversal algorithm used to systematically traverse or search a graph. It employs a **stack data structure**, utilizing the Last In, First Out (LIFO) method for data processing and management, alternatively, DFS can be implemented using **recursion**, where the call stack of the programming language serves as the implicit stack. In DFS, exploration extends as deeply as possible along a branch before backtracking, resulting in a **depth-first traversal**. The total running time for Depth First Search is **θ (V+E)**. Graph traversal, pathfinding, cycle detection, topological sorting, connected components, and more are among its applications.

![Depth-First Search](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

## Pseudocode

```markdown
DFS(G, v):
    for each vertex u in V[G]:
        color[v] ← WHITE          // Mark all vertices as unvisited
        π[v] ← NIL                // Set parent of each vertex to null
    time ← 0                      // Initialize time variable
    for each vertex v in V[G]:
        if color[v] = WHITE:      // If vertex v is unvisited
            Depth_First_Search(v) // Start DFS from vertex v

Depth_First_Search(v):
    color[v] ← GRAY              // Mark vertex v as visited
    time ← time + 1              // Increment time
    d[v] ← time                  // Set discovery time for vertex v
    for each vertex u adjacent to v:
        if color[u] = WHITE:     // If vertex u is unvisited
            π[u] ← v              // Set parent of vertex u to v
            Depth_First_Search(u) // Recursively explore vertex u
    color[v] ← BLACK             // Mark vertex v as finished
    time ← time + 1              // Increment time
    f[v] ← time                  // Set finishing time for vertex v
```

The algorithm involves marking vertices as visited, exploring each vertex and its neighbors, and optionally recording discovery and finishing times.

To put it simply:

```markdown
DFS(G, v):
    mark v as visited
    for each neighbor u of v:
        if u is not visited:
            DFS(G, u)
```

DFS with Stack:

```markdown
DFS(G, start):
    stack = new Stack()
    stack.push(start)
    while stack is not empty:
        current = stack.pop()
        if current is not visited:
            mark current as visited
            for each neighbor u of current:
                if u is not visited:
                    stack.push(u)
```

## Resources
* [DFS Visualization](https://www.cs.usfca.edu/~galles/visualization/DFS.html)