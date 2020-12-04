data = [tuple(x.strip().split(" ")) for x in open("inputs/day_2.txt")]


def task_one(data):
    allowed = 0
    for numbers, criteria, sequence in data:
        least, most = tuple(int(x) for x in numbers.split("-"))
        letter = criteria[:1]
        number_of_occurences = len([x for x in sequence if x == letter])
        allowed += least <= number_of_occurences <= most

    return allowed


def task_two(data):
    allowed = 0
    for numbers, criteria, sequence in data:
        first, second = tuple(int(x) for x in numbers.split("-"))
        letter = criteria[:1]
        char_one = sequence[first - 1]
        char_two = sequence[second - 1]
        alowwed += char_two != char_one and (letter ==
                                             char_one or letter == char_two)
    return allowed


print(task_one(data), task_two(data))
