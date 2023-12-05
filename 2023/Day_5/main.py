import json


def parse_input(puzzle_input):
    almanac = {}

    almanac["seeds"] = puzzle_input[0].split(":")[1].split()

    source = ""
    for line in puzzle_input[1:]:
        if line == "":
            continue

        if line[0].isalpha():
            source, _, destination = line.split()[0].split("-")
            almanac[source] = {"destination": destination, "items": []}
        else:
            almanac[source]["items"].append(line.split())

    return almanac


def map_source_to_destination(almanac, source, value):
    destination = almanac[source]["destination"]

    for dest_range_start, source_range_start, range_length in almanac[source]["items"]:
        if (
            int(source_range_start)
            <= int(value)
            <= int(source_range_start) + int(range_length)
        ):
            value = int(dest_range_start) + int(value) - int(source_range_start)
            break

    if destination == "location":
        return value

    return map_source_to_destination(almanac, destination, value)


def part_one(almanac):
    locations = []

    for seed in almanac["seeds"]:
        value = map_source_to_destination(almanac, "seed", seed)

        locations.append(value)
    return min(locations)


def map_seed_range_to_destination(almanac, source, seed_range_start, seed_range_end):
    destination = almanac[source]["destination"]

    mappings = []
    remaining_ranges = [(seed_range_start, seed_range_end)]

    for dest_range_start, source_range_start, range_length in almanac[source]["items"]:
        source_start = int(source_range_start)
        source_end = source_start + int(range_length)
        diff = int(dest_range_start) - source_start

        # print("Source Range:", source_start, source_end)
        # print("Mappings:", mappings)
        # print("Remaining Ranges:", remaining_ranges)

        new_remaining_ranges = []

        for seed_start, seed_end in remaining_ranges:
            # Check for overlap between seed range and source range
            if seed_end < source_start or seed_start > source_end:
                # No overlap, add entire seed range to new_remaining_ranges
                new_remaining_ranges.append((seed_start, seed_end))
            else:
                # Calculate the overlapping part of the ranges
                overlap_start = max(seed_start, source_start)
                overlap_end = min(seed_end, source_end)
                # Add the mapped overlapping range to mappings
                mappings.append((overlap_start + diff, overlap_end + diff))

                # Add the non-overlapping parts to new_remaining_ranges
                if seed_start < source_start:
                    new_remaining_ranges.append((seed_start, overlap_start - 1))
                if seed_end > source_end:
                    new_remaining_ranges.append((overlap_end + 1, seed_end))

        remaining_ranges = new_remaining_ranges

    mappings.extend(remaining_ranges)

    if destination == "location":
        print(mappings)
        return min(mappings, key=lambda x: x[0])[0]

    # For each left-over seed range, it did not overlap with any source range
    # therefore it keeps its original value
    locations = [
        map_seed_range_to_destination(almanac, destination, start, end)
        for start, end in mappings
    ]

    return min(locations)


def part_two(almanac):
    locations = []

    for start, length in zip(almanac["seeds"][::2], almanac["seeds"][1::2]):
        seed_start = int(start)
        seed_end = seed_start + int(length)

        locations.append(
            map_seed_range_to_destination(almanac, "seed", seed_start, seed_end)
        )

    return min(locations)


with open("example.txt") as f:
    puzzle_input = f.read().splitlines()

    almanac = parse_input(puzzle_input)
    # print("Part 1 Example:", part_one(almanac))
    print("Part 2 Example:", part_two(almanac))

with open("input.txt") as f:
    puzzle_input = f.read().splitlines()

    almanac = parse_input(puzzle_input)
    # print("Part 1:", part_one(almanac))
    # print("Part 2:", part_two(almanac))
