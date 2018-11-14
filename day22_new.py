import itertools

# the idea is to list all possible spell sequences, up to a certain number
# and then go through the all possibilities, to see if any can beat the computer
# to list all possibilities,
# S and P have a timer of 6, which means at least 2 spells need to be casted in between the first spell and the next
# R has a timer of 5, so it needs to wait for at least 1 spell to be used

spells = ["M", "D", "S", "P", "R"]
def get_all_possibilities(num):
    if num == 0:
        return list()
    elif num == 1:
        return spells.copy()
    elif num == 2:
        # return list(itertools.combinations_with_replacement(spells, 2))
        # the above doesn't work, because there cannot be SS or PP or RR
        rtn_list = list()
        for item in get_all_possibilities(1):
            for c in spells:
                if not (item == "S" and c == "S"):
                    if not (item == "P" and c == "P"):
                        if not (item == "R" and c == "R"):
                            new_sequence = item + c
                            rtn_list.append(new_sequence)
                            # print(rtn_list)
        return rtn_list
    elif num == 3:
        rtn_list = list()
        for item in get_all_possibilities(2):
            for c in spells:
                if c == "R":
                    if item[-1] != "R":
                        new_sequence = item + c
                        rtn_list.append(new_sequence)
                elif c == "S" or c == "P":
                    if item[-1] != c and item[-2] != c:
                        new_sequence = item + c
                        rtn_list.append(new_sequence)
                else:
                    new_sequence = item + c
                    rtn_list.append(new_sequence)
        return rtn_list

    else:
        rtn_list = list()
        for item in get_all_possibilities(num-1):
            for c in spells:
                if c == "R":
                    if item[-1] != "R":
                        new_sequence = item + c
                        rtn_list.append(new_sequence)
                elif c == "S" or c == "P":
                    if item[-1] != c and item[-2] != c:
                        new_sequence = item + c
                        rtn_list.append(new_sequence)
                else:
                    new_sequence = item + c
                    rtn_list.append(new_sequence)
        return rtn_list



# print(len(get_all_possibilities(10)))
# print(get_all_possibilities(5))

"""
'SDRMP', 'SDRMR', 'SDRDM', 'SDRDD', 'SDRDS', 'SDRDP'
"""
# up to the length of 10, there are all 2001176 combinations. Not that bad at all.

# list of spells:
# 0: cost; 1: timer; 2: damage; 3: armor; 4: heal; 5: mana
map = dict()
map["M"] = (53, 1, 4, 0, 0, 0)
map["D"] = (73, 1, 2, 0, 2, 0)
map["S"] = (113, 7, 0, 7, 0, 0)
map["P"] = (173, 7, 3, 0, 0, 0)
map["R"] = (229, 6, 0, 0, 0, 101)

player_hit_point_real = 50
mana_real = 500
computer_hit_point_real = 58
computer_damage_real = 9


def play_game(sequence, player_hit_point, mana, computer_hit_point, computer_damage):
    """
    returns True if player wins, False if computer wins
    """
    mana_spent = 0

    damage_timer = 0
    armor_timer = 0
    mana_timer = 0

    for i in range(0, len(sequence)):
        # print("In the beginning of player's turn:")
        # print("Player has hit point: {}, mana: {}".format(player_hit_point, mana))
        # print("Computer has hit point: {}".format(computer_hit_point))
        # print("Armor timer is {}, damage timer is {}, mana timer is {}".format(armor_timer, damage_timer, mana_timer))
        # print()
        # before doing anything, check if computer is dead
        if computer_hit_point <= 0:
            return True, mana_spent
        if player_hit_point <= 0 or mana < 53:
            return False, mana_spent
        spell = sequence[i]

        player_armor = map["S"][3]
        player_damage = map["P"][2]
        player_mana = map["R"][5]

        # turn one:

        # for part two:
        player_hit_point -= 1
        if player_hit_point <= 0 or mana < 53:
            return False, mana_spent

        # before player plays, deal with timers:
        if damage_timer > 0:
            computer_hit_point -= player_damage
        if mana_timer > 0:
            mana += player_mana
        # check if computer is dead yet:
        if computer_hit_point <= 0:
            return True, mana_spent

        # player plays first:
        mana -= map[spell][0]
        mana_spent += map[spell][0]

        if spell == "M":
            player_damage = map[spell][2]
            computer_hit_point -= player_damage
        elif spell == "D":
            player_damage = map[spell][2]
            computer_hit_point -= player_damage
            heal = map[spell][4]
            player_hit_point += heal
        elif spell == "S":
            armor_timer = map[spell][1]
        elif spell == "P":
            damage_timer = map[spell][1]
        elif spell == "R":
            mana_timer = map[spell][1]
        else:
            raise Exception("Wrong spell, shouldn't happen.")
        # in the end, reduce the timer by one:
        armor_timer -= 1
        damage_timer -= 1
        mana_timer -= 1

        # debug prints:
        # print("--DEBUG: At the end of player's turn:")
        # print("Armor timer is {}, damage timer is {}, mana timer is {}".format(armor_timer, damage_timer, mana_timer))
        # print("Player has hit point: {}, mana: {}".format(player_hit_point, mana))
        # print("Computer has hit point: {}".format(computer_hit_point))
        # print("-----------")
        # print()

        # turn two: computer's turn:
        # print("In the beginning of computer's turn:")
        # print("Player has hit point: {}, mana: {}".format(player_hit_point, mana))
        # print("Computer has hit point: {}".format(computer_hit_point))
        # print("Armor timer is {}, damage timer is {}, mana timer is {}".format(armor_timer, damage_timer, mana_timer))
        # print("-----------")
        # print()
        # computer deals with damages and stuff before attacking
        if damage_timer > 0:
            computer_hit_point -= player_damage
        if mana_timer > 0:
            mana += player_mana
        # check if computer is dead yet:
        if computer_hit_point <= 0:
            return True, mana_spent
        # then it attacks:
        if armor_timer > 0:
            if computer_damage > player_armor:
                player_hit_point -= computer_damage - player_armor
            else:
                player_hit_point -= 1
        else:
            player_hit_point -= computer_damage

        # after attack, check if the player is dead yet:
        if player_hit_point <= 0 or mana < 53:
            return False, mana_spent

        # in the end, reduce the timer by one:
        damage_timer -= 1
        mana_timer -= 1
        armor_timer -= 1

        # debug prints:
        # print("--DEBUG: At the end of computer's turn:")
        # print("Armor timer is {}, damage timer is {}, mana timer is {}".format(armor_timer, damage_timer, mana_timer))
        # print("Player has hit point: {}, mana: {}".format(player_hit_point, mana))
        # print("Computer has hit point: {}".format(computer_hit_point))
        # print("-----------")
        # print()

# a, b = play_game("RSDPM", player_hit_point_real, mana_real, computer_hit_point_real, computer_damage_real)


possibilities_9 = get_all_possibilities(9)
for sequence in possibilities_9:
    # print(sequence)
    try:
        win, mana_spent = play_game(sequence, player_hit_point_real, mana_real, computer_hit_point_real, computer_damage_real)

        if win:
            print(sequence)
            print(mana_spent)
            break
    except TypeError:
        # game not finished
        continue