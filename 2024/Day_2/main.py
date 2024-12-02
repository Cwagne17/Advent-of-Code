input_file = "input.txt"
# input_file = "example.txt"

unusual_data = []
with open(input_file) as f:
    for report in f.readlines():
        unusual_data.append([int(level) for level in report.strip().split(" ")])


def safety_check(previous_level, current_level, previous_direction):
    # Check that the direction didn't change
    direction = -1 if current_level < previous_level else 1
    if previous_direction is not None and previous_direction != direction:
        return False, None

    # Any two adjacent levels differ by at least one and at most three
    magnitude = abs(current_level - previous_level)
    if magnitude < 1 or magnitude > 3:
        return False, None

    return True, direction


def test_report(report):
    direction = None
    safe = True

    # Starts with the second level in the report
    for i, level in enumerate(report[1:]):
        safe, direction = safety_check(report[i], level, direction)
        if not safe:
            break

    return safe


# Part 1

safe_reports = 0
for report in unusual_data:
    safe = test_report(report)

    if safe:
        safe_reports += 1

print("Part 1: ", safe_reports)

# Part 2
safe_reports = 0
problem_dampener_reports = []
for report in unusual_data:
    safe = test_report(report)

    if safe:
        safe_reports += 1
    else:
        problem_dampener_reports.append(report)

for report in problem_dampener_reports:
    # Try different combinations of removing one level from the report
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1 :]
        direction = None
        safe = True

        # Starts with the second level in the report
        for j, level in enumerate(new_report[1:]):
            safe, direction = safety_check(new_report[j], level, direction)
            if not safe:
                break

        if safe:
            safe_reports += 1
            break

print("Part 2: ", safe_reports)
