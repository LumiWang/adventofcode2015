
input_1 = "ugknbfddgicrmopn"  # True
input_2 = "aaa"  # True
input_3 = "jchzalrnumimnmhp"  # False
input_4 = "haegwjzuvuyypxyu"  # False
input_5 = "dvszwmarrgswjxmb"  # False


def is_nice(input):
    if contains_three_or_more_vowels(input):
        if contains_one_repetitive_letter(input):
            if no_bad_strings(input):
                return True
    return False


def contains_three_or_more_vowels(input):
    VOWELS = ["a", "e", "i", "o", "u"]
    total_vowels = 0
    for char in input:
        if char in VOWELS:
            total_vowels += 1
    if total_vowels >= 3:
        return True
    return False


def contains_one_repetitive_letter(input):
    for i in range(0, len(input)-1):
        if input[i] == input[i+1]:
            return True
    return False


def no_bad_strings(input):
    bad_strings = ["ab", "cd", "pq", "xy"]
    for bad_string in bad_strings:
        if bad_string in input:
            return False
    return True


nice_strings = 0
with open("input_day5.txt", "r") as file:
    inputs = file.readlines()
    for input in inputs:
        if is_nice(input):
            nice_strings += 1


# print(nice_strings)


# part 2

def new_rule_one(input):
    for i in range(0, len(input) - 1):
        pair = input[i: i+2]
        if input.count(pair) > 1:
            return True
    return False


def new_rule_two(input):
    for i in range(0, len(input) - 2):
        if input[i] == input[i+2]:
            return True
    return False


def is_nice_2(input):
    if new_rule_one(input):
        if new_rule_two(input):
            return True
    return False


input_6 = "qjhvhtzxzqqjkmpb"
input_7 = "xxyxx"
input_8 = "uurcxstgmygtbstg"
input_9 = "ieodomkazucvgmuy"


nice_strings_2 = 0
with open("input_day5.txt", "r") as file:
    inputs = file.readlines()
    for input in inputs:
        if is_nice_2(input):
            nice_strings_2 += 1

print(nice_strings_2)
