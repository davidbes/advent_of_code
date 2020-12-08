
data = [x.strip() for x in open("inputs/day_8.txt")]


# data = ["nop +0",
#         "acc +1",
#         "jmp +4",
#         "acc +3",
#         "jmp -3",
#         "acc -99",
#         "acc +1",
#         "jmp -4",
#         "acc +6"]

processed_data = [(i, (x.split(" "))) for i, x in enumerate(data)]


def task_one(data):
    seen_commands = set()
    accumulator = 0
    itteration = 0
    is__infinite = False
    while len(seen_commands) != len(data):
        if itteration >= len(data):
            break
        index, command = data[itteration]
        if index not in seen_commands:
            seen_commands.add(index)
            if command[0] == "nop":
                itteration += 1
            elif command[0] == "acc":
                accumulator += int(command[1])
                itteration += 1
            elif command[0] == "jmp":
                itteration += int(command[1])

        else:
            is__infinite = True
            break

    return accumulator, seen_commands, is__infinite


# # for item in data:
# for index, item in enumerate(processed_data):
#     comm = processed_data[index][1][0]
#     new_data = processed_data[:]
#     if comm == "nop":
#         new_comm = "jmp"
#     elif comm == "jmp":
#         new_comm == "nop"
#     else:
#         new_comm == comm

#     new_item = (index, [new_comm, processed_data[index][1][1]])
#     new_data[index] = new_item
#     print(new_data)
#     print(task_one(new_data))

def change_one_command(data):

    for index, command in data:
        new_data = data[:]
        if command[0] == "jmp":
            new_data[index] = (index, ["nop", command[1]])
        elif command[0] == "nop":
            new_data[index] = (index, ["jmp", command[1]])
        else:
            new_data[index] = (index, command)

        acc, comms, is_infinite = task_one(new_data)
        if not is_infinite:
            print(acc)


change_one_command(processed_data)
