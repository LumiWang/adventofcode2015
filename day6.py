
# part 1

# initiate a grid with all 0 = OFF
grid = []
size = 1000
for i in range(0, size):
    grid.append(list())
    for j in range(0, size):
        grid[i].append(0)

# print(grid)

# tuple1 = (0, 0)
# tuple2 = (4, 0)


def turn_on(grid, tuple1, tuple2):
    vertical_start = tuple1[1]
    vertical_end = tuple2[1]
    horiz_start = tuple1[0]
    horiz_end = tuple2[0]
    for i in range(vertical_start, vertical_end + 1):
        for j in range(horiz_start, horiz_end + 1):
            grid[i][j] = 1


def turn_off(grid, tuple1, tuple2):
    vertical_start = tuple1[1]
    vertical_end = tuple2[1]
    horiz_start = tuple1[0]
    horiz_end = tuple2[0]
    for i in range(vertical_start, vertical_end + 1):
        for j in range(horiz_start, horiz_end + 1):
            grid[i][j] = 0


def toggle(grid, tuple1, tuple2):
    vertical_start = tuple1[1]
    vertical_end = tuple2[1]
    horiz_start = tuple1[0]
    horiz_end = tuple2[0]
    for i in range(vertical_start, vertical_end + 1):
        for j in range(horiz_start, horiz_end + 1):
            if grid[i][j] == 1:
                grid[i][j] = 0
            else:
                grid[i][j] = 1


def count_on(grid):
    ons = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1:
                ons += 1
    return ons


# turn_on(grid, tuple1, tuple2)
# print(grid)
# print(count_on(grid))
# turn_off(grid, tuple1, tuple2)
# print(grid)
# toggle(grid, tuple1, tuple2)
# print(grid)

with open("input_day6.txt", "r") as file:
    inputs = file.readlines()
    for input in inputs:
        if input.split(" ")[1] == "on":
            tuple1 = (int(input.split(" ")[2].split(",")[0]), int(input.split(" ")[2].split(",")[1]))
            tuple2 = (int(input.split(" ")[4].split(",")[0]), int(input.split(" ")[4].split(",")[1]))
            turn_on(grid, tuple1, tuple2)
        elif input.split(" ")[1] == "off":
            tuple1 = (int(input.split(" ")[2].split(",")[0]), int(input.split(" ")[2].split(",")[1]))
            tuple2 = (int(input.split(" ")[4].split(",")[0]), int(input.split(" ")[4].split(",")[1]))
            turn_off(grid, tuple1, tuple2)
        elif input.split(" ")[0] == "toggle":
            tuple1 = (int(input.split(" ")[1].split(",")[0]), int(input.split(" ")[1].split(",")[1]))
            tuple2 = (int(input.split(" ")[3].split(",")[0]), int(input.split(" ")[3].split(",")[1]))
            toggle(grid, tuple1, tuple2)
        else:
            raise Exception("Wrong command. shouldn't happen.")
    print(count_on(grid))
