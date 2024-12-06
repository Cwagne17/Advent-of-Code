from tqdm import tqdm

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

# Parse input file
with open(input_file) as f:
    for i, line in enumerate(f.readlines()):
        lab_map.append(list(line.strip()))
        if GUARD in lab_map[i]:
            starting_position = (lab_map[i].index(GUARD), i, DIRECTIONS[0])

# Update bounds
X_BOUND = len(lab_map[0])
Y_BOUND = len(lab_map)

# Part 1 - Patrol the lab


def get_next_position(current_position):
    x, y, direction = current_position
    dx, dy = direction
    next_x, next_y = x + dx, y + dy
    return next_x, next_y


def change_direction(direction):
    return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)]


def get_guard_positions(starting_position, lab_map=lab_map):
    current_position = starting_position
    guard_positions = [starting_position]

    while True:
        # Get the guards next position
        new_x, new_y = get_next_position(current_position)

        # Check if the guard is out of bounds
        if new_x < 0 or new_x >= X_BOUND or new_y < 0 or new_y >= Y_BOUND:
            break

        # Check if there is an obstruction in front of the guard
        if lab_map[new_y][new_x] == OBSTRUCTION:
            current_position = (
                current_position[0],
                current_position[1],
                change_direction(current_position[2]),
            )
        else:
            # Move the guard forward
            current_position = (new_x, new_y, current_position[2])

            # Check if there is a cycle
            if current_position in guard_positions:
                return None

            # Record the guard's position
            guard_positions.append(current_position)

    return guard_positions


# Get the guard's positions with original map
guard_positions = get_guard_positions(starting_position)

# Remove direction from the guard_positions
guard_positions_wo_direction = list(set((x, y) for x, y, _ in guard_positions))

print("Part 1: ", len(guard_positions_wo_direction))

# Part 2 - Find all places to place an obstruction to cause a loop

obstruction_positions = set()

# For each position the guard visited try and place an obstruction (excluding starting position)
for i in tqdm(
    range(1, len(guard_positions_wo_direction)), desc="Finding obstruction positions..."
):
    x, y = guard_positions_wo_direction[i]

    # Create a copy of the lab_map
    new_lab_map = [row.copy() for row in lab_map]

    # Place an obstruction
    new_lab_map[y][x] = OBSTRUCTION

    # Get the guard's positions with new map
    new_guard_positions = get_guard_positions(starting_position, new_lab_map)

    # If new guard positions is None, then we have a loop
    if new_guard_positions is None:
        obstruction_positions.add((x, y))

print("Part 2: ", len(list(obstruction_positions)))
