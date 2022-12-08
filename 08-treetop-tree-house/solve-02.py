#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

tree_grid = []

with open(in_file_name) as tree_map_file:
    for line in tree_map_file:
        row = [int(t) for t in line.rstrip()]
        tree_grid.append(row)

# print(f"{tree_grid}")

tree_grid_size = len(tree_grid)
max_scenic_score = 0

for r in range(0, tree_grid_size):
    for c in range(0, tree_grid_size):
        # print(f"Checking spot {r},{c} w/ height {tree_grid[r][c]}")
        up_distance = 0
        down_distance = 0
        left_distance = 0
        right_distance = 0

        for curr_r in range(r - 1, -1, -1):
            up_distance += 1
            if tree_grid[curr_r][c] >= tree_grid[r][c]:
                break

        for curr_r in range(r + 1, tree_grid_size):
            down_distance += 1
            if tree_grid[curr_r][c] >= tree_grid[r][c]:
                break

        for curr_c in range(c - 1, -1, -1):
            left_distance += 1
            if tree_grid[r][curr_c] >= tree_grid[r][c]:
                break

        for curr_c in range(c + 1, tree_grid_size):
            right_distance += 1
            if tree_grid[r][curr_c] >= tree_grid[r][c]:
                break

        scenic_score = up_distance * down_distance * left_distance * right_distance
        print(f"Scenic score for spot {r}, {c} is {scenic_score}")
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(f"Max scenic score is {max_scenic_score} for the tree house")
