import re
import json

with open("input_day12.txt") as file:
    input = file.read()
# print(input)

sum = 0
pattern = r'[-\d]+'

for item in re.findall(pattern, input):
    # print(item)
    sum += int(item)
# print(sum)


with open("input_day12.txt") as file:
    data = json.load(file)
    str_data = json.dumps(data, indent=4)
    print(str_data)

sum = 0

# data = {'a': 81, 'c': 45, 'b': ['orange'], 'd': 'violet', 'f': [-3, 'red', 146, 186, 'orange', 'red', 'blue', {'a': 'yellow', 'c': 22, 'b': 'blue', 'd': -2, 'f': 'green', 'e': 'green'}, 0, 180], 'e': 'yellow'}

def foo(data):
    if isinstance(data, (int,)):
        return data
    elif data == "red":
        return 0
    elif isinstance(data, (list,)):
        rtn = 0
        for item in data:
            rtn += foo(item)
        return rtn
    elif isinstance(data, (dict,)):
        if "red" in data.values():
            return 0
        else:
            rtn = 0
            for item in data:
                rtn += foo(data[item])
            return rtn
    else:
        return 0

print(foo(data))