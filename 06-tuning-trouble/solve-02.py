#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

MARKER_LEN = 14

with open(in_file_name) as signal_file:
    signal = signal_file.readline()

    for s in range(len(signal) - MARKER_LEN):
        print(f"{signal[s:s+MARKER_LEN]}")
        marker = signal[s:s+MARKER_LEN]
        marker_letters = {}
        marker_flag = True

        for m in marker:
            if m not in marker_letters:
                marker_letters[m] = 0
            marker_letters[m] += 1
        

        for letter_count in marker_letters.values():
            if letter_count > 1:
                marker_flag = False
                break
        
        if marker_flag:
            print(f"Marker found after {s + MARKER_LEN} characters processed")
            break

