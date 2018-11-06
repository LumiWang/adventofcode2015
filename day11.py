
import string

alfa = list(string.ascii_lowercase)


def list_to_string(list):
    rtn = ""
    for item in list:
        rtn += item
    return rtn


def get_ascending_3_chars():
    chars_list = list()
    for i in range(0, len(alfa)-2):
        chars_list.append(list_to_string(alfa[i:i+3]))
    return chars_list


def get_repeating_chars():
    chars_list = list()
    for char in alfa:
        chars_list.append(char + char)
    return chars_list


def legal_password(pw):
    pw = list_to_string(pw)
    meet_criteria_1 = False
    char_list = get_ascending_3_chars()
    for chars in char_list:
        if chars in pw:
            meet_criteria_1 = True
            break
    if meet_criteria_1:
        meet_criteria_2 = True
        banned_chars = ["i", "o", "l"]
        for char in banned_chars:
            if char in pw:
                meet_criteria_2 = False
                break
        if meet_criteria_2:
            repeating_chars = get_repeating_chars()
            repeating_char_num = 0
            for chars in repeating_chars:
                if chars in pw:
                    repeating_char_num += 1
            if repeating_char_num >= 2:
                return True
    return False

# print(legal_password("abcdffaa"))


def add_on_one_char(a_char):
    turn_around = False
    try:
        a_char = alfa[alfa.index(a_char)+1]
    except IndexError:
        a_char = alfa[0]
        turn_around = True
    return a_char, turn_around

# print(add_on_one_char("z"))


def pre_process_pw(pw):
    """ pw in list"""
    banned_chars = ["i", "o", "l"]
    for char in banned_chars:
        for i in range(0, len(pw)):
            if pw[i] == char:
                pw[i] = alfa[alfa.index(char) + 1]
    return pw

input = list("hxbxxyzz")


j = -1
while True:
    input[j], turn_around = add_on_one_char(input[j])
    if turn_around:
        input[j-1], turn_around = add_on_one_char(input[j-1])
        if turn_around:
            input[j - 2], turn_around = add_on_one_char(input[j - 2])
            if turn_around:
                print(input)
                input[j - 3], turn_around = add_on_one_char(input[j - 3])
                if turn_around:
                    input[j - 4], turn_around = add_on_one_char(input[j - 4])
                    if turn_around:
                        input[j - 5], turn_around = add_on_one_char(input[j - 5])


    if legal_password(input):
        print(list_to_string(input))
        break


# On second thought, there can be a easy way out:
# as y, or z cannot bring a "abc" sequence after them,
# if there is y or z, and before them there's no "abc" sequence,
# the y or z shall be directly added up to save time.