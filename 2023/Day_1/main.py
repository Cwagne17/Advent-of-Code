import re


def part_one(input):
    sum = 0

    for line in input.splitlines():
        filtered_line = "".join([char for char in line if char.isdigit()])
        sum += int(f"{filtered_line[0]}{filtered_line[-1]}")

    return sum


def part_two(input):
    # Digits as strings
    digits = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    new_input = []

    for line in input.splitlines():
        ids = {}
        for value, digit in enumerate(
            digits[1:], 1
        ):  # Skip the empty string at index 0
            if digit in line:
                # Find all indices of the digit word
                indices = [m.start() for m in re.finditer(digit, line)]
                for index in indices:
                    ids[index] = str(value)

        num = ""
        for i, c in enumerate(line):
            if i in ids:
                num += ids[i]
                continue
            if c.isdigit():
                num += c

        new_input.append(num)

    sum_result = part_one("\n".join(new_input))
    return sum_result


digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt") as fin:
    input = fin.read()

    print("Part 1: ", part_one(input))
    print("Part 2: ", part_two(input))
