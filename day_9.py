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


# def find_weakness(data, desired_sum):  # AVG 0.234sec
#     for i, _ in enumerate(data):
#         numbers = []
#         current_index = i
#         while sum(numbers) < desired_sum:
#             numbers.append(data[current_index])
#             current_index += 1
#         if sum(numbers) == desired_sum and len(numbers) >= 3:
#             return max(numbers) + min(numbers)


def find_weakness(data, desired_sum):   # AVG 0,024sec
    for i, num in enumerate(data):
        num_sum = 0
        current_index = i
        curr_min, curr_max = num, num
        while num_sum < desired_sum:
            number = data[current_index]
            num_sum += number
            curr_max = curr_max if curr_max >= number else number
            curr_min = curr_min if curr_min <= number else number
            current_index += 1
        if num_sum == desired_sum and current_index - i >= 2:
            return curr_min + curr_max


timer = time.time()
imposter = find_imposter(data, 25)

print(find_weakness(data, imposter))
print(time.time() - timer)
