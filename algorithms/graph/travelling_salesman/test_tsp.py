import numpy as np

class Node:
    def __init__(self, level, path, bound, cost):
        self.level = level
        self.path = path
        self.bound = bound
        self.cost = cost

def tsp_branch_and_bound(costs):
    # Initialize variables
    cities = list(costs.keys())
    n = len(cities)
    stack = []
    all_paths = []
    
    # Initialize with a dummy node at level 0
    root = Node(0, ['A'], 0, 0)
    stack.append(root)
    
    # Main loop of the algorithm
    while stack:
        current_node = stack.pop()
        current_level = current_node.level
        
        # Check if all cities have been visited
        if current_level == n - 1:
            current_path = current_node.path
            current_cost = current_node.cost + costs[current_path[-1]][current_path[0]] # Add return to the starting city
            
            # Store the path and cost
            all_paths.append((current_path, current_cost))
            print("{}: Path: {} → {} Cost: {}".format(len(all_paths), ' → '.join(current_path), current_path[0], current_cost))
            continue
        
        # Generate children for the current node
        for city in cities:
            if city not in current_node.path:
                child_path = current_node.path + [city]
                child_cost = current_node.cost + costs[current_node.path[-1]][city]
                child_bound = calculate_bound(child_path, costs)
                # Prune nodes if the lower bound exceeds current best solution
                if not all_paths or child_bound < min(path_cost for _, path_cost in all_paths):
                    child_node = Node(current_level + 1, child_path, child_bound, child_cost)
                    stack.append(child_node)
    
    return all_paths

def calculate_bound(path, costs):
    # Calculate the bound for a given path
    bound = 0
    last_city = path[-1]
    for city in costs:
        if city not in path:
            bound += min(costs[last_city][adj_city] for adj_city in costs[last_city] if adj_city not in path)
    bound += min(costs[last_city][path[0]], costs[path[-1]][path[0]])  # Add the return cost to the starting city
    return bound

# Define the costs dictionary
costs = {
    'A': {'A': np.inf, 'B': 4, 'C': 12, 'D': 7},
    'B': {'A': 5, 'B': np.inf, 'C': np.inf, 'D': 18},
    'C': {'A': 11, 'B': np.inf, 'C': np.inf, 'D': 6},
    'D': {'A': 10, 'B': 2, 'C': 3, 'D': np.inf}
}

# Call the function with the defined costs
all_paths = tsp_branch_and_bound(costs)
