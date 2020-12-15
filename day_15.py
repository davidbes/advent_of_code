
# data_one = (0, 3, 6)
# data_two = (0, 6, 1, 7, 2, 19, 20)


# def find_number(starting_point, max_num):
#     occurances = dict()
#     last_spoken = 0
#     for i, x in enumerate(starting_point):
#         occurances[x] = [i]
#         last_spoken = x

#     for ind in range(len(starting_point), max_num):
#         if ind == 1000000:
#             print("came here")

#         if len(occurances.get(last_spoken, [ind])) == 1:
#             last_spoken = 0

#         elif len(occurances.get(last_spoken, [ind])) >= 2:
#             list_of_occ = occurances[last_spoken]
#             last_spoken = list_of_occ[-1] - list_of_occ[-2]
#         occurances[last_spoken] = occurances.get(
#             last_spoken, []) + [ind]

#         if ind == max_num - 1:
#             print(last_spoken)


# find_number(data_one, 30000000)
from collections import defaultdict


def get_last_spoken_number_at(data, limit):
    occurances = defaultdict(lambda: turn)
    last = -1

    for turn, number in enumerate(data):
        occurances[last], last = turn, number

    for turn in range(len(data), limit):
        occurances[last], last = turn, turn - occurances[last]

    return last


print(get_last_spoken_number_at((0, 6, 1, 7, 2, 19, 20), 2020))
print(get_last_spoken_number_at((0, 6, 1, 7, 2, 19, 20), 30000000))
