# I'll add comments later this is a mess

filesystem = {}
cwd = []

def get_dir_size(directory: str):
    return sum(filesystem[directory].values())

with open('input.txt') as fin:
    for ln in [ln.replace('\n', '') for ln in fin.readlines()]:
        if ln.startswith("$ cd"):
            directory = ln.split(" ")[2]
            if directory == "..":
                cwd.pop()
            else:
                cwd.append(directory)
            absolute_path = "/"+"/".join(cwd[1:])
            if absolute_path not in filesystem:
                filesystem[absolute_path] = {}
        elif ln.split(" ")[0].isnumeric(): # catches if it is a file
            if ln.split(" ")[1] not in filesystem[absolute_path]:
                filesystem[absolute_path][ln.split(" ")[1]] = int(ln.split(" ")[0])

dir_sizes = {}
for k in filesystem.keys():
    subdirs = [directory for directory in filesystem.keys() if directory.startswith(k)]
    dir_sizes[k] = sum([get_dir_size(directory) for directory in subdirs])

print(sum([ v for v in dir_sizes.values() if v <= 100000])) # part 1
print(sorted(size for size in dir_sizes.values() if 30000000 - (70000000 - dir_sizes["/"]) < size)[0]) # part 2
        