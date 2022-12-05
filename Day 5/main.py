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

def crate_mover_9000(count: int, source: str, dest: str):
    for i in range(count):
        crate = stack_dict[source].pop()
        stack_dict[dest].append(crate)

def crate_mover_9001(count: int, source: str, dest: str):
    crates = [stack_dict[source].pop() for i in range(count)]
    for crate in reversed(crates):
        stack_dict[dest].append(crate)

def print_top_crates():
    for value in stack_dict.values():
        print(value[-1], end="")

with open('input.txt') as fin:
    data = [ln.replace('\n', '') if ln != '\n' else ln for ln in fin.readlines()]
    procedures = data[data.index('\n')+1:]
    for procedure in procedures:
        steps = procedure.split()
        # crate_mover_9000(int(steps[1]), steps[3], steps[5])
        crate_mover_9001(int(steps[1]), steps[3], steps[5])
    print_top_crates()
    print()
    
    
    
    
    
    
    
        
        
            