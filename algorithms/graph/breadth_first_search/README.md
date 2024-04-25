# Breadth-First Search (BFS)

BFS is a graph traversal algorithm used to systematically traverse or search a graph. It employs a **queue data structure**, utilizing the First In, First Out (FIFO) method for data processing and management. In BFS, you explore all neighbors of a node before moving to the next level, resulting in a **breadth-first traversal**. The total running time for Breadth First Search is **O(V+E)**. Graph traversal, pathfinding, cycle detection, topological sorting, connected components, and more are among its applications.

![Breadth-First Search](https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif)

## Pseudocode

```markdown
BFS(V, E, s):

Input:
- V: Set of vertices
- E: Set of edges
- s: Starting vertex

Variables:
- V: Set of vertices in the graph
- E: Set of edges in the graph
- s: Starting vertex for BFS traversal
- color: Array to store the color of each vertex (WHITE, GREY, BLACK)
- d: Array to store the distance of each vertex from the starting vertex
- π: Array to store the parent of each vertex
- Q: Queue data structure for BFS traversal

Initialization:
- For each vertex v in V - {s}:
  - Set color[v] to WHITE          // Mark all vertices as unvisited
  - Set d[v] to ∞                  // Set distance from starting vertex to infinity
  - Set π[v] to NIL                // Set parent of each vertex to null
- Set color[s] to GREY             // Mark the starting vertex as visited
- Set d[s] to 0                    // Set distance of the starting vertex to 0
- Set π[s] to NIL                  // Set parent of the starting vertex to null
- Create an empty queue Q           // Initialize a queue for BFS traversal

Algorithm:
- ENQUEUE(Q, s)                    // Enqueue the starting vertex
- While Q is non-empty:
  - Dequeue a vertex v from Q      // Take the next vertex from the queue
  - For each vertex u adjacent to v:
    - If color[u] is WHITE:        // If the adjacent vertex is unvisited
      - Set color[u] to GREY       // Mark it as visited
      - Set d[u] to d[v] + 1       // Update its distance from the starting vertex
      - Set π[u] to v              // Set its parent to the current vertex
      - ENQUEUE(Q, u)              // Enqueue the adjacent vertex for further exploration
  - Set color[v] to BLACK          // Mark the current vertex as fully explored
```

Given a set of vertices (V), edges (E), and a starting vertex (s), BFS initializes variables to track visited vertices, distances, and parents. It begins by enqueueing the starting vertex and iteratively explores adjacent unvisited vertices level by level, recording their distances from the starting vertex. The process continues until all vertices are visited.

To put it simply,

```markdown
BFS(G, start):
    queue = new Queue()                // Initialize a queue
    queue.enqueue(start)               // Enqueue the starting vertex
    while queue is not empty:          // While there are vertices in the queue
        current = queue.dequeue()      // Dequeue a vertex
        mark current as visited        // Mark the current vertex as visited
        for each neighbor u of current:
            if u is not visited:       // If the neighbor is unvisited
                queue.enqueue(u)       // Enqueue the neighbor for further exploration
```

## Resources
* [BFS Visualization](https://www.cs.usfca.edu/~galles/visualization/BFS.html)
* [More Notes](https://www.gatevidyalay.com/breadth-first-search-bfs-algorithm/)