import numpy as np

def expandAssignmentRange(assignment: str):
    """Takes an assignment and expands the range to return a set of assignment IDs.

    Args:
        assignment (str): A section assignment in the form of a range (d-d)

    Returns:
        set: A set of all values included in the range.
    """
    range_list = assignment.split('-')
    return set(np.arange(int(range_list[0]), int(range_list[1])+1))

def checkCompleteSubset(assignment1: set, assignment2: set):
    """Takes two section assignments and returns whether one assignment is a subset of the other.

    Args:
        assignment1 (set): A section assignment that is an expanded set
        assignment2 (set): A section assignment that is an expanded set

    Returns:
        bool: True if one of the assignments is a subset of the other. False otherwise.
    """
    return assignment1.issubset(assignment2) or assignment2.issubset(assignment1)

def checkOverlap(assignment1: set, assignment2: set):
    """Takes two section assignments and returns whether there is an intersection between the two assignments.

    Args:
        assignment1 (set): A section assignment that is an expanded set
        assignment2 (set): A section assignment that is an expanded set

    Returns:
        bool: True if an intersection occurs. False otherwise.
    """
    return len(list(assignment1.intersection(assignment2))) > 0

part1 = 0
part2 = 0
with open('input.txt') as fin:
    for ln in fin.readlines():
        ln = ln.replace('\n', '') # remove \n from ln
        pair = ln.split(',') # splits the ranged section assignments
        if checkCompleteSubset(expandAssignmentRange(pair[0]), expandAssignmentRange(pair[1])):
            part1 += 1
        if checkOverlap(expandAssignmentRange(pair[0]), expandAssignmentRange(pair[1])):
            part2 += 1
    print(part1)
    print(part2)
                