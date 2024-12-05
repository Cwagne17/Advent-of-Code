input_file = "input.txt"
# input_file = "example.txt"

# Rules is a map of X -> [Y, Y, Y] that means X has to be before all Ys
# this can be used when searching in a list, lookup X and check if all
# Ys have not be seen yet when iterating through the list
rules = {}
updates = []

with open(input_file) as f:
    for line in [line.strip() for line in f.readlines()]:
        if "|" in line:
            x, y = line.split("|")
            if x not in rules:
                rules[x] = []
            rules[x].append(y)

        if "," in line:
            updates.append(line.split(","))


# Part 1 - Find correct updates


def satisfies_rule(rule, seen):
    for required in rules.get(rule, []):
        if required in seen:
            return False
    return True


middle_page_number_sum = 0
for update in updates:
    seen = []

    correct = True
    for page in update:
        if not satisfies_rule(page, seen):
            correct = False

        seen.append(page)

        if not correct:
            break

    if correct:
        middle_index = len(update) // 2
        middle_page_number_sum += int(update[middle_index])

print("Part 1: ", middle_page_number_sum)

# Part 2 - Correct incorrect updates

middle_page_number_sum = 0
for update in updates:

    valid_update = []
    needs_correction = False
    for i, page in enumerate(update):
        # This is the case where the page is not valid
        # this means the page needs to be place before the first
        # page that is in it's rules
        index = []
        for required_after in rules.get(page, []):
            if required_after in valid_update:
                needs_correction = True
                index.append(valid_update.index(required_after))

        else:
            if index:
                valid_update.insert(min(index), page)
            else:
                valid_update.append(page)
    if needs_correction:
        middle_index = len(valid_update) // 2
        middle_page_number_sum += int(valid_update[middle_index])

print("Part 2: ", middle_page_number_sum)
