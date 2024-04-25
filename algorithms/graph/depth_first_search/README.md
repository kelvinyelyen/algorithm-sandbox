# Depth-First Search (DFS)

DFS is a graph traversal algorithm used to systematically traverse or search a graph. It employs a **stack data structure**, utilizing the Last In, First Out (LIFO) method for data processing and management, alternatively, DFS can be implemented using **recursion**, where the call stack of the programming language serves as the implicit stack. In DFS, exploration extends as deeply as possible along a branch before backtracking, resulting in a **depth-first traversal**. The total running time for Depth First Search is **θ (V+E)**. DFS can also be classified under uninformed search algorithms. Graph traversal, pathfinding, cycle detection, topological sorting, connected components, and more are among its applications.

![Depth-First Search](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

## Pseudocode

```markdown
DFS(V, E, s):

Input:
- V: Set of vertices
- E: Set of edges
- s: Starting vertex

Variables:
- V: Set of vertices in the graph
- E: Set of edges in the graph
- s: Starting vertex for DFS traversal
- color: Array to store the color of each vertex (WHITE, GREY, BLACK)
- π: Array to store the parent of each vertex
- time: Variable to keep track of the current time during DFS traversal

Initialization:
- For each vertex v in V:
  - Set color[v] to WHITE          // Mark all vertices as unvisited
  - Set π[v] to NIL                // Set parent of each vertex to null
- time ← 0                          // Initialize time variable

Algorithm:
- For each vertex v in V:
  - If color[v] is WHITE:          // If vertex v is unvisited
    - Depth_First_Search(v)        // Start DFS from vertex v

Depth_First_Search(v):
- Set color[v] to GREY             // Mark vertex v as visited
- Increment time by 1               // Increment time
- Set d[v] to time                  // Set discovery time for vertex v
- For each vertex u adjacent to v:
  - If color[u] is WHITE:          // If vertex u is unvisited
    - Set π[u] to v                // Set parent of vertex u to v
    - Depth_First_Search(u)        // Recursively explore vertex u
- Set color[v] to BLACK            // Mark vertex v as finished
- Increment time by 1               // Increment time
- Set f[v] to time                  // Set finishing time for vertex v
```

The algorithm takes a set of vertices (V), a set of edges (E), and a starting vertex (s) as input. The algorithm initializes variables to keep track of visited vertices, parent pointers, and time. It then explores each vertex in V, starting from the given starting vertex (s). During exploration, it recursively visits adjacent unvisited vertices, marking them as visited and updating parent pointers. Finally, it marks the current vertex as finished. This process continues until all vertices are visited.

To put it simply,

### DFS with Recursion:

```markdown
DFS(G, v):
    mark v as visited
    for each neighbor u of v:
        if u is not visited:
            DFS(G, u)
```

### DFS with Stack:

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
* [More Notes](https://www.gatevidyalay.com/depth-first-search-dfs-algorithm/)