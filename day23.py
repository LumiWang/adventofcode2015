

map = dict()
map["a"] = 1
map["b"] = 0

with open("input_day23.txt") as file:
    lines = file.readlines()
    i = 0
    while True:
        try:
            line = lines[i]
            print(map)
            print(i)
            print(line)
            print()
            line = line.strip()
            command = line.split(" ")[0]
            if command != "jmp":
                register = line.split(" ")[1]
            if command == "jio" or command == "jie":
                register = line.split(" ")[1][:-1]
                step = int(line.split(" ")[-1])
            if command == "jmp":
                step = int(line.split(" ")[-1])

            if command == "inc":
                map[register] += 1
                i += 1
            elif command == "hlf":
                map[register] = map[register] / 2
                i += 1
            elif command == "tpl":
                map[register] = map[register] * 3
                i += 1
            elif command == "jmp":
                i += step
            elif command == "jio":
                if map[register] == 1:
                    i += step
                else:
                    i += 1
            elif command == "jie":
                if map[register] % 2 == 0:
                    i += step
                else:
                    i += 1
            else:
                raise Exception("Wrong command. Shouldn't happen.")

            # if i == len(lines)-1:
                # print(map)
        except IndexError:
            print(map)
            break

