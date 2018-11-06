
map = dict()
with open("input_day15.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        ingredient = line.split(" ")[0][:-1]
        if ingredient not in map:
            map[ingredient] = dict()
        map[ingredient]["capacity"] = int(line.split(" ")[2][:-1])
        map[ingredient]["durability"] = int(line.split(" ")[4][:-1])
        map[ingredient]["flavor"] = int(line.split(" ")[6][:-1])
        map[ingredient]["texture"] = int(line.split(" ")[8][:-1])
        map[ingredient]["calories"] = int(line.split(" ")[-1])

# print(map)

import itertools
import collections

ingredients = sorted(map.keys())
max_score = 0
max_combination = ""
for item in itertools.combinations_with_replacement(ingredients, 100):
    total_score = 0
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    # print(item)
    c = collections.Counter(item)
    # print(c)
    for ingredient in ingredients:
        capacity += c[ingredient] * map[ingredient]["capacity"]
        durability += c[ingredient] * map[ingredient]["durability"]
        flavor += c[ingredient] * map[ingredient]["flavor"]
        texture += c[ingredient] * map[ingredient]["texture"]
        calories += c[ingredient] * map[ingredient]["calories"]

    if capacity <= 0:
        continue
    elif durability <= 0:
        continue
    elif flavor <= 0:
        continue
    elif texture <= 0:
        continue
    else:
        # print(capacity)
        # print(durability)
        # print(flavor)
        # print(texture)
        if calories == 500:
            total_score = capacity * durability * flavor * texture
            if total_score > max_score:
                max_score = total_score
                max_combination = c

print(max_score)
print(max_combination)