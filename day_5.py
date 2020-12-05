data = [x.strip() for x in open("inputs/day_5.txt")]


def replace_with_binary(string, zero, one):
    return string.replace(zero, "0").replace(one, "1")


def generate_seats(data):
    seat_ids = set()
    for seat in data:
        column = int(replace_with_binary(seat[:7], "F", "B"), 2)
        row = int(replace_with_binary(seat[7:], "L", "R"), 2)
        seat_ids.add(column * 8 + row)
    return seat_ids


def get_min_max_your_seat(seats):
    maximum = max(seats)
    minimum = min(seats)
    possible_seats = {x for x in range(minimum, maximum + 1) if x not in seats}
    print(maximum, minimum, possible_seats)


get_min_max_your_seat(generate_seats(data))
