def parse_scratchcard(scratchcard):
    winning_numbers, game_numbers = scratchcard[scratchcard.index(":") :].split("|")

    game_numbers = list(filter(None, game_numbers.split(" ")))
    winning_numbers = list(filter(None, winning_numbers.split(" ")))

    return game_numbers, winning_numbers


def find_matches(numbers, winning_numbers):
    return sum([numbers.count(winning_number) for winning_number in winning_numbers])


def score(matches):
    return (2 ** (matches - 1)) if matches > 0 else 0


def part_one(scratchcards):
    prize = 0
    for scratchcard in scratchcards:
        game_numbers, winning_numbers = parse_scratchcard(scratchcard)

        winning_number_appearances = find_matches(game_numbers, winning_numbers)

        prize += score(winning_number_appearances)
    return prize


def part_two(scratchcards):
    winning_tracker = [0] * len(scratchcards)

    for scratchcard in scratchcards:
        game_number_index = (
            int(scratchcard[scratchcard.index(" ") + 1 : scratchcard.index(":")]) - 1
        )

        game_numbers, winning_numbers = parse_scratchcard(scratchcard)

        winning_number_appearances = find_matches(game_numbers, winning_numbers)

        winning_tracker[game_number_index] = winning_number_appearances

    # Iterate backwards through the winning tracker
    for i in range(len(winning_tracker) - 1, -1, -1):
        winning_tracker[i] += sum(
            winning_tracker[i + j + 1] for j in range(winning_tracker[i])
        )

    return sum(winning_tracker) + len(scratchcards)


with open("example.txt") as f:
    scratchcards = f.read().splitlines()

    print("Part 1 Example:", part_one(scratchcards))
    print("Part 2 Example:", part_two(scratchcards))

with open("input.txt") as f:
    scratchcards = f.read().splitlines()

    print("Part 1:", part_one(scratchcards))
    print("Part 2:", part_two(scratchcards))
