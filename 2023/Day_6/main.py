from math import prod
from math import isqrt
import time as t


def parse_input_for_part_one(data):
    times = data[0].split()[1:]
    distances = data[1].split()[1:]

    return [(int(times[i]), int(distances[i])) for i in range(len(times))]


def parse_input_for_part_two(data):
    return [
        (
            int("".join(data[0].split()[1:])),
            int("".join(data[1].split()[1:])),
        )
    ]


def part_one_quadratic(races):
    race_numbers_of_ways = []

    start_time = t.time_ns()

    for time, distance in races:
        # Calculate the discriminant
        discriminant = time**2 - 4 * distance

        # Check if the discriminant is non-negative
        if discriminant >= 0:
            # Calculate the number of ways using integer square root
            ways = isqrt(discriminant)
            race_numbers_of_ways.append(ways)
        else:
            # If the discriminant is negative, no real roots, append 0
            race_numbers_of_ways.append(0)

    print("Time:", t.time_ns() - start_time, "ns")
    return prod(race_numbers_of_ways)


def part_one(races):
    race_number_of_ways = []
    start_time = t.time_ns()

    for time, distance in races:
        number_of_ways = 0

        # Iterate through the first half of possible times
        # of holding the button
        for i in range((time // 2) + 1):
            time_not_holding_button = time - i
            velocity = i

            # If the distance is greater than the distance
            # that can be traveled in the time not holding
            # the button, set the number of ways to the
            # difference between the
            if time_not_holding_button * velocity > distance:
                number_of_ways = (time // 2) - i + 1
                break

        # Because the number of ways is mirrored, multiply
        # by two and subtract one if the time is even
        # or just multiply by two if the time is odd
        if time % 2 == 0:
            number_of_ways = number_of_ways * 2 - 1
        else:
            number_of_ways *= 2

        race_number_of_ways.append(number_of_ways)

    print("Time:", t.time_ns() - start_time, "ns")
    return prod(race_number_of_ways)


with open("example.txt") as f:
    data = f.read().splitlines()

    print("Part 1 Example:", part_one(parse_input_for_part_one(data)))
    print(
        "Part 1 Example Quadratic:", part_one_quadratic(parse_input_for_part_one(data))
    )
    print("Part 2 Example:", part_one(parse_input_for_part_two(data)))
    print(
        "Part 2 Example Quadratic:", part_one_quadratic(parse_input_for_part_two(data))
    )

with open("input.txt") as f:
    data = f.read().splitlines()

    print("Part 1:", part_one(parse_input_for_part_one(data)))
    print("Part 1 Quadratic:", part_one_quadratic(parse_input_for_part_one(data)))
    print("Part 2:", part_one(parse_input_for_part_two(data)))
    print("Part 2 Quadratic:", part_one_quadratic(parse_input_for_part_two(data)))
