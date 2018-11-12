
SIZE = 6
lights = list()

def print_pretty(lights):
    for item in lights:
        print(item)

with open("input_day18.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        lights.append(list(line))

print_pretty(lights)

def get_all_neighbors(lights, location):
    # location in (i, j) tuple
    neighbors = list()
    on_num = 0
    for i in range(location[0]-1, location[0] + 2):
        if i < 0 or i >= len(lights):
            pass
        else:
            for j in range(location[1]-1, location[1] + 2):
                if j < 0 or j >= len(lights[0]):
                    pass
                else:
                    if i == location[0] and j == location[1]:
                        pass
                    else:
                        neighbor = lights[i][j]
                        neighbors.append(neighbor)
                        if neighbor == "#":
                            on_num += 1

    return on_num


# print(get_all_neighbors(lights, (5, 1)))


def turn_on_or_off(lights, location):
    on_num = get_all_neighbors(lights, location)
    # print("neighbors that are on: {}".format(on_num))
    # print("The location is currently: {}".format(lights[location[0]][location[1]]))
    if location == (0, len(lights)-1) or location == (0, 0) or location == (len(lights) - 1 , 0) or location == (len(lights) - 1, len(lights) - 1):
        return "#"
    else:
        if lights[location[0]][location[1]] == ".":
            if on_num == 3:
                return "#"
            else:
                return "."
        else:
            if on_num in (2, 3):
                return "#"
            else:
                return "."


# print(turn_on_or_off(lights, (0, 2)))


def lights_after_one_sec(lights):
    new_lights = list()  # THings learnt: list_a.copy() makes only a new reference, pointing to the same object.
    for i in range(0, len(lights)):
        new_lights.append(list())
        for j in range(0, len(lights[i])):
            new_lights[i].append("")

    for i in range(0, len(lights)):
        for j in range(0, len(lights[i])):
            new_lights[i][j] = turn_on_or_off(lights, (i, j))

    return new_lights

print()


def count_on_lights(lights):
    on_lights = 0
    for i in range(0, len(lights)):
        for j in range(0, len(lights[i])):
            if lights[i][j] == "#":
                on_lights += 1
    return on_lights
# print_pretty(lights_after_one_sec(lights))

TIME = 100
for t in range(0, TIME):
    lights = lights_after_one_sec(lights)
    # print_pretty(lights)
    # print()

print(count_on_lights(lights))

