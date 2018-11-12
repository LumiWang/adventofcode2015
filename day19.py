medicine_molecule = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"
# medicine_molecule = "HOHOHO"

new_molecules = list()

# check through each line of commands
# for each line of command, go through the medicine molecule, find all the possibilities to exchange
# exchange, add new molecule to the list
# count the length of set


def replace_part_of_string(start_string, start_index, old_string, new_string):
    rtn_string = start_string[:start_index]
    rtn_string += new_string
    end_index = start_index + len(old_string)
    rtn_string += start_string[end_index:]
    return rtn_string

# print(replace_part_of_string("abc", 2, "c", "zk"))


def do_one_replacement(medicine_molecule):
    with open("input_day19.txt") as file:
        commands = file.readlines()
        # print(len(commands))
        for command in commands:
            command = command.rstrip()
            # print(command)
            ch1 = command.split(" ")[0]
            ch2 = command.split(" ")[-1]
            # print(ch1, ch2)
            # print()

            for i in range(0, len(medicine_molecule)):
                if medicine_molecule[i:i+len(ch1)] == ch1:
                    # new_molecule = replace_part_of_string(medicine_molecule, i, ch1, ch2)
                    new_molecule = medicine_molecule[:i] + ch2 + medicine_molecule[i+len(ch1):]
                    # print(new_molecule)
                    new_molecules.append(new_molecule)
    return new_molecules

# print(new_molecules)
# new_molecules = do_one_replacement(medicine_molecule=medicine_molecule)
# print(len(set(new_molecules)))


# after_1 = do_one_replacement("e")
# print(after_1)
#
# after_2 = list()
# for item in after_1.copy():
#     print(item)
#     after_2_part = do_one_replacement(item)
#     print(after_2_part)
#     after_2 += after_2_part
# print(after_2)

desired_str = medicine_molecule


def find_desired_str(desired_str):
    step = 1
    start = ["e"]
    after = list()
    while step < 10:
        for item in start.copy():
            after_part = do_one_replacement(item)
            after += after_part
            after = list(set(after))
            start = after
            if desired_str in after_part:
                print("Found after step {}".format(step))
                return step
        step += 1
        print(step)
        print(len(after))
        print()

# print(find_desired_str(desired_str))


def parse_input(input_file):
    map = dict()
    with open(input_file) as file:
        commands = file.readlines()
        # print(len(commands))
        for command in commands:
            command = command.rstrip()
            # print(command)
            ch1 = command.split(" ")[0]
            ch2 = command.split(" ")[-1]
            if ch2 not in map:
                map[ch2] = ch1
            map[ch2] = ch1
    return map
map = parse_input("input_day19.txt")

# risky way: find the longest part of string that can be changed, change it, repeat, see if go back to e
length_sorted = sorted(map, key=len, reverse=True)
print(length_sorted)

string_under_operation = medicine_molecule
step = 0


def find_step(string_under_operation):
    step = 1
    while True:
        for item in length_sorted:
            if item in string_under_operation:
                i = string_under_operation.index(item)
                changed = map[item]
                string_under_operation = string_under_operation[:i] + changed + string_under_operation[i+len(item):]
                if string_under_operation == "e":
                    return step
                print("step {}: {} changed to {}.".format(step, item, changed))
                print("NEW STRING: {}".format(string_under_operation))
                break
        step += 1

# print(find_step(medicine_molecule))
# Didn't work out... In this way it would not go back to "e".


# Official cheat:
# #NumSymbols - #Rn - #Ar - 2 * #Y - 1

print(len(medicine_molecule) - medicine_molecule.count("Rn") - medicine_molecule.count("Ar") - 2 * medicine_molecule.count("Y") - 1)