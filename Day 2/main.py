def evalRound(opp: str, mine: str):
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

total = 0
with open('input.txt') as fin:
    for ln in fin.readlines():
        total += evalRound(ln.split()[0], ln.split()[1])
print(total)