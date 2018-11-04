
#
# literal_sum = 0
# memory_sum = 0
#
# with open("input_day8.txt") as file:
#     lines = file.readlines()
#     for line in lines:
#         line = line.strip()
#         literal_sum += len(line)
#         memory_sum += len(eval(line))
#
# print(literal_sum - memory_sum)

# part2
ori_len = 0
updated_len = 0
with open("input_day8.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        # # line = "abc"
        # print(line)
        # print(len(line))
        ori_len += len(line)

        # print(eval(line))
        # print(len(eval(line)))
        new_line = ""
        for char in line:
            if char == "\"":
                new_line += "\\" + "\""
            elif char == "\\":
                new_line += "\\" + "\\"
            else:
                new_line += char
        # print(new_line)
        # print(len(new_line)+2)
        updated_len += len(new_line) + 2
        # break
print(updated_len - ori_len)



