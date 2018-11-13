
gifts = list()
with open("input_day24.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        gifts.append(int(line))

print(gifts)
print(len(gifts))
total_gifts = len(gifts)
import itertools

# total gifts are 28,
# so the extreme way of splitting would be 1, 1, 26

all_combinations = list()
for i in range(1, total_gifts-1):
    for first_group in list(itertools.combinations(gifts, i)):
        rest = gifts.copy()
        for item in first_group:
            rest.remove(item)
        for j in range(1, total_gifts - i):
            for second_group in list(itertools.combinations(rest, j)):
                last = rest.copy()
                for item in second_group:
                    last.remove(item)
                # print("{} ### {} ### {}".format(list(first_group), list(second_group), last))
                all_combinations.append((list(first_group), list(second_group), last))


print(len(all_combinations))

# deliminate those that doens't balance:
balanced_combinations = list()
for combination in all_combinations:
    if sum(combination[0]) == sum(combination[1]):
        if sum(combination[1]) == sum(combination[2]):
            balanced_combinations.append(combination)
print(len(balanced_combinations))

# get rid of the same combinations:
uniq_combinations = list()
for item in balanced_combinations:
    set_item = set()
    for i in range(3):
        set_item.add(tuple(item[i]))
    if set_item not in uniq_combinations:
        uniq_combinations.append(set_item)
print(len(uniq_combinations))

# arrange the three carts, so that the one with least item is in the front
# if there are multiple carts with the same number of items,
# the one with smallest quantum entanglement will be at front
arranged_combinations = list()
for item in uniq_combinations:
    # print(item)
    combination = sorted(list(item), key=lambda x: (len(x), itertools.product(x)))
    print(combination)



