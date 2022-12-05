#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

with open(in_file_name) as RPS_file:
    # A = rock, B = paper, C = scissors
    # X = rock, Y = paper, Z = scissors
    total_score = 0
    score_map = {"X": 1, "Y": 2, "Z": 3}
    win_map = {"A": "Y", "B": "Z", "C":"X"} # This shows where the player will win the round of RPS
    draw_map = {"A": "X", "B":"Y", "C":"Z"}

    for line in RPS_file:
        #print(f"Testing {line}")
        
        # Score the round
        score = 0
        opponent_choice, player_choice = line.split()[0:2]
        
        score += score_map[player_choice]
        if win_map[opponent_choice] == player_choice:
            score += 6
        elif draw_map[opponent_choice] == player_choice:
            score += 3

        print(f"The score for this round is {score}")
        total_score += score

print(f"The total score is {total_score}")