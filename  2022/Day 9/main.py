previous = { ""}
HEAD = { "X": 0, "Y": 0 }
TAIL = { "X": 0, "Y": 0 }
tail_pos = []
head_pos = []

def move_tail():
    global TAIL
    x_diff = abs(HEAD["X"] - TAIL["X"])
    y_diff = abs(HEAD["Y"] - TAIL["Y"])
    if x_diff > 1 or y_diff > 1:
        TAIL = {"X": previous["X"], "Y": previous["Y"]}
    tail_pos.append({"X": TAIL["X"], "Y": TAIL["Y"]})

def move_head(direction: str, count: int):
    for i in range(count):
        global HEAD, previous
        previous = {"X": HEAD["X"], "Y": HEAD["Y"]}
        head_pos.append({"X": HEAD["X"], "Y": HEAD["Y"]})
        if direction == "U": # move up
            HEAD["Y"] += 1
        elif direction == "R": # move right
            HEAD["X"] += 1
        elif direction == "D": # move down
            HEAD["Y"] -= 1
        elif direction == "L": # move left
            HEAD["X"] -= 1
        move_tail()

with open('example2-input.txt') as fin:
    for ln in (ln.replace('\n', '') for ln in fin.readlines()):
        direction, count = ln.split(" ")
        move_head(direction, int(count))

print(len(set([tuple(pos.values()) for pos in tail_pos])))
    