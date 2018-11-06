
map = dict()
with open("input_day13.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = line.strip(".")
        if line.split(" ")[0] not in map:
            map[line.split(" ")[0]] = dict()
        if line.split(" ")[-1] not in map[line.split(" ")[0]]:
            if "gain" in line:
                map[line.split(" ")[0]][line.split(" ")[-1]] = int(line.split(" ")[3])
            else:
                map[line.split(" ")[0]][line.split(" ")[-1]] = 0 - int(line.split(" ")[3])
print(map)

print("########")

map_with_me = map
# print(map_with_me)
for key in map_with_me:
    map_with_me[key]["Lumi"] = 0
map_with_me["Lumi"] = dict()
for key in map_with_me:
    if key != "Lumi":
        map_with_me["Lumi"][key] = 0
print(map_with_me["Lumi"])

print("########")

import itertools

atendees = sorted(map.keys())
print(atendees)

max_happiness = 0

for sequence in itertools.permutations(atendees):
    happiness = 0
    # print(sequence)
    adjusted_sequence = list()
    adjusted_sequence.append(sequence[-1])
    for atendee in sequence:
        adjusted_sequence.append(atendee)
    adjusted_sequence.append(sequence[0])

    for i in range(1, len(atendees)+1):
        happiness += map[adjusted_sequence[i]][adjusted_sequence[i-1]]
        happiness += map[adjusted_sequence[i]][adjusted_sequence[i + 1]]
    # print(happiness)
    if happiness > max_happiness:
        max_happiness = happiness

print(max_happiness)
