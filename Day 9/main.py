HEAD = { "X": 0, "Y": 0 }
TAIL = { "X": 0, "Y": 0 }

def move_tail():
    pass

def move_head(direction: str, count: int):
    for i in range(count):
        if direction == "U": # move up
            HEAD["Y"] += 1
        elif direction == "R": # move right
            HEAD["X"] += 1
        elif direction == "D": # move down
            HEAD["Y"] -= 1
        elif direction == "L": # move left
            HEAD["X"] -= 1
        print(HEAD)
        move_tail()

with open('input.txt') as fin:
    for ln in (ln.replace('\n', '') for ln in fin.readlines()):
        direction, count = ln.split(" ")
        move_head(direction, int(count))