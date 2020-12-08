data = [x.strip().split(" ") for x in open("inputs/day_8.txt")]


def check_if_infinite(commands):
    seen_commands = [False] * len(commands)
    is_infinite = False
    itterator = 0
    accumulator = 0

    while not all(seen_commands) and itterator < len(commands):
        if not seen_commands[itterator]:
            seen_commands[itterator] = True
            command = commands[itterator]
            if command[0] == "acc":
                accumulator += int(command[1])
                itterator += 1
            elif command[0] == "nop":
                itterator += 1
            elif command[0] == "jmp":
                itterator += int(command[1])
        else:
            is_infinite = True
            break
    return accumulator, is_infinite


def change_one_command(commands):
    new_com = {"jmp": "nop", "nop": "jmp", "acc": "acc"}
    for index, command in enumerate(commands):
        new_commands = commands[:]
        new_commands[index] = (new_com[command[0]], command[1])
        acc, is_infinite = check_if_infinite(new_commands)

        if not is_infinite:
            return acc


print(check_if_infinite(data))

print(change_one_command(data))
