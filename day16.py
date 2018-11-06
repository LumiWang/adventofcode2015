aunts = dict()

with open("input_day16.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        aunt = line.split(" ")[1][:-1]
        if aunt not in aunts:
            aunts[aunt] = dict()
            aunts[aunt]["children"] = -1
            aunts[aunt]["cats"] = -1
            aunts[aunt]["samoyeds"] = -1
            aunts[aunt]["pomeranians"] = -1
            aunts[aunt]["akitas"] = -1
            aunts[aunt]["vizslas"] = -1
            aunts[aunt]["goldfish"] = -1
            aunts[aunt]["trees"] = -1
            aunts[aunt]["cars"] = -1
            aunts[aunt]["perfumes"] = -1
        aunts[aunt][line.split(" ")[2][:-1]] = int(line.split(" ")[3][:-1])
        aunts[aunt][line.split(" ")[4][:-1]] = int(line.split(" ")[5][:-1])
        aunts[aunt][line.split(" ")[6][:-1]] = int(line.split(" ")[-1])
# print(aunts)

for aunt in sorted(aunts.keys()):
    if aunts[aunt]["children"] != -1 and aunts[aunt]["children"] != 3:
        aunts.pop(aunt)
        continue
    elif aunts[aunt]["cats"] != -1 and aunts[aunt]["cats"] <= 7:
        aunts.pop(aunt)
        continue
    elif aunts[aunt]["samoyeds"] != -1 and aunts[aunt]["samoyeds"] != 2:
        aunts.pop(aunt)
        continue
    elif aunts[aunt]["pomeranians"] != -1 and aunts[aunt]["pomeranians"] >= 3:
        aunts.pop(aunt)
        continue
    elif aunts[aunt]["akitas"] != -1 and aunts[aunt]["akitas"] != 0:
        aunts.pop(aunt)
        continue
    elif aunts[aunt]["vizslas"] != -1 and aunts[aunt]["vizslas"] != 0:
        aunts.pop(aunt)
        continue
    elif aunts[aunt]["goldfish"] != -1 and aunts[aunt]["goldfish"] >= 5:
        aunts.pop(aunt)
        continue
    elif aunts[aunt]["trees"] != -1 and aunts[aunt]["trees"] <= 3:
        aunts.pop(aunt)
        continue
    elif aunts[aunt]["cars"] != -1 and aunts[aunt]["cars"] != 2:
        aunts.pop(aunt)
        continue
    elif aunts[aunt]["perfumes"] != -1 and aunts[aunt]["perfumes"] != 1:
        aunts.pop(aunt)
        continue
    else:
        pass

print(len(aunts.keys()))
print(aunts)

