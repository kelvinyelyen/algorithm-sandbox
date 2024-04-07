import heapq
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class DijkstraVisualizer:
    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.steps = self.run_dijkstra()
        self.current_step_index = 0

        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        plt.subplots_adjust(bottom=0.2)
        self.ax.set_title("Step 1: Initialize")
        
        self.G = nx.DiGraph()
        for vertex in self.graph.keys():
            self.G.add_node(vertex)
        for vertex, edges in self.graph.items():
            for neighbor, weight in edges.items():
                self.G.add_edge(vertex, neighbor, weight=weight)

        self.pos = nx.spring_layout(self.G)
        self.draw_graph()

        self.ax_next = plt.axes([0.7, 0.05, 0.1, 0.075])
        self.btn_next = Button(self.ax_next, 'Next')
        self.btn_next.on_clicked(self.next_step)

        self.ax_prev = plt.axes([0.1, 0.05, 0.1, 0.075])
        self.btn_prev = Button(self.ax_prev, 'Previous')
        self.btn_prev.on_clicked(self.prev_step)

        plt.show()

    def run_dijkstra(self):
        dist = {vertex: float('inf') for vertex in self.graph}
        prev = {vertex: None for vertex in self.graph}
        dist[self.source] = 0

        pq = [(0, self.source)]  # Priority queue to store (distance, vertex) pairs
        visited = set()
        unvisited = set(self.graph.keys())
        steps = []

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)
            if current_vertex not in unvisited:
                continue

            visited.add(current_vertex)
            unvisited.remove(current_vertex)
            steps.append((f"Choose vertex {current_vertex} (Distance: {current_dist})", visited.copy(), unvisited.copy()))

            for neighbor, weight in self.graph[current_vertex].items():
                alt = current_dist + weight
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = current_vertex
                    heapq.heappush(pq, (alt, neighbor))
                    steps.append((f"Update distance to vertex {neighbor} to {alt}", visited.copy(), unvisited.copy()))

        return steps

    def draw_graph(self):
        plt.cla()
        nx.draw(self.G, pos=self.pos, ax=self.ax, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', arrows=True)
        step, visited, unvisited = self.steps[self.current_step_index]
        self.ax.set_title(f"Step {self.current_step_index + 1}: {step}")
        nx.draw_networkx_nodes(self.G, pos=self.pos, nodelist=visited, node_color='red', node_size=500)
        nx.draw_networkx_nodes(self.G, pos=self.pos, nodelist=unvisited, node_color='blue', node_size=500)

    def next_step(self, event):
        self.current_step_index = min(self.current_step_index + 1, len(self.steps) - 1)
        self.draw_graph()

    def prev_step(self, event):
        self.current_step_index = max(self.current_step_index - 1, 0)
        self.draw_graph()

# Example usage:
graph = {
    '1': {'2': 1, '3': 5},
    '2': {'3': 2, '5': 1, '4': 2},
    '3': {'5': 2},
    '4': {'5': 3, '6': 1},
    '5': {'6': 2},
    '6': {}  # Empty dictionary for vertex 'e' since it has no outgoing edges
}

source = '1'
DijkstraVisualizer(graph, source)
