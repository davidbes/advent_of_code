data = {int(x) for x in open("inputs/day_1.txt")}


def task_one(data):
    for x in data:
        if 2020 - x in data:
            return x * (2020 - x)


def task_two(data):
    for x in data:
        for y in data:
            if (2020 - x - y) in data:
                return x * (2020 - x - y) * y


print(task_one(data), task_two(data))
