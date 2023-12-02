# Function for part 1 of Day 2
def strategy_guide(opp: str, mine: str):
    """Uses the arguments to determine the points achieved in a given round using a dictionary.

    Args:
        opp (str): the opponent's decision 'A' | 'B' | 'C'
        mine (str): the play I should make 'X' | 'Y' | 'Z'

    Returns:
        int: the total points accquired in the round
    """
    decision_pnts = {
        "A": {      # Rock
            "X": 4, # Rock      1 + 3
            "Y": 8, # Paper     2 + 6
            "Z": 3  # Scissors  3 + 0
        },
        "B": {      # Paper
            "X": 1, # Rock      1 + 0
            "Y": 5, # Paper     2 + 3
            "Z": 9  # Scissors  3 + 6
        },
        "C": {      # Scissors
            "X": 7, # Rock      1 + 6
            "Y": 2, # Paper     2 + 0
            "Z": 6  # Scissors  3 + 3
        }
    }
    return decision_pnts[opp][mine]

# Function for part 2 of Day 2
def ultra_top_secret_startegy_guide(opp: str, mine: str):
    """Uses the arguments to determine the points achieved in a given round using a dictionary.

    Args:
        opp (str): the opponent's decision 'A' | 'B' | 'C'
        mine (str): the play I should make 'X' | 'Y' | 'Z'

    Returns:
        int: the total points accquired in the round
    """
    decision_pnts = {
        "A": {      # Rock
            "X": 3, # Lose  (Scissors)  3 + 0
            "Y": 4, # Draw  (Rock)      1 + 3
            "Z": 8  # Win   (Paper)     2 + 6
        },
        "B": {      # Paper
            "X": 1, # Lose  (Rock)      1 + 0
            "Y": 5, # Draw  (Paper)     2 + 3
            "Z": 9  # Win   (Scissors)  3 + 6
        },
        "C": {      # Scissors
            "X": 2, # Lose  (Paper)     2 + 0
            "Y": 6, # Draw  (Scissors)  3 + 3
            "Z": 7  # Win   (Rock)      1 + 6
        }
    }
    return decision_pnts[opp][mine]

part_1 = 0
part_2 = 0
with open('input.txt') as fin:
    for ln in fin.readlines():
        part_1 += strategy_guide(ln.split()[0], ln.split()[1])
        part_2 += ultra_top_secret_startegy_guide(ln.split()[0], ln.split()[1])
print(part_1)
print(part_2)