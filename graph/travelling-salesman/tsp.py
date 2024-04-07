import math

def distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor(current_city, unvisited_cities):
    # Find the nearest unvisited city from the current city
    min_dist = float('inf')
    nearest_city = None
    for city in unvisited_cities:
        dist = distance(current_city, city)
        if dist < min_dist:
            min_dist = dist
            nearest_city = city
    return nearest_city, min_dist

def tsp(cities, cost_per_move=1):
    start_city = cities[0]
    current_city = start_city
    visited_cities = [start_city]
    unvisited_cities = cities[1:]

    steps = [(f"Start from city {start_city}", start_city)]

    total_cost = 0

    while unvisited_cities:
        nearest, dist = nearest_neighbor(current_city, unvisited_cities)
        visited_cities.append(nearest)
        unvisited_cities.remove(nearest)
        current_city = nearest
        total_cost += dist * cost_per_move
        steps.append((f"Move to city {nearest} (Cost: {dist * cost_per_move})", nearest))

    # Return to the starting city
    visited_cities.append(start_city)
    steps.append((f"Return to city {start_city}", start_city))

    # Calculate total distance
    total_distance = sum(distance(visited_cities[i], visited_cities[i+1]) for i in range(len(visited_cities)-1))

    return visited_cities, total_distance, total_cost, steps

# Example usage:
cities = [(0, 0), (1, 2), (3, 1), (5, 3)]  # Coordinates of cities
cost_per_move = 1  # Cost per move
optimal_path, total_distance, total_cost, steps = tsp(cities, cost_per_move)

print("Step-by-Step Process:")
for step, city in steps:
    print(step)

print("\nOptimal Path:", optimal_path)
print("Total Distance:", total_distance)
print("Total Cost:", total_cost)