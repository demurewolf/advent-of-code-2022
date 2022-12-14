#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

# This just reads the damn file and creates a hashmap `device_structure` that
# contains the directorys and respective files on the current puzzle device
with open(in_file_name) as device_file:
    device_structure = {
        "/": {}
    }
    current_directory_key = None
    current_directory_structure = device_structure
    backtracking_keys = []

    for line in device_file:
        # print(f"Current directory: {current_directory_key}\n{current_directory_structure}\n{backtracking_keys}")
        if line.startswith("$"):
            # print(f"Found command: {line}")
            line_parts = line.split()
            command = line_parts[1]
            
            if command == "cd":
                arg = line_parts[2]

                if arg == "..":
                    # print("Need to go back one directory")
                    previous_structure = device_structure
                    for k in backtracking_keys:
                        if k:
                            previous_structure = previous_structure[k]

                    current_directory_key = backtracking_keys.pop()
                    current_directory_structure = previous_structure

                else:
                    backtracking_keys.append(current_directory_key)
                    new_key = current_directory_key + "/" + arg if current_directory_key else arg
                    current_directory_key = new_key
                    current_directory_structure = current_directory_structure[new_key]
                
        elif line.startswith("dir"):
            # print(f"Found directory: {line}")
            directory_name = line.split()[1]
            new_key = current_directory_key + "/" + directory_name
            current_directory_structure[new_key] = {}

        else:
            # print(f"Found a file: {line}")
            line_parts = line.split()
            current_directory_structure[line_parts[1]] = int(line_parts[0])

# print(f"{device_structure}")

directory_sizes = {}

# This function will return the size of the directory described by `struct` and named `struct_name`
def rec_find_directory_sizes(struct, struct_name):
    current_size = 0

    for k in struct:
        if type(struct[k]) is int:
            current_size += struct[k]

        else:
            current_size += rec_find_directory_sizes(struct[k], k)

    directory_sizes[struct_name] = current_size
    return current_size

rec_find_directory_sizes(device_structure, "/")
# print(directory_sizes)

# print(directory_sizes)

UPDATE_SIZE = 30000000
MAX_DEVICE_SIZE = 70000000

current_directory = "/"
current_size = directory_sizes["/"]

free_space = MAX_DEVICE_SIZE - current_size
space_to_delete = UPDATE_SIZE - free_space

print(f"Bytes to free for update: {space_to_delete}")

for dir_key, size in directory_sizes.items():
    # print(f"{dir_key}, {size}")
    if size < current_size and size >= space_to_delete:
        current_size = size
        current_directory = dir_key

print(f"Smallest directory to delete: {current_directory} with {current_size} bytes to delete")