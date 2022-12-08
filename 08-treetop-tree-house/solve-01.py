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
visibility_count = 4 * (tree_grid_size - 1)

for r in range(1, tree_grid_size - 1):
    for c in range(1, tree_grid_size - 1):
        print(f"Checking spot {r},{c} w/ height {tree_grid[r][c]}")
        up_visible = True
        down_visible = True
        left_visible = True
        right_visible = True

        for curr_r in range(0, r):
            if tree_grid[curr_r][c] >= tree_grid[r][c]:
                up_visible = False

        for curr_r in range(r + 1, tree_grid_size):
            if tree_grid[curr_r][c] >= tree_grid[r][c]:
                down_visible = False

        for curr_c in range(0, c):
            if tree_grid[r][curr_c] >= tree_grid[r][c]:
                left_visible = False

        for curr_c in range(c + 1, tree_grid_size):
            if tree_grid[r][curr_c] >= tree_grid[r][c]:
                right_visible = False

        visible = up_visible or down_visible or left_visible or right_visible
        if visible:
            print("Visible tree!")

        visibility_count += 1 if visible else 0

print(f"Found {visibility_count} visible trees")            
