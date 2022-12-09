#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

import os
path = "/home/joswood/workspace/advent-of-code-2022/09-rope-bridge"
in_file_name = os.path.join(path, in_file_name)

# Holds (row, column) pair for head and tail of rope
rope_head_pos = (0, 0)
rope_tail_pos = (0, 0)

visited_tail_pos = [rope_tail_pos]

def move_rope_one(direction):
    # This will move the rope head one space in the given direction
    # and update the tail if needed
    global rope_head_pos
    global rope_tail_pos

    new_head_pos_r = 0
    new_head_pos_c = 0
    tail_direction_r = 0
    tail_direction_c = 0

    if direction == "R":
        new_head_pos_r = rope_head_pos[0]
        new_head_pos_c = rope_head_pos[1] + 1

    elif direction == "D":
        new_head_pos_r = rope_head_pos[0] + 1
        new_head_pos_c = rope_head_pos[1]

    elif direction == "L":
        new_head_pos_r = rope_head_pos[0]
        new_head_pos_c = rope_head_pos[1] - 1

    elif direction == "U":
        new_head_pos_r = rope_head_pos[0] - 1
        new_head_pos_c = rope_head_pos[1]

    else:
        raise Exception(f"Invalid direction encountered {direction}")

    rope_head_pos = (new_head_pos_r, new_head_pos_c)


    if rope_head_pos[0] - rope_tail_pos[0] > 1:
        tail_direction_r = 1

    elif rope_head_pos[0] - rope_tail_pos[0] < -1:
        tail_direction_r = -1

    if rope_head_pos[1] - rope_tail_pos[1] > 1:
        tail_direction_c = 1
    
    elif rope_head_pos[1] - rope_tail_pos[1] < -1:
        tail_direction_c = -1

    # Just check again for diagonal movements
    if tail_direction_c and rope_head_pos[0] > rope_tail_pos[0]:
        tail_direction_r = 1

    elif tail_direction_c and rope_head_pos[0] < rope_tail_pos[0]:
        tail_direction_r = -1

    if tail_direction_r and rope_head_pos[1] > rope_tail_pos[1]:
        tail_direction_c = 1

    elif tail_direction_r and rope_head_pos[1] < rope_tail_pos[1]:
        tail_direction_c = -1

    if tail_direction_c != 0 or tail_direction_r != 0:
        rope_tail_pos = (rope_tail_pos[0] + tail_direction_r, rope_tail_pos[1] + tail_direction_c)


with open(in_file_name) as rope_file:
    for move in rope_file:
        direction, distance_str = move.split()
        distance = int(distance_str)
        print(f"Moving {direction}, by {distance} spaces.")

        while distance > 0:
            move_rope_one(direction)
            distance -= 1

            print(f"Current tail pos is {rope_tail_pos}")
            if rope_tail_pos not in visited_tail_pos:
                visited_tail_pos.append(rope_tail_pos)

print(f"List: {visited_tail_pos}")
print(f"The tail visited {len(visited_tail_pos)} spaces")