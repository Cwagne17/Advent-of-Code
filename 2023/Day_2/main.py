def part_one(input, red, green, blue):
    total_sum = 0

    for line in input:
        game_number, cubes_list = line.split(": ")
        game_number = int(game_number.split(" ")[1])

        flag = all(
            int(count) <= red
            if color == "red"
            else int(count) <= green
            if color == "green"
            else int(count) <= blue
            for handful in cubes_list.split("; ")
            for count, color in (cube.split(" ") for cube in handful.split(", "))
        )

        if flag:
            total_sum += game_number

    return total_sum


def part_two(input):
    sum = 0

    for line in input:
        red_max = 1
        green_max = 1
        blue_max = 1

        game = line.split(": ")

        game_number = game[0].split(" ")[1]

        for handful in game[1].split("; "):
            for cubes in handful.split(", "):
                count = cubes.split(" ")[0]
                color = cubes.split(" ")[1]

                if color == "red" and int(count) > red_max:
                    red_max = int(count)
                elif color == "green" and int(count) > green_max:
                    green_max = int(count)
                elif color == "blue" and int(count) > blue_max:
                    blue_max = int(count)

        power = red_max * green_max * blue_max
        sum += int(power)

    return sum


with open("part1-example.txt") as fin:
    print("Part 1 Example:", part_one(fin.read().splitlines(), 12, 13, 14))

with open("input.txt") as fin:
    print("Part 1:", part_one(fin.read().splitlines(), 12, 13, 14))

with open("part1-example.txt") as fin:
    print("Part 2 Example:", part_two(fin.read().splitlines()))

with open("input.txt") as fin:
    print("Part 2:", part_two(fin.read().splitlines()))
