import heapq

def dijkstra(graph, source):
    dist = {vertex: float('inf') for vertex in graph}
    prev = {vertex: None for vertex in graph}
    dist[source] = 0

    pq = [(0, source)]  # Priority queue to store (distance, vertex) pairs

    while pq:
        current_dist, current_vertex = heapq.heappop(pq)

        if current_dist > dist[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            alt = current_dist + weight
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current_vertex
                heapq.heappush(pq, (alt, neighbor))

    return dist, prev