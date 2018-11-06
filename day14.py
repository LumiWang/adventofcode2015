
def count_distance(run_time, wait_time, speed, t_all):
    T = run_time + wait_time
    total_distance = 0
    d = t_all // T
    p = t_all % T
    total_distance += d * run_time * speed
    if p > run_time:
        total_distance += run_time * speed
    else:
        total_distance += p * speed
    return total_distance

# print(count_distance(run_time, wait_time, speed, 1000))

deers = dict()
with open("input_day14.txt") as file:
    lines = file.readlines()
    for line in lines:
        line.strip()
        if line.split(" ")[0] not in deers:
            deers[line.split(" ")[0]] = dict()
            deers[line.split(" ")[0]]["speed"] = int(line.split(" ")[3])
            deers[line.split(" ")[0]]["run_time"] = int(line.split(" ")[6])
            deers[line.split(" ")[0]]["wait_time"] = int(line.split(" ")[-2])

print(deers)


def deers_run(deers, t_all):
    travelled_distance = dict()
    for deer in sorted(deers.keys()):
        travelled_distance[deer] = 0
        run_time = deers[deer]["run_time"]
        wait_time = deers[deer]["wait_time"]
        speed = deers[deer]["speed"]
        travelled_distance[deer] = count_distance(run_time, wait_time, speed, t_all=t_all)
    return travelled_distance

# travelled_distance = {'Vixen': 2660, 'Donner': 2660, 'Rudolph': 2637, 'Prancer': 2550, 'Blitzen': 2565, 'Comet': 2639, 'Cupid': 2550, 'Dasher': 2590, 'Dancer': 2292}


def find_leading_deer(travelled_distance):
    leading_deers = list()
    max_distance = max(travelled_distance.values())
    for deer in travelled_distance:
        if travelled_distance[deer] == max_distance:
            leading_deers.append(deer)
    return leading_deers

# print(find_leading_deer(travelled_distance))


deer_points = dict()
for deer in sorted(deers.keys()):
    deer_points[deer] = 0
i = 0
while i <= 2503:
    i += 1
    travelled_distance = deers_run(deers, i)
    leading_deers = find_leading_deer(travelled_distance)
    for deer in leading_deers:
        deer_points[deer] += 1
print(deer_points)

