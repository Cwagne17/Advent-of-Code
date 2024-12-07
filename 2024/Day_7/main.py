input_file = "input.txt"
# input_file = "example.txt"

equations = {}
with open(input_file) as f:
    for equation in [line.strip() for line in f.readlines()]:
        colon_index = equation.index(":")
        test_value = int(equation[:colon_index])
        operands = [int(op) for op in equation[colon_index + 2 :].split(" ")]

        equations[test_value] = operands


def recursive_solve(test_value, operands):
    """Recursively solve the equation"""
    if len(operands) == 1:
        return operands[0] == test_value

    # Two branches of the recursion tree
    # One will try to add the first two operands and then recursively solve the rest
    # The other will try to multiply the first two operands and then recursively solve the rest
    new_added_operands = [operands[0] + operands[1]] + operands[2:]
    new_multiplied_operands = [operands[0] * operands[1]] + operands[2:]
    new_concatendated_operands = [int(str(operands[0]) + str(operands[1]))] + operands[
        2:
    ]

    return (
        recursive_solve(test_value, new_added_operands)
        or recursive_solve(test_value, new_multiplied_operands)
        # Comment this line out to solve part 1
        or recursive_solve(test_value, new_concatendated_operands)
    )


total_calibration_results = 0

for test_value, operands in equations.items():
    if recursive_solve(test_value, operands):
        total_calibration_results += test_value

print(total_calibration_results)
