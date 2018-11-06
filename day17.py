containers = list()

with open("input_day17.txt") as file:
    lines = file.readlines()
    for line in lines:
        containers.append(int(line.strip()))

print(containers)

import itertools
num_of_containers = len(containers)
print(num_of_containers)
all_combinations = list()

for i in range(1, num_of_containers+1):
    all_combinations.extend(list(itertools.combinations(containers, i)))

answer1 = 0
fits_dict = dict()
for i in range(0, len(all_combinations)):
    # print(all_combinations[i])
    total_amount = sum(all_combinations[i])
    if total_amount == 150:
        answer1 += 1
        num_containers = len(all_combinations[i])
        if num_containers not in fits_dict:
            fits_dict[num_containers] = 0
        fits_dict[num_containers] += 1

print(answer1)
print(fits_dict)