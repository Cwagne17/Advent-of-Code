SYMBOLS = ["*", "+", "/", "$", "%", "@", "-", "=", "#"]

numbers = set()
symbols = set()

seen = set()


with open("input.txt") as fin:
    for i, row in enumerate(fin.read().splitlines()):
        potential_part_number = ""
        start = 0

        for j, column in enumerate(row):
            if column.isdigit():
                if potential_part_number == "":
                    start = j
                potential_part_number += column
            else:
                if column != ".":
                    symbols.add((i, j, column))

                if potential_part_number != "":
                    numbers.add(
                        (
                            i,
                            start,
                            start + len(potential_part_number) - 1,
                            potential_part_number,
                        )
                    )
                    potential_part_number = ""
                    start = 0

        if potential_part_number != "":
            numbers.add(
                (
                    i,
                    start,
                    start + len(potential_part_number) - 1,
                    potential_part_number,
                )
            )

    # Check if any part numbers are adjacent to symbols
    sum = 0
    part2_sum = 0
    for symbol in symbols:
        # Part 2
        parts = []
        for part in numbers:
            directions = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
                (1, 1),
                (1, -1),
                (-1, 1),
                (-1, -1),
            ]
            for x_offset, y_offset in directions:
                x = symbol[0] + x_offset
                y = symbol[1] + y_offset
                if x == part[0] and y >= part[1] and y <= part[2]:
                    seen.add(part)
                    parts.append(part)

        # Part 2
        # Check if the symbol is *
        parts = list(set(parts))
        if symbol[2] == "*" and len(parts) == 2:
            gear_ratio = int(parts[0][3]) * int(parts[1][3])
            part2_sum += gear_ratio


sum = 0
for part in seen:
    sum += int(part[3])
print(sum)

print(part2_sum)
