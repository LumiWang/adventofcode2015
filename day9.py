
# build a map with all cities
map = dict()

with open("input_day9.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        city1 = line.split(" ")[0]
        city2 = line.split(" ")[2]
        distance = int(line.split(" ")[-1])
        if city1 not in map:
            map[city1] = dict()
        if city2 not in map:
            map[city2] = dict()

        if city2 not in map[city1]:
            map[city1][city2] = distance
        if city1 not in map[city2]:
            map[city2][city1] = distance

# print(map)

cities = sorted(map.keys())

# get all the permutations of cities
import itertools
permutations = itertools.permutations(cities)

# find minimum length
max_length = 0
for i in range(0, len(cities) - 1):
    max_length += map[cities[i]][cities[i+1]]
# print(min_length)
for permutation in permutations:
    # print(permutation)
    length = 0
    for i in range(0, len(permutation) - 1):
        length += map[permutation[i]][permutation[i+1]]
    if length > max_length:
        max_length = length

print(max_length)

