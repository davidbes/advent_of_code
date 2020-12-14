def generate_data(input):
    data = []
    for line in [x.strip() for x in open(input)]:
        p = line.split(" ")
        if p[0] == "mask":
            data.append(p[2])
        elif p[0].startswith("mem"):
            addr = int("".join([x for x in p[0] if x.isdigit()]))
            numb = int(p[2])
            data.append((addr, numb))
    return data


data = generate_data("inputs/day_14.txt")
small_data = generate_data("inputs/day_14_two.txt")


def count_values_decoder_one(rules):
    current_mask = ""
    current_values = dict()
    for row in rules:
        if len(row) == 2:
            addr, num = row
            binary_val = f"{bin(num)[2:]:0>36}"
            output_num = list(current_mask)
            for i, c in enumerate(current_mask):
                if c == "X":
                    output_num[i] = binary_val[i]
            current_values[addr] = int("".join(output_num), 2)
        else:
            current_mask = row
    return sum(current_values.values())


def return_all_binaries(binary_list):
    if sum(["X" in x for x in binary_list]) == 0:
        return binary_list

    new_binary_list = []

    for binary_str in binary_list:
        index = binary_str.find("X")
        our_string = list(binary_str)
        our_string[index] = "1"
        new_binary_list.append("".join(our_string))
        our_string[index] = "0"
        new_binary_list.append("".join(our_string))

    return return_all_binaries(new_binary_list)


def count_values_decoder_two(rules):
    current_mask = ""
    current_values = dict()
    for row in rules:
        if len(row) == 2:
            addr, number = row
            binary_val = f"{bin(addr)[2:]:0>36}"
            output_num = list(current_mask)
            for i, c in enumerate(current_mask):
                if c == "0":
                    output_num[i] = binary_val[i]

            list_of_binaries = return_all_binaries(["".join(output_num)])

            for x in list_of_binaries:
                current_values[x] = number
        else:
            current_mask = row
    return sum(current_values.values())


print(count_values_decoder_one(data))
print(count_values_decoder_two(data))
