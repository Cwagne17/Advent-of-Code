import functools


def parse_input(data):
    return [(line.split()[0], int(line.split()[1])) for line in data]


def type_of_hand(hand):
    card_counts = {}
    type = 6

    for card in hand[0]:
        card_counts[card] = card_counts.get(card, 0) + 1

    for count in card_counts.values():
        if count == 5:
            type = 0  # five-of-a-kind
        elif count == 4:
            type = 1  # four-of-a-kind
        elif count == 3:
            type = 3  # three-of-a-kind
            if 2 in card_counts.values():
                type = 2  # full-house
        elif count == 2:
            if type == 6:
                type = 5  # one-pair
            elif 3 in card_counts.values():
                type = 2  # full-house
            elif list(card_counts.values()).count(2) == 2:
                type = 4  # two-pair

    return type


def find_min_hand(hand1, hand2):
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    hand1_type = type_of_hand(hand1)
    hand2_type = type_of_hand(hand2)

    if hand1_type == hand2_type:
        for i in range(5):
            if hand1[0][i] != hand2[0][i]:
                return -1 if cards.index(hand1[0][i]) > cards.index(hand2[0][i]) else 1

    return -1 if hand1_type > hand2_type else 1


def part_one(hands):
    winnings = 0

    hands = sorted(hands, key=functools.cmp_to_key(find_min_hand))
    for i, hand in enumerate(hands):
        winnings += hand[1] * (i + 1)
    return winnings


def type_of_hand_joker_rule(hand):
    card_counts = {}
    type = 6

    for card in hand[0]:
        card_counts[card] = card_counts.get(card, 0) + 1

    for card, count in card_counts.items():
        if card != "J":
            count += card_counts.get("J", 0)

        if count == 5:
            type = 0  # five-of-a-kind
            break
        elif count == 4:
            type = 1  # four-of-a-kind
            break
        elif count == 3:
            type = 3  # three-of-a-kind
            if 2 in card_counts.values():
                type = 2  # full-house
        elif count == 2:
            type = 5  # one-pair
            if 3 in card_counts.values():
                type = 2  # full-house
            elif list(card_counts.values()).count(2) == 2:
                type = 4  # two-pair
    return type


def find_min_hand_joker_rule(hand1, hand2):
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    hand1_type = type_of_hand_joker_rule(hand1)
    hand2_type = type_of_hand_joker_rule(hand2)

    if hand1_type == hand2_type:
        for i in range(5):
            card1 = hand1[0][i]
            card2 = hand2[0][i]

            # Use J as a wildcard
            if card1 == "J" and card2 != "J":
                card1 = max(
                    hand1[0], key=lambda x: cards.index(x)
                )  # Treat J as a wildcard
            elif card2 == "J" and card1 != "J":
                card2 = max(
                    hand2[0], key=lambda x: cards.index(x)
                )  # Treat J as a wildcard

            if card1 != card2:
                return -1 if cards.index(card1) > cards.index(card2) else 1

    return -1 if hand1_type > hand2_type else 1


def part_two(hands):
    winnings = 0

    hands = sorted(hands, key=functools.cmp_to_key(find_min_hand_joker_rule))
    for i, hand in enumerate(hands):
        winnings += hand[1] * (i + 1)
    return winnings


with open("example.txt") as f:
    hands = parse_input(f.read().splitlines())

    # print("Part 1 Example:", part_one(hands))
    print("Part 2 Example:", part_two(hands))

with open("input.txt") as f:
    hands = parse_input(f.read().splitlines())

    # print("Part 1:", part_one(hands))
    print("Part 2:", part_two(hands))
