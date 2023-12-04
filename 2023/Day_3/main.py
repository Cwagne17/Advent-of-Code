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
                    symbols.add((i, j, column))

                if potential_part_number != "":
                    numbers.add((i, local_j, potential_part_number))
                    potential_part_number = ""

    # Check if any part numbers are adjacent to symbols
    for symbol in symbols:
        for part in numbers:
            for iter in range(len(part[2])):
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
                    for k in range(len(part[2])):
                        if (
                            part[0] + x_offset,
                            part[1] + iter + y_offset,
                            symbol[2],
                        ) == symbol:
                            flag = True
                            break

                if flag:
                    if part not in seen:
                        seen.add(part)

sum = 0
for part in seen:
    sum += int(part[2])
print(sum)
