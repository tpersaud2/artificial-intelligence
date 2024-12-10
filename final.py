import math
from itertools import permutations

# Coordinates of Molloy buildings from Google Maps
coordinates = {
    "Hagan Center": (40.68584341545361, -73.62765348050581),
    "Kellenberg Hall": (40.68603236195549, -73.62620208738565),
    "Casey Center": (40.686891887881494, -73.62664564824905),
    "Siena Hall": (40.687102094897476, -73.6272256375704),
    "Wilbur Arts Center": (40.687237044508734, -73.62592901997263),
    "Public Square": (40.68639138598025, -73.6274092125621)
}

# Function to calculate Manhattan Distance between two buildings
def manhattan_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to meters (approximate)
    lat_diff = abs(lat1 - lat2) * 111139  # 1 degree latitude is ~111,139 meters
    lon_diff = abs(lon1 - lon2) * 111139 * abs(math.cos(math.radians(lat1)))  # Adjust longitude for latitude
    return lat_diff + lon_diff

# Calculate distances for all possible pairs of buildings
distances = {}
for building1, coords1 in coordinates.items():
    for building2, coords2 in coordinates.items():
        if building1 != building2:
            lat1, lon1 = coords1
            lat2, lon2 = coords2
            distance = manhattan_distance(lat1, lon1, lat2, lon2)
            distances[(building1, building2)] = distance

# Average walking speed (1.2 meters per second)
walking_speed = 1.2

# Calculate the time for each pair (time = distance / speed)
times = {pair: distance / walking_speed for pair, distance in distances.items()}

# Function to find the shortest route using TSP logic
def find_shortest_route_tsp(start, buildings_to_visit, walking_times):
    # Include the starting building in the list of buildings to visit
    all_buildings = [start] + buildings_to_visit
    shortest_time = float("inf")
    best_route = []

    # Generate all permutations of the buildings to visit (excluding the starting point)
    for perm in permutations(buildings_to_visit):
        # Build the route by adding the starting point at the beginning
        route = [start] + list(perm)
        total_time = 0

        # Calculate the total time for this route
        valid_route = True
        for i in range(len(route) - 1):
            start_building = route[i]
            end_building = route[i + 1]
            if (start_building, end_building) in walking_times:
                total_time += walking_times[(start_building, end_building)]
            elif (end_building, start_building) in walking_times:
                total_time += walking_times[(end_building, start_building)]
            else:
                valid_route = False
                break  # Invalid route, skip this permutation

        # Update the shortest route if this one is better
        if valid_route and total_time < shortest_time:
            shortest_time = total_time
            best_route = route

    return best_route, shortest_time

start_building = "Kellenberg Hall"

# Get the user's input for buildings to visit
print("Enter the names of the buildings you need to visit, separated by commas.")
print("Available buildings: " + ", ".join([b for b in coordinates.keys() if b != start_building]))
buildings_input = input("Buildings to visit: ").strip()
buildings_to_visit = [b.strip() for b in buildings_input.split(",") if b.strip() in coordinates]

invalid_buildings = [b for b in buildings_to_visit if b not in coordinates]
if invalid_buildings:
    print(f"Invalid buildings in input: {', '.join(invalid_buildings)}")
else:
    # Find the shortest route
    shortest_route, shortest_time = find_shortest_route_tsp(start_building, buildings_to_visit, times)

    if not shortest_route:
        print("No valid route found.")
    else:
        print(f"\nShortest route starting from {start_building}: {' -> '.join(shortest_route)}")
        print(f"Total walking time: {shortest_time:.2f} seconds")
