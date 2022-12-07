# I'll add comments later this is a mess

filesystem = {}
cwd = []

def get_dir_size(directory: str):
    return sum(filesystem[directory].values())

with open('input.txt') as fin:
    for ln in [ln.replace('\n', '') for ln in fin.readlines()]: # iterates over lines and filters out \n
        split_ln = ln.split(" ")
        
        # Case 1: Change Directory
        #   input format "$ cd directory"
        if ln.startswith("$ cd"):
            directory = split_ln[2] # gets directory name from line
            cwd.pop() if directory == ".." else cwd.append(directory) # uses cwd stack to track current working directory 
            abs_path = "/"+"/".join(cwd[1:]) # creates string identifier for cwd that is absolute path
            if abs_path not in filesystem: 
                filesystem[abs_path] = {} # initializes an empty dir with the abs_path
        
        # Case 2: File with size
        #   input format "number filename"
        elif split_ln[0].isnumeric():
            size, filename = split_ln
            if filename not in filesystem[abs_path]:
                filesystem[abs_path][filename] = int(size)

dir_sizes = {}
for k in filesystem.keys():
    subdirs = [directory for directory in filesystem.keys() if directory.startswith(k)]
    dir_sizes[k] = sum([get_dir_size(directory) for directory in subdirs])

print(sum([ v for v in dir_sizes.values() if v <= 100000])) # part 1
print(sorted(size for size in dir_sizes.values() if 30000000 - (70000000 - dir_sizes["/"]) < size)[0]) # part 2
        