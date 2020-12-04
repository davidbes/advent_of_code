data = [x.strip()for x in open("inputs/day_3.txt")]


def task_one(data, slope, down):
    row_multiplier = 1
    collisions = 0
    for index, row in enumerate(data[::down]):
        collisions += (row_multiplier * row)[slope * index] == "#"
        row_multiplier += len(row_multiplier * row) - slope <= (slope * index)
    return collisions


def task_two(data, slopes_and_downs):
    values = []
    multiply = 1
    for slope, down in slopes_and_downs:
        result = task_one(data, slope, down)
        values.append(result)
        multiply *= result
    return values, multiply


print(task_one(data, 3, 1))
print(task_two(data, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
