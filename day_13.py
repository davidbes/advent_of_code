from math import prod
import math
input_data = [x.strip() for x in open("inputs/day_13.txt")]
data = int(input_data[0]), [int(x)
                            for x in input_data[1].split(",") if x != "x"]

data_two = [int(x) if x != "x"else x for x in input_data[1].split(",")]


def get_timestamp(data):
    timestamp, bus_ids = data
    best_ts, bus_id = None, None
    for ts in range(timestamp, max(bus_ids) + timestamp):
        for bus in bus_ids:
            if ts % bus == 0:
                best_ts, bus_id = ts, bus
                break
        else:
            continue
        break

    return (best_ts-timestamp) * bus_id


print(get_timestamp(data))


data = [x.strip() for x in open("inputs/day_13_examples.txt")]
new_data = []
for x in data:
    new_data.append([(i, int(x))
                     for i, x in enumerate(x.split(",")) if x != "x"])

# If we get first common denominator of first two numbers,
# then we can get the first common denominator of the number we get and the third number,
# and then we can get the fourth number and so on.


# def get_winner(bus_ids):
#     first_bus = bus_ids[0]
#     for offset, bus in bus_ids[1:]:
#         dcm = first_bus +


# get_winner(new_data[0])

# with open("inputs/day_13.txt") as f:
#     data = f.read().splitlines()

# earliest_start = int(data[0])
# buses = [int(x) for x in data[1].split(",") if x != "x"]

# departing = [(-1 * earliest_start) % x for x in buses]

# earliest_bus = sorted([[x, y] for x, y in zip(
#     buses, departing)], key=lambda b: b[1])[0]

# print(prod(earliest_bus))


# def chinese_remainder(n, a):
#     p = prod(n)
#     total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
#     return total % p


# inputs = [(int(x), int(x) - p)
#           for p, x in enumerate(data[1].split(",")) if x != "x"]

# print(chinese_remainder([x[0] for x in inputs], [x[1] for x in inputs]))
