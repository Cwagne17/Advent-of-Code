import re
from functools import reduce

input_file = "input.txt"
# input_file = "example.txt"


def repl(file, pattern):
    result = 0
    enabled = True
    for line in file.readlines():
        uncorrupted = re.findall(pattern, line)
        for match in uncorrupted:
            if match == "do()":
                enabled = True
            elif match == "don't()":
                enabled = False
            elif enabled:
                result += reduce(
                    lambda x, y: x * y,
                    [int(number) for number in match[4:-1].split(",")],
                )

    return result


with open(input_file) as f:
    print("Part 1: ", repl(f, r"mul\(\d\d?\d?,\d\d?\d?\)"))

    # Reset the file pointer
    f.seek(0)

    print("Part 2: ", repl(f, r"do\(\)|don't\(\)|mul\(\d\d?\d?,\d\d?\d?\)"))
