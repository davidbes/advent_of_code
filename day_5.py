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


def get_max_seat_id(seats):
    print("Maximum seat", max(seats))
    print("Minimum seat", min(seats))
    [print("Your seat", x)
     for x in range(min(seats), max(seats)) if x not in seats]


get_max_seat_id(generate_seats(data))
