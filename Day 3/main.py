def getSharedItem(compartment1: str, compartment2: str):
    return list(set(compartment1).intersection(compartment2))[0]

def getGroupBadge(ruck1: str, ruck2: str, ruck3: str):
    return list((set(ruck1).intersection(ruck2).intersection(ruck3)))[0]

def getPriority(item: str):
    return ord(item)-96 if item.islower() else ord(item)-38

part1 = 0
part2 = 0
with open('input.txt') as fin:
    data = [ln.replace('\n', '') for ln in fin.readlines()]
    for rucksack in data:
        part1 += getPriority(getSharedItem(rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]))
    print(part1)

    for group in list(zip(*[iter(data)]*3)):
        part2 += getPriority(getGroupBadge(list(group)[0], list(group)[1], list(group)[2]))
    print(part2)