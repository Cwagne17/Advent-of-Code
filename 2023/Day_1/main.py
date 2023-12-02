input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

input_sum = 0
with open("input.txt") as fin:
    input = fin.read()
    for line in input.splitlines():
        calibration_value = "".join([char for char in line if not char.isalpha()])
        input_sum += int(f"{calibration_value[0]}{calibration_value[-1]}")
print("Part 1: ", input_sum)

input_sum = 0
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def replace_digit_with_position(line, digit, position):
    return line.replace(digit, str(position))


with open("input.txt") as fin:
    for line in fin.read().splitlines():
        # Replace digits with words
        for char in line:
            if char.isdigit():
                line = line.replace(char, digits[int(char) - 1])

        line_indexes = []
        for digit in digits:
            try:
                for i in range(len(line)):
                    line_indexes.append((line.index(digit), digit))
            except ValueError:
                pass
        line_indexes.sort()

        first = line_indexes[0]
        last = line_indexes[-1]

        first_value = digits.index(first[1]) + 1
        last_value = digits.index(last[1]) + 1
        calibration_value = f"{first_value}{last_value}"
        input_sum += int(calibration_value)

print("Part 2: ", input_sum)
