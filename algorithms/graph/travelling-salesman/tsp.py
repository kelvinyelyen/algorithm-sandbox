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
    return nearest_city

def tsp(cities):
    start_city = cities[0]
    current_city = start_city
    visited_cities = [start_city]
    unvisited_cities = cities[1:]

    while unvisited_cities:
        nearest = nearest_neighbor(current_city, unvisited_cities)
        visited_cities.append(nearest)
        unvisited_cities.remove(nearest)
        current_city = nearest

    # Return to the starting city
    visited_cities.append(start_city)

    # Calculate total distance
    total_distance = sum(distance(visited_cities[i], visited_cities[i+1]) for i in range(len(visited_cities)-1))

    return visited_cities, total_distance
