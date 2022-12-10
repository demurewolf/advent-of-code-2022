#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

# import os
# path = "/home/joswood/workspace/advent-of-code-2022/09-rope-bridge"
# in_file_name = os.path.join(path, in_file_name)

# Holds (row, column) pair for head and tail of rope
ROPE_LENGTH = 10
rope_knots = [(0, 0)] * ROPE_LENGTH
rope_head_pos = rope_knots[0]
rope_tail_pos = rope_knots[ROPE_LENGTH - 1]

visited_tail_pos = [rope_tail_pos]


# Checks if knot2 is too far away from knot1
def knots_are_too_far(knot1, knot2):
    (k1_r, k1_c) = knot1
    (k2_r, k2_c) = knot2

    return abs(k1_r - k2_r) > 1 or abs(k1_c - k2_c) > 1


# This function only moves the second knot if the first is too far away
def rec_following_knots_one(k_index):
    if k_index >= ROPE_LENGTH - 1:
        return

    knot1 = rope_knots[k_index]
    knot2 = rope_knots[k_index + 1]

    tail_direction_r = 0
    tail_direction_c = 0

    if knots_are_too_far(knot1, knot2):
        if knot1[0] - knot2[0] > 1:
            tail_direction_r = 1

        elif knot1[0] - knot2[0] < -1:
            tail_direction_r = -1

        if knot1[1] - knot2[1] > 1:
            tail_direction_c = 1

        elif knot1[1] - knot2[1] < -1:
            tail_direction_c = -1

        # Just check again for diagonal movements
        if tail_direction_c and knot1[0] > knot2[0]:
            tail_direction_r = 1

        elif tail_direction_c and knot1[0] < knot2[0]:
            tail_direction_r = -1

        if tail_direction_r and knot1[1] > knot2[1]:
            tail_direction_c = 1

        elif tail_direction_r and knot1[1] < knot2[1]:
            tail_direction_c = -1

        if tail_direction_c or tail_direction_r:
            rope_knots[k_index + 1] = (knot2[0] + tail_direction_r, knot2[1] + tail_direction_c)

        return rec_following_knots_one(k_index + 1)

    else:
        # No need to move the rest of the knot rope
        return


with open(in_file_name) as rope_file:
    for move in rope_file:
        direction, distance_str = move.split()
        distance = int(distance_str)
        print(f"Moving {direction}, by {distance} spaces.")

        while distance > 0:
            # A mapping form direction ->
            rope_head_mover = {
                "R": (rope_knots[0][0], rope_knots[0][1] + 1),
                "D": (rope_knots[0][0] + 1, rope_knots[0][1]),
                "L": (rope_knots[0][0], rope_knots[0][1] - 1),
                "U": (rope_knots[0][0] - 1, rope_knots[0][1])
            }
            new_knot_head_pos = rope_head_mover[direction]
            # print(f"New head pos is {new_knot_head_pos}")

            rope_knots[0] = new_knot_head_pos
            rec_following_knots_one(0)
            distance -= 1

            print(f"Current tail pos is {rope_knots[ROPE_LENGTH - 1]}")
            if rope_knots[ROPE_LENGTH - 1] not in visited_tail_pos:
                visited_tail_pos.append(rope_knots[ROPE_LENGTH - 1])

print(f"List: {visited_tail_pos}")
print(f"The tail visited {len(visited_tail_pos)} spaces")
