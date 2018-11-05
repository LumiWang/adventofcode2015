


def look_and_say(input):
    """ input in str """
    copy_input = input[:]
    new_str = ""
    while len(copy_input) > 0:
        char = copy_input[0]
        num_chars = 0
        for i in range(0, len(copy_input)):
            if copy_input[i] == char:
                num_chars += 1
                if i == len(copy_input) - 1:
                    copy_input = ""
            else:
                copy_input = copy_input[num_chars:]
                # print(copy_input)
                break
        # print(num_chars)
        new_str += str(num_chars)
        new_str += char
        # print(new_str)
        # print(copy_input)
    return new_str

import itertools
def look_and_say_cheat(input):
    rtn = ""
    for k, v in itertools.groupby(input):
        # print(k)
        # print(len(list(v)))
        rtn += str(len(list(v))) + k
    return rtn
# print(look_and_say("1"))

TIMES = 50
input = "3113322113"
for i in range(0, TIMES):
    input = look_and_say_cheat(input)
    print(i)
print(len(input))

