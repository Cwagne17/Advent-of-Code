# input_file = "example.txt"
input_file = "input.txt"

left_list = []
right_list = []

# Parse input file into two lists
for line in open(input_file):
    split = line.strip().split("   ")
    left_list.append(split[0])
    right_list.append(split[1])

# Sort each list
left_list.sort()
right_list.sort()

# Calculate distance between each pair of points
total_distance = 0
for i in range(len(left_list)):
    total_distance += abs(int(left_list[i]) - int(right_list[i]))

print("Part 1: ", total_distance)

## Part 2

simularity_score = 0
for value in left_list:
    appearences = right_list.count(value)
    simularity_score += appearences * int(value)

print("Part 2: ", simularity_score)
