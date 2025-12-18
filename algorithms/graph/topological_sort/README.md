# Topological Sort

## What is it?
**Topological Sort** for a Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge `u -> v`, vertex `u` comes before vertex `v` in the ordering.

**Note**: Topological Sort is not possible if the graph is not a DAG (i.e., if it contains a cycle).

## How it works
This implementation uses Detail-First Search (DFS).
1.  Call DFS for the graph.
2.  In the recursive function, once all adjacent vertices of a node are processed (i.e., visited), push the node to a stack.
3.  Finally, pop elements from the stack to get the topological order.

## Complexity
- **Time**: **O(V + E)**, where V is the number of vertices and E is the number of edges.
- **Space**: **O(V)** for the stack and recursion.

## Applications
- Scheduling tasks (e.g., build systems like Make or Ant).
- Course prerequisites resolution.
- Data serialization.

## Example Usage
```bash
python3 topological_sort.py
```
