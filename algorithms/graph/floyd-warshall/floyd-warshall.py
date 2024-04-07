def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('inf')] * V for _ in range(V)]
    steps = []

    # Initialize distances for direct edges
    for u in range(V):
        dist[u][u] = 0
        for v in range(V):
            if graph[u][v] != float('inf'):
                dist[u][v] = graph[u][v]

    steps.append([row[:] for row in dist])

    # Update distances using all vertices as intermediate nodes
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        steps.append([row[:] for row in dist])

    return steps

# Example usage:
graph = [
    [0, 3, 8, float('inf'), -4],
    [float('inf'), 0, float('inf'), 1, 7],
    [float('inf'), 4, 0, float('inf'), float('inf')],
    [2, float('inf'), -5, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 6, 0]
]

steps = floyd_warshall(graph)

for i, step in enumerate(steps):
    print(f"Iteration {i + 1}:")
    for row in step:
        print(row)
    print()
