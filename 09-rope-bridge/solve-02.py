#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
# in_file_name = "puzzle-input.txt"

import os
path = "/home/joswood/workspace/advent-of-code-2022/09-rope-bridge"
in_file_name = os.path.join(path, in_file_name)

# Holds (row, column) pair for head and tail of rope
ROPE_LENGTH = 10
rope_knots = [(0, 0)] * ROPE_LENGTH
rope_head_pos = rope_knots[0]
rope_tail_pos = rope_knots[ROPE_LENGTH - 1]

visited_tail_pos = [rope_tail_pos]

def move_knot_pair_one(direction, knot_head, knot_tail):
    # This will move the rope head one space in the given direction
    # and update the tail if needed

    new_head_pos_r = 0
    new_head_pos_c = 0
    tail_direction_r = 0
    tail_direction_c = 0

    if direction == "R":
        new_head_pos_r = knot_head[0]
        new_head_pos_c = knot_head[1] + 1

    elif direction == "D":
        new_head_pos_r = knot_head[0] + 1
        new_head_pos_c = knot_head[1]

    elif direction == "L":
        new_head_pos_r = knot_head[0]
        new_head_pos_c = knot_head[1] - 1

    elif direction == "U":
        new_head_pos_r = knot_head[0] - 1
        new_head_pos_c = knot_head[1]

    else:
        raise Exception(f"Invalid direction encountered {direction}")

    knot_head = (new_head_pos_r, new_head_pos_c)


    if knot_head[0] - knot_tail[0] > 1:
        tail_direction_r = 1

    elif knot_head[0] - knot_tail[0] < -1:
        tail_direction_r = -1

    if knot_head[1] - knot_tail[1] > 1:
        tail_direction_c = 1
    
    elif knot_head[1] - knot_tail[1] < -1:
        tail_direction_c = -1

    # Just check again for diagonal movements
    if tail_direction_c and knot_head[0] > knot_tail[0]:
        tail_direction_r = 1

    elif tail_direction_c and knot_head[0] < knot_tail[0]:
        tail_direction_r = -1

    if tail_direction_r and knot_head[1] > knot_tail[1]:
        tail_direction_c = 1

    elif tail_direction_r and knot_head[1] < knot_tail[1]:
        tail_direction_c = -1

    if tail_direction_c != 0 or tail_direction_r != 0:
        knot_tail = (knot_tail[0] + tail_direction_r, knot_tail[1] + tail_direction_c)

    return knot_head, knot_tail


with open(in_file_name) as rope_file:
    for move in rope_file:
        direction, distance_str = move.split()
        distance = int(distance_str)
        print(f"Moving {direction}, by {distance} spaces.")

        while distance > 0:
            for k in range(len(rope_knots) - 1):
                new_knot_head_pos, new_knot_tail_pos = move_knot_pair_one(direction, rope_knots[k], rope_knots[k + 1])

                rope_knots[k] = new_knot_head_pos
                distance -= 1

                if new_knot_tail_pos == rope_knots[k+1]:
                    break

                rope_knots[k+1] = new_knot_tail_pos
                

            print(f"Current tail pos is {rope_knots[ROPE_LENGTH - 1]}")
            if rope_knots[ROPE_LENGTH - 1] not in visited_tail_pos:
                visited_tail_pos.append(rope_knots[ROPE_LENGTH - 1])

print(f"List: {visited_tail_pos}")
print(f"The tail visited {len(visited_tail_pos)} spaces")