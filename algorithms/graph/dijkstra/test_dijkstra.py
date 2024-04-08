import heapq


def dijkstra(graph, source):
    dist = {vertex: float('inf') for vertex in graph}
    prev = {vertex: None for vertex in graph}
    dist[source] = 0

    pq = [(0, source)]  # Priority queue to store (distance, vertex) pairs
    visited = []  # Changed to list to maintain the order of visit
    unvisited = set(graph.keys())
    steps = []

    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        if current_vertex not in unvisited:
            continue

        # Appending to the list to maintain order
        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        steps.append(
            (f"Choose vertex {current_vertex} (Distance: {current_dist})", visited.copy(), unvisited.copy()))

        for neighbor, weight in graph[current_vertex].items():
            alt = current_dist + weight
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current_vertex
                heapq.heappush(pq, (alt, neighbor))
                steps.append(
                    (f"Update distance to vertex {neighbor} to {alt}", visited.copy(), unvisited.copy()))

    return dist, prev, steps, visited


# Example graph represented as an adjacency list
graph = {
    '1': {'2': 1, '3': 5},
    '2': {'3': 2, '5': 1, '4': 2},
    '3': {'5': 2},
    '4': {'5': 3, '6': 1},
    '5': {'6': 2},
    '6': {}  # Empty dictionary for vertex 'e' since it has no outgoing edges
}

source = '1'
shortest_distances, predecessors, steps, visited = dijkstra(graph, source)

print("Step-by-Step Process:")
for i, (step, visited_step, unvisited) in enumerate(steps):
    print(f"Step {i + 1}: {step}")
    print("Visited:", visited_step)
    print("Unvisited:", unvisited)
    print()

print("\nOrder of visit:", visited)
print("\nShortest distances from source vertex", source, ":")
print(shortest_distances)
print("Predecessors:")
print(predecessors)
