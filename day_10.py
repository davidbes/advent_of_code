from toolz import memoize, concatv, frequencies, drop
data = sorted([int(x) for x in open("inputs/day_10.txt")])


def get_most_adapters_fact(data):
    differences = {1: 0, 2: 0, 3: 1}
    prev_number = 0
    for number in data:
        if number - prev_number <= 3:
            differences[number-prev_number] += 1
        prev_number = number

    return differences[1] * differences[3]


print(get_most_adapters_fact(data))


def recursive_counter(dictionary, value, cache):
    all_counter = 0
    if value in cache:
        return cache[value]
    for number in dictionary[value]:
        all_counter += recursive_counter(dictionary, number, cache)
    cache[value] = all_counter
    return all_counter


def get_all_possibilities(data):
    "Dict of adapters that have the value of adapters they can connect to"
    dictionary = {adapter: [x for x in data[i: i+3] if 0 < x-adapter <= 3]
                  for i, adapter in enumerate([0] + data)}
    return recursive_counter(dictionary, 0, {data[-1]: 1})
