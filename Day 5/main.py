stack_dict = {
    "1": ["D", "H", "N", "Q", "T", "W", "V", "B"],
    "2": ["D", "W", "B"],
    "3": ["T", "S", "Q", "W", "J", "C"],
    "4": ["F", "J", "R", "N", "Z", "T", "P"],
    "5": ["G", "P", "V", "J", "M", "S", "T"],
    "6": ["B", "W", "F", "T", "N"],
    "7": ["B", "L", "D", "Q", "F", "H", "V", "N"],
    "8": ["H", "P", "F", "R"],
    "9": ["Z", "S", "M", "B", "L", "N", "P", "H"],
}

def crate_mover_9000(n: int, source: str, dest: str):
    """Procedure that represents the crane moving one crate at a time from the source to the destination 'n' times.

    Args:
        n (int): The number of times the crane should move a crate from the source stack.
        source (str): The source stack of crates the crane should move from.
        dest (str): The destination stack of crates the crane should move to.
    """
    for i in range(n):
        crate = stack_dict[source].pop()
        stack_dict[dest].append(crate)

def crate_mover_9001(n: int, source: str, dest: str):
    """Procedure that represents the crane moving 'n' crates from the source stack to the destination stack.

    Args:
        n (int): The number of crates the crane should move at once.
        source (str): The source stack of crates the crane should move from.
        dest (str): The destination stack of crates the crane should move to.
    """
    crates = [stack_dict[source].pop() for i in range(n)]
    for crate in reversed(crates):
        stack_dict[dest].append(crate)

def print_top_crates():
    """Prints the last value (top) of each stack in order 1-9.
    """
    for value in stack_dict.values():
        print(value[-1], end="")
    print()

with open('input.txt') as fin:
    data = [ln.replace('\n', '') if ln != '\n' else ln for ln in fin.readlines()] # Reads in file removing \n from the end of lines, ignoring empty newlines
    procedures = data[data.index('\n')+1:] # Gets all procedures (after drawing)
    for procedure in procedures:
        steps = procedure.split() # format 'move n from source to dest'
        
        # Because the stack_dict data structure is manipulated by both functions only
        # one function can be used at a given time.
        # crate_mover_9000(int(steps[1]), steps[3], steps[5])
        crate_mover_9001(int(steps[1]), steps[3], steps[5])
    print_top_crates()
