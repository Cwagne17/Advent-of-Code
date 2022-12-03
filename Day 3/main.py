def getSharedItem(compartment1: str, compartment2: str):
    """Takes an elf's two compartments and returns the intersection. Assumes there is only one shared value.

    Args:
        compartment1 (str): First compartment of the rucksack
        compartment2 (str): Second compartment of the rucksack

    Returns:
        str: a str of len 1 is returned which represents the shared item in the rucksack's compartments. 
    """
    return list(set(compartment1).intersection(compartment2))[0]

def getGroupBadge(ruck1: str, ruck2: str, ruck3: str):
    """Takes three elves rucksacks and returns the shared badge. Assumes there is only one shared value amongst the three elves.

    Args:
        ruck1 (str): Rucksack of the first elf in the group
        ruck2 (str): Rucksack of the second elf in the group
        ruck3 (str): Rucksack of the third elf in the group

    Returns:
        str: a str of len 1 is returned which represents the shared badge in the evles rucksacks.
    """
    return list((set(ruck1).intersection(ruck2).intersection(ruck3)))[0]

def getPriority(item: str):
    """Takes a given item from a rucksack and returns the priority values of that item.
    If the item is upper case the offset from it's ASCII value is 38.
    If the item is lower case the offset from it's ASCII value is 96.

    Args:
        item (str): A str of len 1 which is between [a-zA-Z]

    Returns:
        int: an integer which represents the priority value of the item.
    """
    return ord(item)-96 if item.islower() else ord(item)-38

part1 = 0
part2 = 0
with open('input.txt') as fin:
    data = [ln.replace('\n', '') for ln in fin.readlines()] # removes newline character (previously each rucksack was odd length)
    for rucksack in data:
        part1 += getPriority(getSharedItem(rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]))
    print(part1)

    for group in list(zip(*[iter(data)]*3)):
        part2 += getPriority(getGroupBadge(list(group)[0], list(group)[1], list(group)[2]))
    print(part2)