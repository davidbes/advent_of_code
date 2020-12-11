import time
data = [x.strip()for x in open("inputs/day_11.txt")]
positions = {
    "left": (-1, 0),
    "right": (1, 0),
    "up": (0, -1),
    "down": (0, 1),
    "up-left": (-1, -1),
    "up-right": (1, -1),
    "down-left": (-1, 1),
    "down-right": (1, 1)
}


def count_adjacent_taken_seats(grid, x, y):
    counts = 0
    for cal_x, cal_y in positions.values():
        if y + cal_y == len(grid) or y + cal_y == -1:
            continue
        if x + cal_x == len(grid[y]) or x + cal_x == -1:
            continue

        if grid[y + cal_y][x + cal_x] == "#":
            counts += 1
    return counts


def count_seen_taken_seats(grid, x, y):
    counts = 0
    for cal_x, cal_y in positions.values():
        pos_y = y + cal_y
        pos_x = x + cal_x
        while True:
            if pos_y == len(grid) or pos_y == -1 or pos_x == len(grid[y]) or pos_x == -1:
                break
            elif grid[pos_y][pos_x] in {'#', 'L'}:
                if grid[pos_y][pos_x] == "#":
                    counts += 1
                break
            else:
                pos_x += cal_x
                pos_y += cal_y
    return counts


def make_seats_with_lists(grid, max_seats_allowed, seat_counter):
    new_grid = grid[:]
    for iy, row in enumerate(grid):
        for ix, x in enumerate(row):
            near_seats = seat_counter(grid, ix, iy)
            list_y = list(new_grid[iy])

            if x == "L" and near_seats == 0:
                list_y[ix] = "#"
            elif x == "#" and near_seats >= max_seats_allowed:
                list_y[ix] = "L"

            new_grid[iy] = "".join(list_y)

    for row1, row2 in zip(grid, new_grid):
        if row1 != row2:
            return make_seats_with_lists(new_grid, max_seats_allowed, seat_counter)
    else:
        return sum([x.count('#') for x in grid])


# Solution for faster algorithm =
# Make two sets of coordinates of taken/empty seats


def create_tuples_of_coords(data, el):
    return {(ix, iy) for iy, row in enumerate(data) for ix, x in enumerate(row) if x == el}


def count_adjacency_seats(seat, taken_seats, _):
    counter = 0
    x, y = seat
    for pos_x, pos_y in positions.values():
        if (pos_x + x, pos_y + y) in taken_seats:
            counter += 1
    return counter


# def count_seen_seats(seat, taken_seats, avilable_seats):
#     counter = 0
#     seat_x, seat_y = seat
#     all_seats = avilable_seats | taken_seats
#     max_x = max(all_seats)[0]
#     max_y = max(all_seats, key=lambda x: x[1])[1]
#     for x, y in positions.values():
#         pos_y = seat_x + y
#         pos_x = seat_y + x
#         while True:
#             if 0 <= pos_x <= max_x and 0 <= pos_y <= max_y:
#                 if (pos_x, pos_y) in taken_seats:
#                     counter += 1
#                     break
#                 if (pos_x, pos_y) in avilable_seats:
#                     break
#                 pos_y += y
#                 pos_x += x
#             else:
#                 break
#     return counter

# def count_seen_seats(seat, taken, avilable):
#     main_x, main_y = seat
#     counts = 0
#     all_seats_on_x = set()
#     all_seats_on_y = set()
#     all_seats_on_diagonal = set()
#     all_seats_on_diagonal_2 = set()
#     for x, y in avilable:
#         if x == main_x and y != main_y:
#             all_seats_on_x.add((x, y))
#             continue
#         if y == main_y and x != main_x:
#             all_seats_on_y.add((x, y))
#             continue

#         if x != 0 and main_x != 0:
#             if y/x == main_y/main_x:
#                 all_seats_on_diagonal.add((x, y))
#                 continue
#         if y != 0 and main_y != 0:
#             if x/y == main_x/main_y:
#                 all_seats_on_diagonal_2.add((x, y))

#     print(seat)
#     print(all_seats_on_diagonal)
#     print(all_seats_on_diagonal_2)
#     return 2


def make_rotation(taken, avilable, max_seats_allowed, seat_counter):
    new_taken = taken.copy()
    new_avil = avilable.copy()
    for seat in taken | avilable:
        counter = seat_counter(seat, taken, avilable)
        if counter == 0:
            new_taken.add(seat)
            if seat in new_avil:
                new_avil.remove(seat)
            continue
        if counter >= max_seats_allowed:
            new_avil.add(seat)
            if seat in new_taken:
                new_taken.remove(seat)
            continue

    if len(taken) == len(new_taken):
        return len(taken)
    else:
        return make_rotation(new_taken, new_avil, max_seats_allowed, seat_counter)


def make_better_seats(grid):
    taken = create_tuples_of_coords(grid, "#")
    avilable = create_tuples_of_coords(grid, "L")
    first = make_rotation(taken, avilable, 4, count_adjacency_seats)
    # SECOND == MISSING FUCNTION FOR COUNTER CHECK
    return first


timer = time.time()
result_one = make_seats_with_lists(
    data, 4, count_adjacent_taken_seats)
first_time = time.time() - timer
timer = time.time()

result_two = make_better_seats(data)
second_time = time.time() - timer

print(result_one)
print(f"With Lists: {first_time:.3f}s")
print(f"With Sets: {second_time:.3f}s")
