SYMBOLS = ["*", "+", "/", "$", "%", "@", "-", "=", "#"]

numbers = set()
symbols = set()

seen = set()

with open("input.txt") as fin:
    for i, row in enumerate(fin.read().splitlines()):
        potential_part_number = ""
        local_j = 0

        for j, column in enumerate(row):
            if column.isdigit():
                if potential_part_number == "":
                    local_j = j
                potential_part_number += column
            else:
                if column in SYMBOLS:
                    symbols.add((i, j, j, column))

                if potential_part_number != "":
                    numbers.add(
                        (
                            i,
                            local_j,
                            local_j + len(potential_part_number) - 1,
                            potential_part_number,
                        )
                    )
                    potential_part_number = ""

    # Check if any part numbers are adjacent to symbols
    for symbol in symbols:
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
            flag = False
            for x_offset, y_offset in directions:
                if symbol[0] + x_offset == part[0] and symbol[1] + y_offset in range(
                    part[1], part[2] + 1
                ):
                    flag = True

            if flag:
                if part not in seen:
                    seen.add(part)

sum = 0
for part in seen:
    sum += int(part[3])
print(sum)
