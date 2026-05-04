import sys

def nearest_neighbor_tsp(distances):
    n = len(distances)
    visited = set([0])
    tour = [0]
    current = 0
    total = 0

    while len(visited) < n:
        next_city = None
        min_dist = sys.maxsize

        for i in range(n):
            if i not in visited and distances[current][i] < min_dist:
                next_city = i
                min_dist = distances[current][i]

        tour.append(next_city)
        visited.add(next_city)
        total += min_dist
        current = next_city

    tour.append(0)
    total += distances[current][0]

    print("Tour:", tour)
    print("Distance:", total)


distances = [
    [0,4,8,9,12],
    [4,0,6,8,9],
    [8,6,0,10,11],
    [9,8,10,0,7],
    [12,9,11,7,0]
]

nearest_neighbor_tsp(distances)
