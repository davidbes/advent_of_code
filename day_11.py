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


def make_seats(grid, max_seats_allowed, seat_counter):
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
            return make_seats(new_grid, max_seats_allowed, seat_counter)
    else:
        return sum([x.count('#') for x in grid])


print(make_seats(data, 5, count_seen_taken_seats))
print(make_seats(data, 4, count_adjacent_taken_seats))
