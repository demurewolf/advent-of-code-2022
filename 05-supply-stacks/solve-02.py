#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

def setup():
    if "test" in in_file_name:
        crates = [
            ["Z", "N"],
            ["M", "C", "D"],
            ["P"]
        ]
        lines_to_skip = 5

    else:
    #     [H]         [H]         [V]    
    #     [V]         [V] [J]     [F] [F]
    #     [S] [L]     [M] [B]     [L] [J]
    #     [C] [N] [B] [W] [D]     [D] [M]
    # [G] [L] [M] [S] [S] [C]     [T] [V]
    # [P] [B] [B] [P] [Q] [S] [L] [H] [B]
    # [N] [J] [D] [V] [C] [Q] [Q] [M] [P]
    # [R] [T] [T] [R] [G] [W] [F] [W] [L]

        crates = [
            ["R", "N", "P", "G"],
            ["T", "J", "B", "L", "C", "S", "V", "H"],
            ["T", "D", "B", "M", "N", "L"],
            ["R", "V", "P", "S", "B"],
            ["G", "C", "Q", "S", "W", "M", "V", "H"],
            ["W", "Q", "S", "C", "D", "B", "J"],
            ["F", "Q", "L"],
            ["W", "M", "H", "T", "D", "L", "F", "V"],
            ["L", "P", "B", "V", "M", "J", "F"]
        ]
        lines_to_skip = 10

    return crates, lines_to_skip

with open(in_file_name) as crane_file:
    crates, lines_to_skip = setup()

    for s in range(lines_to_skip):
        crane_file.readline()

    for crane_move in crane_file:
        parsed_move = crane_move.split()
        num_to_move = int(parsed_move[1])
        from_stack = int(parsed_move[3]) - 1
        to_stack = int(parsed_move[5]) - 1
        
        crates[to_stack].extend(crates[from_stack][-num_to_move:])
        for c in range(num_to_move):
            crates[from_stack].pop()

        # print(f"{crates}")

tops = ""

for stack in crates:
    try:
        tops += stack.pop()
    except IndexError:
        print("Empty stack here")

print(f"The elves can predict {tops} on the top of each stack")
