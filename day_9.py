import time
data = [int(x) for x in open("inputs/day_9.txt")]


def find_imposter(data, preamble):
    for index, number in enumerate(data):
        if index < preamble:
            continue
        numbers_pool = set(data[index-preamble:index])
        number_is_okay = False
        for pool_num in numbers_pool:
            if number - pool_num in numbers_pool:
                number_is_okay = True
                break
        if not number_is_okay:
            return number


def find_weakness(data, desired_sum):
    for i, num in enumerate(data):
        numbers = []
        current_index = i
        while sum(numbers) < desired_sum:
            numbers.append(data[current_index])
            current_index += 1
        if sum(numbers) == desired_sum and len(numbers) >= 3:
            return max(numbers) + min(numbers)


timer = time.time()
imposter = find_imposter(data, 25)
print(imposter)
print(find_weakness(data, imposter))
print(time.time() - timer)
