commands = list()
with open("input_day7.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        commands.append(line.strip())
# print(commands)

wires = dict()
# wires["b"] = 16076

while len(commands) > 0:
    print(len(commands))
    for command in commands:
        target = command.split(" ")[-1]

        if "AND" in command:
            try:
                o1 = int(command.split(" ")[0])
            except ValueError:
                try:
                    o1 = wires[command.split(" ")[0]]
                except KeyError:
                    continue
            try:
                o2 = int(command.split(" ")[2])
            except ValueError:
                try:
                    o2 = wires[command.split(" ")[2]]
                except KeyError:
                    continue
            if target not in wires:
                wires[target] = None
            wires[target] = o1 & o2
            commands.remove(command)

        elif "OR" in command:
            try:
                o1 = int(command.split(" ")[0])
            except ValueError:
                try:
                    o1 = wires[command.split(" ")[0]]
                except KeyError:
                    continue
            try:
                o2 = int(command.split(" ")[2])
            except ValueError:
                try:
                    o2 = wires[command.split(" ")[2]]
                except KeyError:
                    continue
            if target not in wires:
                wires[target] = None
            wires[target] = o1 | o2
            commands.remove(command)

        elif "LSHIFT" in command:
            shift = int(command.split(" ")[2])
            try:
                o1 = wires[command.split(" ")[0]]
            except KeyError:
                continue
            if target not in wires:
                wires[target] = None
            wires[target] = o1 << shift
            commands.remove(command)

        elif "RSHIFT" in command:
            shift = int(command.split(" ")[2])
            try:
                o1 = wires[command.split(" ")[0]]
            except KeyError:
                continue
            if target not in wires:
                wires[target] = None
            wires[target] = o1 >> shift
            commands.remove(command)

        elif "NOT" in command:
            try:
                o1 = wires[command.split(" ")[1]]
            except KeyError:
                continue
            if target not in wires:
                wires[target] = None
            wires[target] = ~ o1
            commands.remove(command)

        else: # ->
            if target not in wires:
                wires[target] = None
            try:
                wires[target] = int(command.split(" ")[0])
                commands.remove(command)
            except ValueError:
                try:
                    wires[target] = wires[command.split(" ")[0]]
                    commands.remove(command)
                except KeyError:
                    continue

print(wires)
print(wires["a"])