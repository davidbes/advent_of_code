data = " ".join(["-" if x == "\n" else x.strip()
                 for x in open("inputs/day_6.txt")]).split(" - ")


def task_one(polls) -> int:
    count = 0
    for group in polls:
        unique = {x for x in group if x != " "}
        count += len(unique)
    return count


def task_two(polls) -> int:
    count = 0
    for group in polls:
        unique = {x for x in group if x != " "}
        for c in unique:
            count += group.count(c) == len(group.split(" "))
    return count


def task_one_oneliner(polls) -> int:
    return sum([len(unique) for group in polls for unique in {x for x in group if x != " "}])


def task_two_oneliner(polls) -> int:
    return sum([group.count(c) == len(group.split(" ")) for group in polls for c in {x for x in group if x != " "}])


print(task_one_oneliner(data), task_two_oneliner(data))
