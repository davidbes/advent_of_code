data = [(x.strip()[:1], int(x.strip()[1:]))
        for x in open("inputs/day_12.txt")]

#  N move north by the given value.
#  S move south by the given value.
#  E move east by the given value.
#  W move west by the given value.

#  L turn left the given number of degrees.
#  R turn right the given number of degrees.

#  F move forward by the given value in the direction the ship is currently facing.


def move_by_instructions(instructions):
    directions = {
        "N": (0, 1),
        "S": (0, -1),
        "E": (1, 0),
        "W": (-1, 0),
    }
    compass = {
        "R": ["N", "E", "S", "W"],
        "L": ["N", "W", "S", "E"]}

    current_e, current_n = (0, 0)
    facing = "E"
    for direction, value in instructions:
        if direction == "F":
            multiplier_e, multiplier_n = directions[facing]
            current_e += multiplier_e * value
            current_n += multiplier_n * value
        elif direction in directions:
            multiplier_e, multiplier_n = directions[direction]
            current_e += multiplier_e * value
            current_n += multiplier_n * value
        elif direction in {"L", "R"}:
            facing = compass[direction][(
                compass[direction].index(facing) + int(value / 90)) % 4]

    return abs(current_e) + abs(current_n)


# N move the waypoint north by the given value.
# S move the waypoint south by the given value.
# E move the waypoint east by the given value.
# W move the waypoint west by the given value.

# Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
# Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.

# Action F means to move forward to the waypoint a number of times equal to the given value.
def move_by_waypointing(instructions):

    directions = {
        "N": (0, 1),
        "S": (0, -1),
        "E": (1, 0),
        "W": (-1, 0),
    }

    ship_pos_e, shop_pos_n = (0, 0)
    wp_e, wp_n = (10, 1)

    for direction, value in instructions:
        # This moves ship
        if direction == "F":
            ship_pos_e += value * wp_e
            shop_pos_n += value * wp_n
        # Moves waypoint by this coords
        elif direction in directions:
            multiplier_e, multiplier_n = directions[direction]
            wp_e += multiplier_e * value
            wp_n += multiplier_n * value
        # Rotate waypoint
        elif direction in {"R", "L"}:
            if value == 180:
                wp_e, wp_n = -1 * wp_e, -1 * wp_n
            elif (direction == "R" and value == 90) or (direction == "L" and value == 270):
                wp_e, wp_n = wp_n, -1 * wp_e
            elif (direction == "L" and value == 90) or (direction == "R" and value == 270):
                wp_e, wp_n = -1 * wp_n, wp_e

    return abs(ship_pos_e) + abs(shop_pos_n)


print(move_by_instructions(data))
print(move_by_waypointing(data))
