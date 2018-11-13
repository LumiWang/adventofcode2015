
gifts = list()
with open("input.txt") as file:
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
                print("{} ### {} ### {}".format(first_group, second_group, last))


