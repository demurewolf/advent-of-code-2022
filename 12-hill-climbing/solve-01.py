#!/usr/bin/env python3.8

from math import sqrt, pow, inf

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

height_map = []
start_pos = []
end_pos = []

with open(in_file_name) as height_map_file:
    row_count = 0
    for line in height_map_file:
        height_map.append(list(map(ord, line.rstrip())))

        if ord("S") in height_map[row_count]:
            start_pos = [row_count, line.index("S")]
            height_map[row_count][height_map[row_count].index(ord("S"))] = ord("a")
        if ord("E") in height_map[row_count]:
            end_pos = [row_count, line.index("E")]
            height_map[row_count][height_map[row_count].index(ord("E"))] = ord("z")

        row_count += 1

MAX_ROWS = row_count
MAX_COLS = len(height_map[0])
print(f"Read {MAX_ROWS} rows and {MAX_COLS} columns of data")


def print_height_map():
    for h in height_map:
        print("".join(map(chr, h)))


def print_costs():
    for c in cost_to_visit_pos:
        print(c)


def calc_distance_to_end(pos):
    return sqrt(pow(pos[0] - end_pos[0], 2) + pow(pos[1] - end_pos[1], 2))


def init_costs(rows, cols):
    costs = []
    for r in range(rows):
        cost_row = [inf] * cols
        costs.append(cost_row)

    return costs


# print_height_map()
print(f"Starting at {start_pos} and getting to {end_pos}")

pos_to_visit = {(start_pos[0], start_pos[1])}
visited_pos = set()
# cost_to_visit_pos = [[0] * MAX_COLS] * MAX_ROWS
cost_to_visit_pos = init_costs(MAX_ROWS, MAX_COLS)
cost_to_visit_pos[start_pos[0]][start_pos[1]] = 0

print_costs()

while len(pos_to_visit):
    position = min(pos_to_visit, key=lambda p: cost_to_visit_pos[p[0]][p[1]])
    # position = min(pos_to_visit, key=lambda p: calc_distance_to_end(p))
    pos_to_visit.remove(position)
    # position = pos_to_visit.pop()
    # Add current location to visited set
    print(position)

    if position == end_pos:
        # If it is, break out of the loop
        break

    row, col = position
    height_limit = height_map[row][col]
    steps = cost_to_visit_pos[row][col]
    unvisited_neighbors = set()

    visited_pos.add(position)

    # check down neighbor
    if row < MAX_ROWS - 1 and height_limit - height_map[row + 1][col] >= -1 and (row + 1, col) not in visited_pos:
        unvisited_neighbors.add((row + 1, col))
    # check up neighbor
    if row > 0 and height_limit - height_map[row - 1][col] >= -1 and (row - 1, col) not in visited_pos:
        unvisited_neighbors.add((row - 1, col))
    # check right neighbor
    if col < MAX_COLS - 1 and height_limit - height_map[row][col + 1] >= -1 and (row, col + 1) not in visited_pos:
        unvisited_neighbors.add((row, col + 1))
    # check left neighbor
    if col > 0 and height_limit - height_map[row][col - 1] >= -1 and (row, col - 1) not in visited_pos:
        unvisited_neighbors.add((row, col - 1))

    if len(unvisited_neighbors):
        # next_pos = min(unvisited_neighbors, key=lambda p: calc_distance_to_end(p))

        for unvisited in unvisited_neighbors:
            unv_row, unv_col = unvisited
            if cost_to_visit_pos[unv_row][unv_col] > steps + 1:
                cost_to_visit_pos[unv_row][unv_col] = steps + 1

        pos_to_visit.update(unvisited_neighbors)


steps_to_reach = cost_to_visit_pos[end_pos[0]][end_pos[1]]
print_costs()
print(f"Reached the last pos in {steps_to_reach} steps")
