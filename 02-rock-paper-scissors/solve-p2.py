#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

with open(in_file_name) as RPS_file:
    # A = rock, B = paper, C = scissors
    # X = rock, Y = paper, Z = scissors
    total_score = 0
    score_map = {"A": 1, "B": 2, "C": 3}
    win_map = {"A": "B", "B": "C", "C":"A"} 
    draw_map = {"A": "A", "B":"B", "C":"C"}
    lose_map = {"A": "C", "B": "A", "C": "B"}

    for line in RPS_file:
        #print(f"Testing {line}")
        
        # Score the round
        score = 0
        opponent_choice, game_outcome = line.split()[0:2]
        
        if game_outcome == "X":
            # Player loses
            score += score_map[lose_map[opponent_choice]]

        elif game_outcome == "Y":
            # Player draws
            score += 3 + score_map[draw_map[opponent_choice]]
        else:
            # Player wins
            score += 6 + score_map[win_map[opponent_choice]]

        print(f"The score for this round is {score}")
        total_score += score

print(f"The total score is {total_score}")