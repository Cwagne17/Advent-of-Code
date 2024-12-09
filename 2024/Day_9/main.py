input_file = "example.txt"
# input_file = "input.txt"

expanded_disk_map = []
id_counter = 0
with open(input_file) as f:
    for i, c in enumerate(f.read()):
        if i % 2 == 0:
            for _ in range(int(c)):
                expanded_disk_map.append(id_counter)
            id_counter += 1
        else:
            for _ in range(int(c)):
                expanded_disk_map.append(".")


def move_file_blocks(filesystem):
    # Count the number of free spaces in the filesystem
    free_space = filesystem.count(".")

    optimized_filesystem = []
    from_back_index = -1
    for i in range(len(filesystem) - free_space):
        file_block = filesystem[i]

        # If the file block is empty, find the next non-empty file block
        # from the back of the filesystem
        if file_block == ".":
            # Find the next non-empty file block
            while filesystem[from_back_index] == ".":
                from_back_index -= 1

            optimized_filesystem.append(filesystem[from_back_index])
            from_back_index -= 1
            continue

        optimized_filesystem.append(file_block)

    return optimized_filesystem


def filesystem_checksum(filesystem):
    checksum = 0
    for i, value in enumerate(filesystem):
        checksum += i * int(value)
    return checksum


print("Part 1: ", filesystem_checksum(move_file_blocks(expanded_disk_map)))


# Part 2
# instead of moving file blocks using fragmented space, we can move the whole file


def move_files(filesystem):
    # Transform the filesystem to be a list of tuples with the common file block ids
    transformed_filesystem = []
    i = 0
    while i < len(filesystem) - 1:
        file_block = filesystem[i]
        whole_file = []

        while filesystem[i] == file_block:
            whole_file.append(file_block)
            i += 1

            # If we reach the end of the filesystem, break
            if i == len(filesystem):
                break

        transformed_filesystem.append(whole_file)

    optimized_filesystem = []
    from_back_index = -1
    i = 0
    while i < len(transformed_filesystem):
        # If the file block is not empty, move the whole file
        if transformed_filesystem[i][0] != ".":
            optimized_filesystem.append(transformed_filesystem[i])
            i += 1
            continue

        # The rest of this loop is for handling that position i is an empty
        # section of file blocks, this mean we can look for a non-empty file
        # from the back and start from i until from_back_index to look for a
        # free space to move the whole file

        # Get non-empty file from the back of the filesystem
        while (
            from_back_index < -len(transformed_filesystem)
            and transformed_filesystem[from_back_index][0] == "."
        ):
            from_back_index -= 1
        else:
            whole_file = transformed_filesystem[from_back_index]
            from_back_index -= 1

        # Find a free space in the filesystem where the whole file can be moved
        for j in range(i, len(transformed_filesystem) + from_back_index):
            if transformed_filesystem[j][0] == "." and len(
                transformed_filesystem[j]
            ) >= len(whole_file):
                # Move the whole file to the free space
                optimized_filesystem += whole_file

                # Update the filesystem to reflect the move
                i = j
                break

        i += 1

        # If the from_back_index has passed the i index, we can't move the file
        if len(transformed_filesystem) + from_back_index < i:
            break


print("Part 2: ", move_files(expanded_disk_map))
