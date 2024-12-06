input_file = "input.txt"
# input_file = "example.txt"

# CONSTANTS
X_BOUND = 0
Y_BOUND = 0
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
GUARD = "^"
OBSTRUCTION = "#"

# Variables
lab_map = []
current_position = (0, 0)  # (x, y)
current_direction = DIRECTIONS[0]  # (dx, dy)
guard_positions = []


# Patrol protocol
# 1. If there is something directly in front of you, turn right 90 degrees.
# 2. Otherwise, take a step forward.

with open(input_file) as f:
    for i, line in enumerate(f.readlines()):
        lab_map.append(list(line.strip()))
        if GUARD in lab_map[i]:
            current_position = (lab_map[i].index(GUARD), i)
            current_direction = DIRECTIONS[0]
            guard_positions.append(current_position)

# Update bounds
X_BOUND = len(lab_map[0])
Y_BOUND = len(lab_map)

# Part 1 - Patrol the lab


def get_next_position(current_position, current_direction):
    x, y = current_position
    dx, dy = current_direction
    next_x, next_y = x + dx, y + dy
    return next_x, next_y


def check_obstruction(x, y):
    return lab_map[y][x] == OBSTRUCTION


def change_direction(direction):
    return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)]


while True:
    # Get the guards next position
    new_x, new_y = get_next_position(current_position, current_direction)
    # print(new_x, new_y, direction)

    # Check if the guard is out of bounds
    if new_x < 0 or new_x >= X_BOUND or new_y < 0 or new_y >= Y_BOUND:
        break

    # print(new_x, new_y, direction)
    # Check if there is an obstruction in front of the guard
    if check_obstruction(new_x, new_y):
        current_position = (
            current_position[0],
            current_position[1],
        )
        current_direction = change_direction(current_direction)
    else:
        # Move the guard forward
        current_position = (new_x, new_y)

        # Record the guard's position
        guard_positions.append(current_position)

print("Part 1: ", len(list(set(guard_positions))))
