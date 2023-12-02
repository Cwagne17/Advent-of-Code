X_reg = 1
clock_cycles = 0
signal_strengths = []
drawing = []

def inc_clock_cycle():
    """Increments the clock cycles by 1. Also checks the signal strength at given intervals."""
    global clock_cycles; clock_cycles += 1

    ## CRT position = (clock_cycles - 1) % 40
    ## Sprite position = range(X_reg-1, X_reg+1)
    drawing.append("#" if (clock_cycles-1) % 40 in list(range(X_reg-1, X_reg+2)) else ".") # part 2 CRT drawing
    
    if clock_cycles in [20, 60, 100, 140, 180, 220]: # part 1 signal strengths
        signal_strengths.append(clock_cycles * X_reg)

def noop():
    """"Takes one cycle to complete. It has no other effect."""
    inc_clock_cycle()

def addx(V: int):
    """Takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)

    Args:
        V (int): value to increase/decrease the X register by
    """
    inc_clock_cycle()
    inc_clock_cycle()
    global X_reg; X_reg += V

with open('input.txt') as fin:
    for ln in (ln.replace('\n', '') for ln in fin.readlines()):
        instruction = ln.split(" ")[0]
        if instruction == "addx":
            addx(int(ln.split(" ")[1]))
        elif instruction == "noop":
            noop()

print(signal_strengths)
print(sum(signal_strengths)) # Part 1
for i in range(6): # Part 2
    print("".join(drawing[i*40: (i+1)*40]))
