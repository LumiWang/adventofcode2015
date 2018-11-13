
# The original day24 way is too brute force, and cannot handle 28 packages.
gifts = list()
with open("input_day24.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        gifts.append(int(line))

print(gifts)
print(len(gifts))

# get the balanced weight:
weight = sum(gifts) / 4
print(weight)

# the first cart must have only 5 items to get a total weight 508
# because the 4 largest items cannot reach the target weight
# so the question becomes:
# pick 5 items out of the list that sums up to 508
# and find one senario with the smallest product

import itertools

senarios = list()

for item in list(itertools.combinations(gifts, 4)):
    if sum(item) == weight:
        senarios.append(item)
print(senarios)

# this is getting interesting:
# results show that no 5 objects can sum up to 508
# so i need 6 objects:

for item in list(itertools.combinations(gifts, 5)):
    if sum(item) == weight:
        senarios.append(item)
print(senarios)

# now find the group with smallest production
min_production = 113 * 109 * 107 * 103 * 101 * 97
for item in senarios:
    product = 1
    for num in item:
        product *= num
    if product < min_production:
        min_production = product

print(min_production)

