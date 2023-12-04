SYMBOLS = ["&", "+", "/", "$", "%", "*", "@", "-", "=", "#"]


def check_for_adjacent_part_numbers(lines, i, j, direction=1):
    local_j = j
    part_number = ""

    while 0 <= local_j < len(lines[i]) and lines[i][local_j].isdigit():
        part_number = (
            lines[i][local_j] + part_number
            if direction == -1
            else part_number + lines[i][local_j]
        )
        local_j += direction

    return part_number, local_j - direction


def check_left_right(lines, i, j):
    parts = []

    directions = [
        (0, 1, 1),  # Right
        (0, -1, -1),  # Left
    ]

    for direction in directions:
        x_offset, y_offset, x_direction = direction
        part_number, local_j = check_for_adjacent_part_numbers(
            lines, i + x_offset, j + y_offset, x_direction
        )

        if part_number:
            parts.append((i, local_j, part_number))

    return parts


part_numbers = set()

with open("example.txt") as f:
    lines = f.read().splitlines()

    for i, row in enumerate(lines):
        for j, column in enumerate(row):
            # Check if the current character is a symbol
            if column in SYMBOLS:
                # Check if the character left and right of the symbol is a part number
                parts = check_left_right(lines, i, j)
                for part in parts:
                    if part not in part_numbers:
                        part_numbers.add(part)

                # Check up

                upper_right_part_number, local_j1 = check_for_adjacent_part_numbers(
                    lines, i - 1, j + 1
                )
                upper_left_part_number, local_j2 = check_for_adjacent_part_numbers(
                    lines, i - 1, j - 1, -1
                )

                if lines[i - 1][j].isdigit():
                    part_number = (
                        upper_left_part_number
                        + lines[i - 1][j]
                        + upper_right_part_number
                    )
                    part_numbers.add((i - 1, local_j2, part_number))
                elif (
                    upper_left_part_number
                    and (i - 1, local_j2, upper_left_part_number) not in part_numbers
                ):
                    part_numbers.add((i - 1, local_j2, upper_left_part_number))
                elif (
                    upper_right_part_number
                    and (i - 1, local_j1, upper_right_part_number) not in part_numbers
                ):
                    part_numbers.add((i - 1, local_j1, upper_right_part_number))

                # Check down

                lower_right_part_number, local_j1 = check_for_adjacent_part_numbers(
                    lines, i + 1, j + 1
                )
                lower_left_part_number, local_j2 = check_for_adjacent_part_numbers(
                    lines, i + 1, j - 1, -1
                )

                if lines[i + 1][j].isdigit():
                    part_number = (
                        lower_left_part_number
                        + lines[i + 1][j]
                        + lower_right_part_number
                    )
                    part_numbers.add((i + 1, local_j2, part_number))
                elif (
                    lower_left_part_number
                    and (i + 1, local_j2, lower_left_part_number) not in part_numbers
                ):
                    part_numbers.add((i + 1, local_j2, lower_left_part_number))
                elif (
                    lower_right_part_number
                    and (i + 1, local_j1, lower_right_part_number) not in part_numbers
                ):
                    part_numbers.add((i + 1, local_j1, lower_right_part_number))

    for part in part_numbers:
        print(part)
    # sum = 0
    # for i, j, part_number in list(part_numbers):
    #     print(part_number)
    #     sum += int(part_number)
    # print(sum)
