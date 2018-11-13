
# parse input

stuff = dict()
stuff["Weapons"] = dict()
stuff["Armor"] = dict()
stuff["Rings"] = dict()

is_weapon = False
is_armor = False
is_ring = False
# parse stuff selling in shop
with open("input_day21.txt") as file:
    lines = file.readlines()
    for line in lines:
        if len(line)>1:
            line = line.strip()
            merchandise = line.split(" ")[0]
            # print(merchandise)
            if "Weapons" in merchandise:
                is_weapon = True
                is_armor = False
                is_ring = False
                continue
            elif "Armor" in merchandise:
                is_armor = True
                is_weapon = False
                is_ring = False
                continue
            elif "Rings" in merchandise:
                is_armor = False
                is_weapon = False
                is_ring = True
                continue
            else:
                if is_weapon:
                    stuff["Weapons"][merchandise] = dict()
                    line = line.split(" ")[1:]
                    new_line = list()
                    for i in range(0, len(line)):
                        if len(line[i]) > 0:
                            new_line.append(line[i])
                    # print(new_line)
                    # print(int(new_line[0]))
                    stuff["Weapons"][merchandise]["Cost"] = int(new_line[0])
                    stuff["Weapons"][merchandise]["Damage"] = int(new_line[1])
                    stuff["Weapons"][merchandise]["Armor"] = int(new_line[2])
                elif is_armor:
                    stuff["Armor"][merchandise] = dict()
                    line = line.split(" ")[1:]
                    new_line = list()
                    for i in range(0, len(line)):
                        if len(line[i]) > 0:
                            new_line.append(line[i])
                    # print(new_line)
                    # print(int(new_line[0]))
                    stuff["Armor"][merchandise]["Cost"] = int(new_line[0])
                    stuff["Armor"][merchandise]["Damage"] = int(new_line[1])
                    stuff["Armor"][merchandise]["Armor"] = int(new_line[2])
                elif is_ring:
                    merchandise = line.split(" ")[0]+" "+line.split(" ")[1]
                    stuff["Rings"][merchandise] = dict()
                    line = line.split(" ")[2:]
                    new_line = list()
                    for i in range(0, len(line)):
                        if len(line[i]) > 0:
                            new_line.append(line[i])
                    # print(new_line)
                    # print(int(new_line[0]))
                    stuff["Rings"][merchandise]["Cost"] = int(new_line[0])
                    stuff["Rings"][merchandise]["Damage"] = int(new_line[1])
                    stuff["Rings"][merchandise]["Armor"] = int(new_line[2])
                else:
                    raise Exception("Wrong type of stuff. Shouldn't happen.")
print(stuff)


def do_one_attack(damage, armor):
    if damage > armor:
        return damage - armor
    else:
        return 1


def play_game(player_hit_point, player_damage, player_armor, computer_hit_point, computer_damage, computer_armor):
    # player always starts first
    players_turn = True
    while player_hit_point > 0 and computer_hit_point > 0:
        if players_turn:
            computer_hit_point -= do_one_attack(player_damage, computer_armor)
            players_turn = False
            # print("Computer goes down to {} points".format(computer_hit_point))
        else:
            player_hit_point -= do_one_attack(computer_damage, player_armor)
            players_turn = True
            # print("Player goes down to {} points".format(player_hit_point))
    if player_hit_point <= 0:
        return False
    else:
        return True

# print(play_game(8, 5, 5, 12, 7, 2))



# requirements:
# 1 weapon, 0-1 armor, 0-2 rings
# find the minimal money needed to beat the computer
import itertools


def get_all_possibilities_that_meet_requirements(stuff):
    possibilities = list()
    weapon_possibilities = sorted(stuff["Weapons"].keys())
    # print(weapon_possibilities)
    # print()
    armor_possibilities = list()
    armor_possibilities.append([])
    armor_possibilities.extend(sorted(stuff["Armor"].keys()))
    # print(armor_possibilities)
    # print()
    ring_possibilities = list()
    ring_possibilities.append([])
    ring_possibilities.extend(sorted(stuff["Rings"].keys()))
    ring_possibilities.extend(list(itertools.combinations(stuff["Rings"].keys(), 2)))
    # print(ring_possibilities)
    # print()
    for weapon in weapon_possibilities:
        for armor in armor_possibilities:
            for ring in ring_possibilities:
                if isinstance(ring, str):
                    item = [weapon, armor, ring]
                else:
                    item = [weapon, armor]
                    for r in ring:
                        item.append(r)
                possibilities.append(item)
    # print(possibilities)
    return possibilities


possibilities = get_all_possibilities_that_meet_requirements(stuff)
print(possibilities)


def calculate_damage_and_armor_and_cost(possibility):
    damage = 0
    armor = 0
    cost = 0
    for item in possibility:
        if isinstance(item, str):
            try:
                damage += stuff["Weapons"][item]["Damage"]
            except KeyError:
                pass
            try:
                damage += stuff["Rings"][item]["Damage"]
            except KeyError:
                pass
            try:
                armor += stuff["Armor"][item]["Armor"]
            except KeyError:
                pass
            try:
                armor += stuff["Rings"][item]["Armor"]
            except KeyError:
                pass
            try:
                cost += stuff["Weapons"][item]["Cost"]
            except KeyError:
                pass
            try:
                cost += stuff["Armor"][item]["Cost"]
            except KeyError:
                pass
            try:
                cost += stuff["Rings"][item]["Cost"]
            except KeyError:
                pass

    return damage, armor, cost


player_hit_point = 100
computer_hit_point = 103
computer_damage = 9
computer_armor = 2


def part_1(possibilities):
    lowest_cost = 5000
    combination = list()
    for possibility in possibilities:
        damage, armor, cost = calculate_damage_and_armor_and_cost(possibility)
        if play_game(player_hit_point, damage, armor, computer_hit_point, computer_damage, computer_armor):
            if cost < lowest_cost:
                lowest_cost = cost
                combination = possibility
    return lowest_cost, combination

lowest_cost, combination = part_1(possibilities)
print(lowest_cost)
print(combination)


def part2(possibilities):
    highest_cost = 0
    combination = list()
    for possibility in possibilities:
        damage, armor, cost = calculate_damage_and_armor_and_cost(possibility)
        if not play_game(player_hit_point, damage, armor, computer_hit_point, computer_damage, computer_armor):
            if cost > highest_cost:
                combination = possibility
                highest_cost = cost
    return highest_cost, combination


highest_cost, combination = part2(possibilities)
print(highest_cost)
print(combination)

