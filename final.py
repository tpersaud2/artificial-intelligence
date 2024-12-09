coordinates = {
    "Hagan Center": (40.68584341545361, -73.62765348050581),
    "Kellenberg Hall": (40.68603236195549, -73.62620208738565),
    "Casey Center": (40.686891887881494, -73.62664564824905),
    "Siena Hall": (40.687102094897476, -73.6272256375704),
    "Wilbur Arts Center": (40.687237044508734, -73.62592901997263),
    "Public Square": (40.68639138598025, -73.6274092125621)
}

def manhattan_distance(lat1, lon1, lat2, lon2):
    lat_diff = abs(lat1 - lat2) * 111139
    lon_diff = abs(lon1 - lon2) * 111139 * abs(math.cos(math.radians(lat1)))
    return lat_diff + lon_diff

import math

distances = {}
for building1, coords1 in coordinates.items():
    for building2, coords2 in coordinates.items():
        if building1 != building2:
            lat1, lon1 = coords1
            lat2, lon2 = coords2
            distance = manhattan_distance(lat1, lon1, lat2, lon2)
            distances[(building1, building2)] = distance

walking_speed = 1.2

times = {pair: distance / walking_speed for pair, distance in distances.items()}

print(distances)
print(times)
